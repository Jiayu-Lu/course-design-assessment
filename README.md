# Course Management System Design Document

## Overview

This document outlines design for a Course Management System focused on managing courses, students, assignments, and grades using in-memory data structures, without external persistence or a frontend interface.



### Data Structures

- **Dictionaries and Lists**: Python dictionaries and lists are used to store and manage data regarding users, courses, enrollments, assignments, and grades.



### Project Structure

```
course-design-assessment/
├── main.py
│
├── app/                  # Application code
│   ├── course_service.py         # Interface definition
│   ├── course_service_impl.py    # Implementation of the interface
│   └── models.py                 # Data models
│
└── tests/                # Unit tests
    └── test_course_service_impl.py
```



### Running Tests

From the root directory (`course-design-assessment-main/`), execute all unit tests by running:

```
python -m unittest discover -s tests
```



### Models.py

#### Course Class

- **Purpose**: Represents a course with a unique ID, name, assignments, and enrolled students.
- **Attributes**:
  - `course_id`: A unique identifier for the course.
  - `course_name`: The name of the course.
  - `assignments`: A dictionary to store assignments by assignment ID.
  - `enrolled_students`: A dictionary to keep track of students enrolled in the course by student ID.
- **Methods**:
  - `add_assignment(assignment_name)`: Adds a new assignment to the course.
  - `enroll_student(student)`: Enrolls a student in the course.
  - `submit_assignment(student_id, assignment_id, grade)`: Records a grade for a student's assignment submission.
  - `get_assignment_average(assignment_id)`: Calculates the average grade for an assignment across all submissions.

#### Student Class

- **Purpose**: Represents a student with a unique ID and their enrollments and assignments.
- **Attributes**:
  - `student_id`: A unique identifier for the student.
  - `enrolled_courses`: A dictionary to store courses the student is enrolled in by course ID.
  - `assignments`: A nested dictionary to keep track of grades for assignments in each course.
- **Methods**:
  - `enroll_in_course(course)`: Enrolls the student in a given course.
  - `submit_assignment(course_id, assignment_id, grade)`: Submits a grade for an assignment in a course.
  - `get_average_grade(course_id)`: Calculates the student's average grade across all assignments in a course.



### CourseServiceImpl.py

#### Class Variables

- **`courses`**: A dictionary to store `Course` objects by their course ID. 
- **`students`**: A dictionary to store `Student` objects by their student ID. 
- **`next_course_id`**: An integer used to generate unique IDs for new courses.
- **`next_student_id`**: An integer used to generate unique IDs for new students.