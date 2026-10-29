from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime, time
from enum import Enum


class AppointmentStatus(Enum):
    PENDING = "Pending"
    ACCEPTED = "Accepted"
    DECLINED = "Declined"


@dataclass
class AvailabilitySlot:
    slotId: str
    date: date
    startTime: time
    endTime: time
    isAvailable: bool = True

    def __str__(self) -> str:
        return (
            f"{self.slotId}: {self.date:%a, %b %d, %Y} "
            f"{self.startTime:%H:%M}-{self.endTime:%H:%M}"
        )


@dataclass
class Patient:
    patientId: str
    name: str
    appointments: list[Appointment] = field(default_factory=list)


@dataclass
class Doctor:
    doctorId: str
    name: str
    availabilitySlots: list[AvailabilitySlot] = field(default_factory=list)


@dataclass
class Staff:
    staffId: str
    name: str
    authorization_level: str = "staff"


@dataclass
class Appointment:
    appointmentId: str
    patient: Patient
    doctor: Doctor
    slot: AvailabilitySlot
    status: AppointmentStatus
    requestedAt: datetime = field(default_factory=datetime.now)

    def accept(self) -> None:
        if self.status is not AppointmentStatus.PENDING:
            raise ValueError("Only pending requests can be accepted.")
        if not self.slot.isAvailable:
            raise ValueError("This time slot is no longer available.")
        self.status = AppointmentStatus.ACCEPTED
        self.slot.isAvailable = False

    def decline(self) -> None:
        if self.status is not AppointmentStatus.PENDING:
            raise ValueError("Only pending requests can be declined.")
        self.status = AppointmentStatus.DECLINED


@dataclass
class MedicalRecord:
    recordId: str
    medicalData: str
    patientId: str | None = None