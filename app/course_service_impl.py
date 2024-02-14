from app.course_service import CourseService
from app.models import Course, Student

class CourseServiceImpl(CourseService):
    def __init__(self):
        self.courses = {}  # course_id: Course object
        self.students = {}  # student_id: Student object
        self.next_course_id = 1
        self.next_student_id = 1

    def get_courses(self):
        """Returns a list of all courses."""
        return list(self.courses.values())

    def get_course_by_id(self, course_id):
        """Returns a course by its id."""
        return self.courses.get(course_id)

    def create_course(self, course_name):
        """Creates a new course."""
        course_id = self.next_course_id
        self.courses[course_id] = Course(course_id, course_name)
        self.next_course_id += 1
        return course_id

    def delete_course(self, course_id):
        """Deletes a course by its id."""
        if course_id in self.courses:
            del self.courses[course_id]
            return True
        return False

    def create_assignment(self, course_id, assignment_name):
        """Creates a new assignment for a course."""
        if course_id in self.courses:
            return self.courses[course_id].add_assignment(assignment_name)
        return None

    def enroll_student(self, course_id, student_id):
        """Enrolls a student in a course."""
        if course_id not in self.courses or student_id not in self.students:
            return False
        course = self.courses[course_id]
        student = self.students[student_id]
        return course.enroll_student(student)

    def dropout_student(self, course_id, student_id):
        """Drops a student from a course."""
        if course_id in self.courses and student_id in self.students:
            course = self.courses[course_id]
            if student_id in course.enrolled_students:
                del course.enrolled_students[student_id]
                del self.students[student_id].enrolled_courses[course_id]
                return True
        return False

    def submit_assignment(self, course_id, student_id, assignment_id, grade):
        """Submits an assignment for a student."""
        if course_id in self.courses and student_id in self.students:
            course = self.courses[course_id]
            return course.submit_assignment(student_id, assignment_id, grade)
        return False

    def get_assignment_grade_avg(self, course_id, assignment_id):
        """Returns the average grade for an assignment."""
        if course_id in self.courses:
            course = self.courses[course_id]
            return course.get_assignment_average(assignment_id)
        return 0

    def get_student_grade_avg(self, course_id, student_id):
        """Returns the average grade for a student in a course."""
        if course_id in self.courses and student_id in self.students:
            student = self.students[student_id]
            return student.get_average_grade(course_id)
        return 0

    def get_top_five_students(self, course_id):
        """Returns the IDs of the top 5 students in a course based on their average grades."""
        if course_id not in self.courses:
            return []

        course = self.courses[course_id]
        averages = {student_id: student.get_average_grade(course_id) for student_id, student in course.enrolled_students.items()}
        sorted_students = sorted(averages.items(), key=lambda x: x[1], reverse=True)[:5]
        return [student_id for student_id, _ in sorted_students]

    # Additional methods to manage students
    def create_student(self):
        """Creates a new student."""
        student_id = self.next_student_id
        self.students[student_id] = Student(student_id)
        self.next_student_id += 1
        return student_id
