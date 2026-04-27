# Functional Requirements - ImparaTo

## General Description
The web application allows users to search for tutors and book personalized lessons based on their learning needs.  
Users can also register as tutors and offer personalized lessons in specific subjects or skills.

## Functional Requirements

### FR1 - Registration and Authentication
- The user must be able to register by creating a personal account, providing:
  - First name and last name.
  - Email address.
  - Password.
- After registration, the user must be able to log in by entering their email and password.
- In case of incorrect credentials, an error message must be displayed.
- A password recovery system must be provided.

### FR2 - Tutor Profile Creation
- A user who wants to offer lessons must be able to register as a tutor by creating a tutor profile.
- The tutor profile must include:
  - Personal information.
  - Subjects or skills taught.
  - A short biography or presentation.
  - Availability for lessons.
  - Lesson format (online, in person, or both).
  - Hourly rate.

### FR3 - Search for Tutors
- After authentication, the user must be able to search for available tutors.
- The user must be able to filter tutors by:
  - Subject or skill.
  - Availability.
  - Lesson format (online or in person).
  - Price range.
- For each tutor, the platform must display:
  - Name.
  - Subjects taught.
  - Short description.
  - Hourly rate.
  - Availability.

### FR4 - Tutor Profile Viewing
- The user must be able to view the full profile of a tutor.
- For each tutor profile, the system must display:
  - Personal presentation.
  - Subjects or skills offered.
  - Lesson format.
  - Availability.
  - Hourly rate.
  - Reviews or ratings, if available.

### FR5 - Lesson Booking
- The user must be able to book a personalized lesson with a selected tutor.
- The user must be able to choose:
  - Date.
  - Time slot.
  - Lesson format.
- Upon confirmation, the system must:
  - Record the booking and associate it with both the student and the tutor.
  - Update the tutor’s availability.
  - Display a confirmation message.

### FR6 - Viewing Personal Bookings
- The user must be able to view the list of their upcoming and past bookings.
- For each booking, the following must be displayed:
  - Tutor name.
  - Subject.
  - Date.
  - Time slot.
  - Lesson format.

### FR7 - Booking Cancellation
- The user must be able to cancel a booking before the scheduled lesson start time.
- In case of cancellation, the system must restore the tutor’s availability for that time slot.

### FR8 - Tutor Booking Management
- A tutor must be able to view all upcoming and past lessons booked with students.
- For each lesson, the tutor must be able to see:
  - Student name.
  - Subject.
  - Date.
  - Time slot.
  - Lesson format.

### FR9 - Availability Management
- A tutor must be able to set and update their availability.
- The system must prevent double bookings for the same tutor and time slot.

### FR10 - Notifications (NO)
- The system must send a confirmation email to both the student and the tutor when a lesson is booked.
- The system must send a reminder before the scheduled lesson.

## Additional Notes
- The application must be responsive and usable on mobile devices.