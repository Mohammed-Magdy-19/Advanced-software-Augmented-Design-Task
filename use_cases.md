# Clinic Appointment Booking System — Use Cases

**Actors:** Patient, Doctor  
**N = 7** (maximum upcoming appointments per patient, as specified for this team)

> See [use_case_diagram.md](use_case_diagram.md) for the Mermaid use case diagram.

---

## UC1 — View Doctor Availability

| Field | Description |
|---|---|
| **Use Case ID** | UC1 |
| **Use Case Name** | View Doctor Availability |
| **Primary Actor** | Patient |
| **Goal** | The Patient views a doctor's available days and time slots so that they can choose a suitable slot to book. |
| **Preconditions** | The Patient is authenticated in the system. The Doctor has at least one availability record in the system. |
| **Main Flow** | 1. The Patient selects a doctor from the list. <br>2. The system retrieves and displays the doctor's available days and time slots within 2 seconds (R6). <br>3. The Patient reviews the available slots. |
| **Postconditions** | The Patient can see a list of available days and time slots for the selected doctor. |
| **Alternative Flow A** | **No availability found:** If the selected doctor has no available slots, the system displays a message indicating no availability, and the use case ends. |

**Requirements covered:** R1, R6

---

## UC2 — Book an Appointment

| Field | Description |
|---|---|
| **Use Case ID** | UC2 |
| **Use Case Name** | Book an Appointment |
| **Primary Actor** | Patient |
| **Goal** | The Patient selects an available time slot and submits a booking request for an appointment with a doctor. |
| **Preconditions** | The Patient is authenticated in the system. The Patient has completed UC1 and can see at least one available slot. The Patient currently has fewer than 7 upcoming appointments (N = 7). |
| **Main Flow** | 1. The Patient selects an available time slot from the doctor's schedule. <br>2. The Patient confirms the booking request. <br>3. The system checks that the selected slot is still available. <br>4. The system checks that the Patient does not already have 7 upcoming appointments. <br>5. The system records the booking request with status "Pending". <br>6. The system notifies the Doctor of the new pending request. <br>7. The system confirms to the Patient that the request has been submitted. |
| **Postconditions** | A pending appointment request exists in the system for the selected slot. The doctor receives a notification of the pending request. |
| **Alternative Flow A** | **Slot no longer available:** If at step 3 the selected slot has already been taken, the system informs the Patient that the slot is no longer available, refreshes the availability display, and returns to step 1. The booking request is not created. |
| **Alternative Flow B** | **Appointment limit reached:** If at step 4 the Patient already has 7 upcoming appointments, the system informs the Patient that they have reached the maximum limit of 7 upcoming appointments and cannot book another. The use case ends without creating a request. |

**Requirements covered:** R2, R4

---

## UC3a — Accept Appointment Request

| Field | Description |
|---|---|
| **Use Case ID** | UC3a |
| **Use Case Name** | Accept Appointment Request |
| **Primary Actor** | Doctor |
| **Goal** | The Doctor accepts a pending appointment request, confirming the appointment. |
| **Preconditions** | The Doctor is authenticated in the system. At least one pending appointment request exists for the Doctor. |
| **Main Flow** | 1. The Doctor opens the list of pending appointment requests. <br>2. The Doctor selects a specific request to review. <br>3. The system displays the request details (Patient name, requested date, requested time slot). <br>4. The Doctor chooses to accept the request. <br>5. The system updates the appointment status to "Accepted". <br>6. The system marks the time slot as no longer available for new bookings. <br>7. The system notifies the Patient that their request has been accepted. |
| **Postconditions** | The appointment status is "Accepted". The time slot is no longer available. The Patient is notified of the acceptance. |
| **Alternative Flow A** | **Request already handled:** If at step 2 the selected request is no longer pending (already accepted or declined by a concurrent action), the system displays a message that the request is no longer available, and the use case ends. |

**Requirements covered:** R3

---

## UC3b — Decline Appointment Request

| Field | Description |
|---|---|
| **Use Case ID** | UC3b |
| **Use Case Name** | Decline Appointment Request |
| **Primary Actor** | Doctor |
| **Goal** | The Doctor declines a pending appointment request, freeing the time slot for other patients. |
| **Preconditions** | The Doctor is authenticated in the system. At least one pending appointment request exists for the Doctor. |
| **Main Flow** | 1. The Doctor opens the list of pending appointment requests. <br>2. The Doctor selects a specific request to review. <br>3. The system displays the request details (Patient name, requested date, requested time slot). <br>4. The Doctor chooses to decline the request. <br>5. The system updates the appointment status to "Declined". <br>6. The time slot remains available for new bookings. <br>7. The system notifies the Patient that their request has been declined. |
| **Postconditions** | The appointment status is "Declined". The time slot remains available. The Patient is notified of the decline. |
| **Alternative Flow A** | **Request already handled:** If at step 2 the selected request is no longer pending, the system displays a message that the request is no longer available, and the use case ends. |

**Requirements covered:** R3

---

## System-Wide Constraints

The following non-functional requirements apply across the entire system and are not tied to a single use case interaction.

| Requirement | Type | Application |
|---|---|---|
| R5 — Security | Non-Functional | Patient medical data is accessible only to authenticated and authorized staff. Access control is enforced at the system level across all use cases. |
| R6 — Performance | Non-Functional | The availability display (UC1, step 2) must respond within 2 seconds. This is enforced by the system architecture. |
| R7 — Mobile Usability | Non-Functional | All screens involved in UC1, UC2, UC3a, and UC3b must be usable on mobile phone screen sizes. |

---

## Requirement Coverage Table

| Requirement | Type | Covered By |
|---|---|---|
| R1 — View Doctor Availability | Functional | UC1 |
| R2 — Book an Appointment | Functional | UC2 |
| R3 — Accept or Decline Request | Functional | UC3a, UC3b |
| R4 — Max N = 7 Upcoming Appointments | Functional | UC2 (Alternative Flow B and step 4) |
| R5 — Medical Data Security | Non-Functional | System-wide constraint (authentication/authorization layer) |
| R6 — 2-Second Response Time | Non-Functional | UC1 (step 2); system-wide performance constraint |
| R7 — Mobile Usability | Non-Functional | System-wide UI constraint (all use cases) |
