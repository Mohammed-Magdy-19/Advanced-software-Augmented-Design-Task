from __future__ import annotations

from datetime import datetime
from time import perf_counter

if __package__:
    from .models import (
        Appointment,
        AppointmentStatus,
        AvailabilitySlot,
        Doctor,
        MedicalRecord,
        Patient,
        Staff,
    )
else:
    from models import (
        Appointment,
        AppointmentStatus,
        AvailabilitySlot,
        Doctor,
        MedicalRecord,
        Patient,
        Staff,
    )


MAX_UPCOMING_APPOINTMENTS = 7


class NotificationService:
    @staticmethod
    def notifyPatient(appointment: Appointment) -> None:
        print(
            f"[Patient notification] {appointment.patient.name}: appointment "
            f"{appointment.appointmentId} is {appointment.status.value.lower()} "
            f"for {appointment.slot}."
        )

    @staticmethod
    def notifyDoctor(appointment: Appointment) -> None:
        print(
            f"[Doctor notification] Dr. {appointment.doctor.name}: new request "
            f"{appointment.appointmentId} from {appointment.patient.name} "
            f"for {appointment.slot}."
        )


class MedicalRecordAccessService:
    AUTHORIZED_LEVELS = {"clinician", "records_admin"}

    def __init__(self, records: dict[str, MedicalRecord]) -> None:
        self.records = records

    def canAccess(self, staff: Staff, record: MedicalRecord) -> bool:
        return (
            staff.authorization_level.strip().lower() in self.AUTHORIZED_LEVELS
            and self.records.get(record.recordId) is record
        )

    def getMedicalRecord(self, staff: Staff, recordId: str) -> str:
        record = self.records.get(recordId)
        if record is None:
            raise KeyError(f"Medical record {recordId!r} was not found.")
        if not self.canAccess(staff, record):
            raise PermissionError("Access denied: staff is not authorized.")
        return record.medicalData


class AppointmentService:
    def __init__(
        self,
        patients: dict[str, Patient],
        doctors: dict[str, Doctor],
        notification_service: NotificationService | None = None,
    ) -> None:
        self.patients = patients
        self.doctors = doctors
        self.appointments: dict[str, Appointment] = {}
        self.notification_service = notification_service or NotificationService()
        self._next_appointment_number = 1

    def viewAvailability(self, doctorId: str) -> list[AvailabilitySlot]:
        start = perf_counter()
        doctor = self.doctors.get(doctorId)
        if doctor is None:
            raise KeyError(f"Doctor {doctorId!r} was not found.")

        now = datetime.now()
        slots = [
            slot
            for slot in doctor.availabilitySlots
            if slot.isAvailable
            and datetime.combine(slot.date, slot.startTime) > now
        ]
        elapsed = perf_counter() - start
        print(f"Availability lookup: {elapsed:.4f}s (target: under 2s).")
        return sorted(slots, key=lambda slot: (slot.date, slot.startTime))

    @staticmethod
    def _is_upcoming(appointment: Appointment, now: datetime) -> bool:
        return (
            appointment.status
            in {AppointmentStatus.PENDING, AppointmentStatus.ACCEPTED}
            and datetime.combine(
                appointment.slot.date, appointment.slot.startTime
            )
            > now
        )

    def _upcoming_count(self, patient: Patient) -> int:
        now = datetime.now()
        return sum(
            self._is_upcoming(appointment, now)
            for appointment in patient.appointments
        )

    def bookAppointment(self, patientId: str, slotId: str) -> Appointment:
        patient = self.patients.get(patientId)
        if patient is None:
            raise KeyError(f"Patient {patientId!r} was not found.")

        doctor_and_slot = next(
            (
                (doctor, slot)
                for doctor in self.doctors.values()
                for slot in doctor.availabilitySlots
                if slot.slotId == slotId
            ),
            None,
        )
        if doctor_and_slot is None:
            raise KeyError(f"Availability slot {slotId!r} was not found.")
        doctor, slot = doctor_and_slot
        if not slot.isAvailable or datetime.combine(
            slot.date, slot.startTime
        ) <= datetime.now():
            raise ValueError("This time slot is no longer available.")
        if self._upcoming_count(patient) >= MAX_UPCOMING_APPOINTMENTS:
            raise ValueError(
                "Appointment limit reached "
                f"({MAX_UPCOMING_APPOINTMENTS} upcoming appointments)."
            )

        appointment_id = f"A{self._next_appointment_number:03d}"
        self._next_appointment_number += 1
        appointment = Appointment(
            appointmentId=appointment_id,
            patient=patient,
            doctor=doctor,
            slot=slot,
            status=AppointmentStatus.PENDING,
        )
        self.appointments[appointment_id] = appointment
        patient.appointments.append(appointment)
        self.notification_service.notifyDoctor(appointment)
        return appointment

    def reviewRequest(self, appointmentId: str, decision: str) -> Appointment:
        appointment = self.appointments.get(appointmentId)
        if appointment is None:
            raise KeyError(f"Appointment {appointmentId!r} was not found.")

        normalized_decision = decision.strip().lower()
        if normalized_decision == "accept":
            appointment.accept()
        elif normalized_decision == "decline":
            appointment.decline()
        else:
            raise ValueError("Decision must be 'accept' or 'decline'.")
        self.notification_service.notifyPatient(appointment)
        return appointment