from __future__ import annotations

from datetime import date, time, timedelta

if __package__:
    from .models import (
        AppointmentStatus,
        AvailabilitySlot,
        Doctor,
        MedicalRecord,
        Patient,
        Staff,
    )
    from .services import AppointmentService, MedicalRecordAccessService
else:
    from models import (
        AppointmentStatus,
        AvailabilitySlot,
        Doctor,
        MedicalRecord,
        Patient,
        Staff,
    )
    from services import AppointmentService, MedicalRecordAccessService


def build_sample_app() -> tuple[
    AppointmentService,
    dict[str, Staff],
    MedicalRecordAccessService,
]:
    sample_day = date.today() + timedelta(days=1)
    doctor = Doctor(
        doctorId="D001",
        name="Maya Chen",
        availabilitySlots=[
            AvailabilitySlot("S001", sample_day, time(10, 0), time(10, 30)),
            AvailabilitySlot("S002", sample_day, time(11, 0), time(11, 30)),
            AvailabilitySlot("S003", sample_day, time(14, 0), time(14, 30)),
            AvailabilitySlot("S004", sample_day, time(15, 0), time(15, 30)),
            AvailabilitySlot("S005", sample_day, time(16, 0), time(16, 30)),
            AvailabilitySlot("S006", sample_day, time(16, 30), time(17, 0)),
            AvailabilitySlot("S007", sample_day, time(17, 0), time(17, 30)),
            AvailabilitySlot("S008", sample_day, time(17, 30), time(18, 0)),
            AvailabilitySlot("S009", sample_day, time(18, 0), time(18, 30)),
            AvailabilitySlot("S010", sample_day, time(18, 30), time(19, 0)),
        ],
    )
    patient = Patient(patientId="P001", name="Jordan Lee")
    staff = {
        "ST001": Staff("ST001", "Alex Rivera", "clinician"),
        "ST002": Staff("ST002", "Sam Taylor", "receptionist"),
    }
    records = {
        "R001": MedicalRecord(
            recordId="R001",
            medicalData="Sample record: seasonal allergies.",
            patientId=patient.patientId,
        )
    }
    appointment_service = AppointmentService(
        patients={patient.patientId: patient},
        doctors={doctor.doctorId: doctor},
    )
    return (
        appointment_service,
        staff,
        MedicalRecordAccessService(records),
    )


def _read_choice(prompt: str, valid_choices: set[str]) -> str:
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print(f"Choose one of: {', '.join(sorted(valid_choices))}.")


def _show_doctors(service: AppointmentService) -> None:
    print("\nDoctors:")
    for doctor in service.doctors.values():
        print(f"  {doctor.doctorId} - Dr. {doctor.name}")


def _show_availability(service: AppointmentService) -> None:
    _show_doctors(service)
    doctor_id = input("Doctor ID (blank for D001): ").strip() or "D001"
    try:
        slots = service.viewAvailability(doctor_id)
    except KeyError as error:
        print(error)
        return

    if not slots:
        print("No available upcoming slots.")
        return
    print("Available slots:")
    for slot in slots:
        print(f"  {slot}")


def _book_appointment(service: AppointmentService) -> None:
    patient_id = input("Patient ID (P001): ").strip() or "P001"
    _show_doctors(service)
    doctor_id = input("Doctor ID (D001): ").strip() or "D001"
    try:
        slots = service.viewAvailability(doctor_id)
    except KeyError as error:
        print(error)
        return

    if not slots:
        print("No available upcoming slots.")
        return
    for slot in slots:
        print(f"  {slot}")

    slot_id = input("Slot ID: ").strip()
    try:
        appointment = service.bookAppointment(patient_id, slot_id)
    except (KeyError, ValueError) as error:
        print(f"Booking not completed: {error}")
        return
    print(
        f"Request {appointment.appointmentId} submitted with status "
        f"{appointment.status.value}."
    )


def _review_pending_requests(service: AppointmentService) -> None:
    pending = [
        appointment
        for appointment in service.appointments.values()
        if appointment.status is AppointmentStatus.PENDING
    ]
    if not pending:
        print("There are no pending requests.")
        return

    print("Pending requests:")
    for appointment in pending:
        print(
            f"  {appointment.appointmentId}: {appointment.patient.name}, "
            f"Dr. {appointment.doctor.name}, {appointment.slot}"
        )
    appointment_id = input("Request ID to review: ").strip()
    decision = _read_choice("Decision (a)ccept / (d)ecline: ", {"a", "d"})
    try:
        appointment = service.reviewRequest(
            appointment_id, "accept" if decision == "a" else "decline"
        )
    except (KeyError, ValueError) as error:
        print(f"Request not updated: {error}")
        return
    print(f"Request {appointment.appointmentId} is now {appointment.status.value}.")


def _access_medical_record(
    staff_members: dict[str, Staff],
    access_service: MedicalRecordAccessService,
) -> None:
    print("Staff:")
    for staff in staff_members.values():
        print(f"  {staff.staffId} - {staff.name} ({staff.authorization_level})")
    staff_id = input("Staff ID: ").strip()
    staff = staff_members.get(staff_id)
    if staff is None:
        print("Access denied: staff member not found.")
        return

    record_id = input("Medical record ID (R001): ").strip() or "R001"
    try:
        data = access_service.getMedicalRecord(staff, record_id)
    except (KeyError, PermissionError) as error:
        print(error)
        return
    print(f"Authorized record data: {data}")


def main() -> None:
    service, staff_members, record_access = build_sample_app()
    actions = {
        "1": "View doctor availability",
        "2": "Book an appointment",
        "3": "Review pending requests",
        "4": "Access a medical record",
        "5": "Exit",
    }
    print("Clinic Appointment Booking System")
    print("Demo patient: P001 | Demo doctor: D001 | Demo record: R001")

    while True:
        menu = " | ".join(
            f"{key}. {label}" for key, label in actions.items()
        )
        print(f"\n{menu}")
        choice = _read_choice("Select an option: ", set(actions))
        if choice == "1":
            _show_availability(service)
        elif choice == "2":
            _book_appointment(service)
        elif choice == "3":
            _review_pending_requests(service)
        elif choice == "4":
            _access_medical_record(staff_members, record_access)
        else:
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()