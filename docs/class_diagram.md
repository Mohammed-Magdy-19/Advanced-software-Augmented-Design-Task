# Clinic Appointment Booking System — Class Diagram

The diagram models the patients, doctors, appointment requests, and availability slots used by the documented use cases. It also shows the services responsible for booking rules, notifications, and protecting medical data.

```mermaid
classDiagram
    direction LR

    class Patient {
        +String patientId
        +String name
    }

    class Doctor {
        +String doctorId
        +String name
    }

    class Staff {
        +String staffId
        +String name
    }

    class AvailabilitySlot {
        +String slotId
        +Date date
        +Time startTime
        +Time endTime
        +Boolean isAvailable
    }

    class Appointment {
        +String appointmentId
        +AppointmentStatus status
        +DateTime requestedAt
        +accept()
        +decline()
    }

    class AppointmentStatus {
        <<enumeration>>
        Pending
        Accepted
        Declined
    }

    class MedicalRecord {
        +String recordId
        +String medicalData
    }

    class AppointmentService {
        +viewAvailability(doctorId)
        +bookAppointment(patientId, slotId)
        +reviewRequest(appointmentId, decision)
    }

    class NotificationService {
        +notifyPatient(appointment)
        +notifyDoctor(appointment)
    }

    class MedicalRecordAccessService {
        +canAccess(staff, record)
        +getMedicalRecord(staff, recordId)
    }

    Doctor "1" --> "0..*" AvailabilitySlot : provides
    Patient "1" --> "0..*" Appointment : requests
    Doctor "1" --> "0..*" Appointment : reviews
    AvailabilitySlot "1" <-- "0..*" Appointment : requested for
    Appointment --> AppointmentStatus : has status
    Patient "1" *-- "0..*" MedicalRecord : owns

    AppointmentService ..> Patient : checks appointment limit
    AppointmentService ..> Doctor : reads schedule
    AppointmentService ..> AvailabilitySlot : checks availability
    AppointmentService ..> Appointment : creates and updates
    AppointmentService ..> NotificationService : sends notifications
    MedicalRecordAccessService ..> Staff : verifies authorization
    MedicalRecordAccessService ..> MedicalRecord : controls access to
```

## Rules and requirement mapping

- **R1, R2, R3:** `AppointmentService` displays availability, creates pending requests, and processes a doctor's accept or decline decision.
- **R4:** A patient may have at most **7 upcoming appointments**. `AppointmentService` enforces this before creating a request.
- **R5:** Medical-record access goes through `MedicalRecordAccessService`; only authorized staff may access a `MedicalRecord`.
- **R6:** Availability returned by `viewAvailability` must be displayed within **2 seconds**.
- **R7:** The application screens for these interactions must be usable on mobile phone screens.
- An appointment has one patient, one doctor, and one requested time slot. Its status is `Pending`, `Accepted`, or `Declined`.
- A slot must be available to create a booking request. Accepting a request makes the slot unavailable; declining it leaves the slot available.
