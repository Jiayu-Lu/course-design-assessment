import unittest
from app.course_service_impl import CourseServiceImpl

class TestCourseServiceImpl(unittest.TestCase):
    def setUp(self):
        """Initial setup before each test case."""
        self.service = CourseServiceImpl()
        # Assume create_student returns a student ID
        self.student_id = self.service.create_student()
        # Assume create_course returns a course ID
        self.course_id = self.service.create_course("Test Course")

    def create_student_and_enroll(self, grade):
        """Helper function to create a student, enroll in the course, and submit an assignment."""
        student_id = self.service.create_student()
        self.service.enroll_student(self.course_id, student_id)
        assignment_id = self.service.create_assignment(self.course_id, "General Assignment")
        self.service.submit_assignment(self.course_id, student_id, assignment_id, grade)
        return student_id

    def test_create_course(self):
        """Test creating a course and verifying its existence."""
        course_id = self.service.create_course("New Course")
        self.assertIsNotNone(self.service.get_course_by_id(course_id))

    def test_enroll_student(self):
        """Test enrolling a student in a course."""
        result = self.service.enroll_student(self.course_id, self.student_id)
        self.assertTrue(result)

    def test_create_assignment(self):
        """Test creating an assignment for a course."""
        assignment_id = self.service.create_assignment(self.course_id, "Assignment 1")
        self.assertIsNotNone(assignment_id)

    def test_submit_assignment(self):
        """Test submitting an assignment for a student."""
        assignment_id = self.service.create_assignment(self.course_id, "Assignment 1")
        self.service.enroll_student(self.course_id, self.student_id)

        result = self.service.submit_assignment(self.course_id, self.student_id, assignment_id, 85)
        self.assertTrue(result)

    def test_get_assignment_grade_avg(self):
        """Test calculating the average grade for an assignment."""
        student_id2 = self.service.create_student()

        assignment_id = self.service.create_assignment(self.course_id, "Assignment 1")
        self.service.enroll_student(self.course_id, self.student_id)
        self.service.enroll_student(self.course_id, student_id2)

        self.service.submit_assignment(self.course_id, self.student_id, assignment_id, 80)
        self.service.submit_assignment(self.course_id, student_id2, assignment_id, 70)
        avg_grade = self.service.get_assignment_grade_avg(self.course_id, assignment_id)
        self.assertEqual(avg_grade, 75)

    def test_get_student_grade_avg(self):
        """Test calculating the average grade for a student in a course."""
        self.service.enroll_student(self.course_id, self.student_id)

        assignment_id = self.service.create_assignment(self.course_id, "Assignment 1")
        assignment_id2 = self.service.create_assignment(self.course_id, "Assignment 2")

        self.service.submit_assignment(self.course_id, self.student_id, assignment_id, 90)
        self.service.submit_assignment(self.course_id, self.student_id, assignment_id2, 100)

        avg_grade = self.service.get_student_grade_avg(self.course_id, self.student_id)
        self.assertEqual(avg_grade, 95)

    def test_get_top_five_students(self):
        """Test retrieving the top five students based on average grades."""
        # Creating and enrolling multiple students, then submitting assignments with varying grades
        grades = [88, 92, 75, 60, 99, 82, 91, 100, 65, 73]  # Grades for ten students
        for grade in grades:
            self.create_student_and_enroll(grade)

        # Retrieving the top five students
        top_students = self.service.get_top_five_students(self.course_id)
        top_students_grades = [self.service.get_student_grade_avg(self.course_id, student_id) for student_id in top_students]

        # Asserting the top five students are correctly identified
        expected_top_grades = sorted(grades, reverse=True)[:5]
        self.assertEqual(sorted(top_students_grades, reverse=True), expected_top_grades)

if __name__ == '__main__':
    unittest.main()
