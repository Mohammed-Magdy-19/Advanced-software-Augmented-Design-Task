# System Sequence Diagrams

## 1. View Doctor Availability
- **Description:** The Patient requests and reviews a Doctor's available days and time slots.
```mermaid
sequenceDiagram
    autonumber
    actor Patient
    participant AppointmentService

    Patient->>AppointmentService: viewAvailability(doctorId)
    activate AppointmentService
    Note over AppointmentService: Retrieves the selected Doctor's available slots.
    alt Available slots found
        AppointmentService-->>Patient: Available days and time slots
        Patient->>Patient: Reviews the available slots
    else No availability found
        AppointmentService-->>Patient: No availability found
    end
    deactivate AppointmentService
```

## 2. Book an Appointment
- **Description:** The Patient submits a booking request for an available slot, subject to availability and the seven-upcoming-appointments limit.
```mermaid
sequenceDiagram
    autonumber
    actor Patient
    participant AppointmentService
    participant AvailabilitySlot
    participant Appointment
    participant NotificationService
    actor Doctor

    loop Until booking succeeds or the appointment limit is reached
        Patient->>Patient: Selects an available slot and confirms
        Patient->>AppointmentService: bookAppointment(patientId, slotId)
        activate AppointmentService
        Note over AppointmentService: Checks that AvailabilitySlot.isAvailable is true and enforces the maximum of 7 upcoming appointments.
        alt Slot is no longer available
            AppointmentService-->>Patient: Slot is no longer available
            AppointmentService->>AppointmentService: viewAvailability(doctorId)
            AppointmentService-->>Patient: Refreshed available days and time slots
        else Appointment limit reached
            AppointmentService-->>Patient: Maximum of 7 upcoming appointments reached
            break Booking cannot continue
                Note over Patient,AppointmentService: The use case ends without creating an appointment.
            end
        else Slot available and limit not reached
            AppointmentService->>Appointment: Create appointment with status Pending
            activate Appointment
            Note right of Appointment: The appointment is associated with the Patient and selected AvailabilitySlot.
            deactivate Appointment
            AppointmentService->>NotificationService: notifyDoctor(appointment)
            activate NotificationService
            NotificationService-->>Doctor: New pending appointment request
            deactivate NotificationService
            AppointmentService-->>Patient: Booking request submitted
            break Booking request submitted
                Note over Patient,AppointmentService: The pending request has been recorded.
            end
        end
        deactivate AppointmentService
    end
```

## 3. Accept Appointment Request
- **Description:** The Doctor accepts a pending appointment request, making its time slot unavailable and notifying the Patient.
```mermaid
sequenceDiagram
    autonumber
    actor Doctor
    participant AppointmentService
    participant Appointment
    participant AvailabilitySlot
    participant NotificationService
    actor Patient

    Doctor->>Doctor: Opens pending requests and selects a request to review
    Doctor->>Doctor: Reviews request details and chooses to accept
    Doctor->>AppointmentService: reviewRequest(appointmentId, "accept")
    activate AppointmentService
    alt Request is no longer pending
        AppointmentService-->>Doctor: Request is no longer available
    else Request is pending
        AppointmentService->>Appointment: accept()
        activate Appointment
        deactivate Appointment
        AppointmentService->>AvailabilitySlot: isAvailable = false
        AppointmentService->>NotificationService: notifyPatient(appointment)
        activate NotificationService
        NotificationService-->>Patient: Appointment request accepted
        deactivate NotificationService
        AppointmentService-->>Doctor: Request accepted
    end
    deactivate AppointmentService
```

## 4. Decline Appointment Request
- **Description:** The Doctor declines a pending appointment request, leaves its time slot available, and notifies the Patient.
```mermaid
sequenceDiagram
    autonumber
    actor Doctor
    participant AppointmentService
    participant Appointment
    participant NotificationService
    actor Patient

    Doctor->>Doctor: Opens pending requests and selects a request to review
    Doctor->>Doctor: Reviews request details and chooses to decline
    Doctor->>AppointmentService: reviewRequest(appointmentId, "decline")
    activate AppointmentService
    alt Request is no longer pending
        AppointmentService-->>Doctor: Request is no longer available
    else Request is pending
        AppointmentService->>Appointment: decline()
        activate Appointment
        deactivate Appointment
        Note over AppointmentService: The declined request leaves its AvailabilitySlot available.
        AppointmentService->>NotificationService: notifyPatient(appointment)
        activate NotificationService
        NotificationService-->>Patient: Appointment request declined
        deactivate NotificationService
        AppointmentService-->>Doctor: Request declined
    end
    deactivate AppointmentService
```
