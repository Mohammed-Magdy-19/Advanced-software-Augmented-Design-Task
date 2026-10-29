# Clinic Appointment Booking System

## P1 — Requirements Classification

**Maximum upcoming appointments per patient (N): 7**

This document classifies the seven original system requirements into functional and non-functional requirements. The original requirement statements are preserved.

## 1. Functional Requirements

Functional requirements describe the services and behaviors the system must provide.

### R1 — View Doctor Availability

> A patient can view the days and times when a doctor is available.

**Classification:** Functional Requirement  
**Actor:** Patient

**Explanation:** The system must allow patients to view a doctor's available days and time slots.

### R2 — Book an Appointment

> A patient can book an appointment during an available time slot.

**Classification:** Functional Requirement  
**Actor:** Patient

**Explanation:** The system must allow a patient to request an appointment in an available time slot.

### R3 — Accept or Decline an Appointment Request

> A doctor can accept or decline an appointment request.

**Classification:** Functional Requirement  
**Actor:** Doctor

**Explanation:** The system must allow a doctor to review an appointment request and either accept or decline it.

### R4 — Maximum Number of Upcoming Appointments

> A patient can have at most N upcoming appointments at any given time.

**Classification:** Functional Requirement  
**Constraint:** `N = 7`

**Explanation:** The system must enforce the maximum number of upcoming appointments for each patient. For this team, a patient must not have more than **7 upcoming appointments** at any given time.

## 2. Non-Functional Requirements

Non-functional requirements describe quality attributes and constraints on the system's operation.

### R5 — Medical Data Access Control

> Patient medical data shall be accessible only to authorized staff.

**Classification:** Non-Functional Requirement  
**Quality attribute:** Security

**Explanation:** The system must protect patient medical data from unauthorized access and make it accessible only to authorized staff.

### R6 — Appointment Availability Response Time

> Available appointment times shall be displayed within 2 seconds.

**Classification:** Non-Functional Requirement  
**Quality attribute:** Performance

**Explanation:** The system must display available appointment times within **2 seconds**.

### R7 — Mobile Usability

> The application shall be usable on mobile phone screens.

**Classification:** Non-Functional Requirement  
**Quality attribute:** Usability

**Explanation:** The application must provide an interface that can be used on mobile phone screens.
