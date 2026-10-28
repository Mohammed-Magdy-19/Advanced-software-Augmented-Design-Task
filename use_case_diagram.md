# Clinic Appointment Booking System — Use Case Diagram

This diagram represents the actors and use cases of the Clinic Appointment Booking System.

**Actors:**
- **Patient** — views doctor availability and books appointments.
- **Doctor** — accepts or declines appointment requests.

```mermaid
usecase-beta
    direction LR

    actor Patient("Patient")
    actor Doctor("Doctor")

    systemBoundary "Clinic Appointment Booking System"
        ViewAvailability("View Doctor Availability")
        BookAppointment("Book an Appointment")
        AcceptRequest("Accept Appointment Request")
        DeclineRequest("Decline Appointment Request")
    end

    Patient --> ViewAvailability
    Patient --> BookAppointment

    Doctor --> AcceptRequest
    Doctor --> DeclineRequest
```

---

## Diagram Notes

| Element | Detail |
|---|---|
| **Patient** | External actor outside the system boundary. Initiates UC1 and UC2. |
| **Doctor** | External actor outside the system boundary. Initiates UC3a and UC3b. |
| **System boundary** | The `Clinic Appointment Booking System` block encloses all four use cases. |
| **View Doctor Availability** | UC1 — satisfies R1 and the R6 performance constraint (2-second response). |
| **Book an Appointment** | UC2 — satisfies R2 and enforces R4 (max N = 7 upcoming appointments per patient). |
| **Accept Appointment Request** | UC3a — satisfies R3 (accept path). |
| **Decline Appointment Request** | UC3b — satisfies R3 (decline path). |
| **R5, R6, R7** | Applied as system-wide constraints; not represented as separate use cases. |

Refer to [use_cases.md](use_cases.md) for full use case descriptions including preconditions, main flows, postconditions, and alternative flows.