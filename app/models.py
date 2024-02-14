class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        self.next_assignment_id = 0
        self.assignments = {}  # assignment_id: assignment_name
        self.enrolled_students = {}  # student_id: Student

    def add_assignment(self, assignment_name):
        """Adds an assignment to the course."""
        self.next_assignment_id += 1
        assignment_id = self.next_assignment_id
        self.assignments[assignment_id] = assignment_name
        return assignment_id

    def enroll_student(self, student):
        """Enrolls a student in the course."""
        if student.student_id not in self.enrolled_students:
            self.enrolled_students[student.student_id] = student
            student.enroll_in_course(self)
            return True
        return False

    def submit_assignment(self, student_id, assignment_id, grade):
        """Submits an assignment for a student."""
        if student_id in self.enrolled_students and assignment_id in self.assignments:
            student = self.enrolled_students[student_id]
            student.submit_assignment(self.course_id, assignment_id, grade)
            return True
        return False

    def get_assignment_average(self, assignment_id):
        """Calculates the average grade for an assignment."""
        total = 0
        count = 0
        for student in self.enrolled_students.values():
            if assignment_id in student.assignments[self.course_id]:
                total += student.assignments[self.course_id][assignment_id]
                count += 1
        return total // count if count else 0

class Student:
    def __init__(self, student_id):
        self.student_id = student_id
        self.enrolled_courses = {}  # course_id: Course
        self.assignments = {}  # course_id: {assignment_id: grade}

    def enroll_in_course(self, course):
        """Enrolls the student in a course."""
        if course.course_id not in self.enrolled_courses:
            self.enrolled_courses[course.course_id] = course
            self.assignments[course.course_id] = {}

    def submit_assignment(self, course_id, assignment_id, grade):
        """Submits an assignment for a course."""
        if course_id in self.enrolled_courses:
            self.assignments[course_id][assignment_id] = grade
            return True
        return False

    def get_average_grade(self, course_id):
        """Calculates the average grade of the student for a specific course."""
        if course_id in self.assignments:
            total = 0
            count = 0
            for grade in self.assignments[course_id].values():
                total += grade
                count += 1
            return total // count if count else 0
        return 0
