import unittest
from gradebook.storage import save_data
from gradebook.service import add_student, add_grade, add_course, enroll, compute_average, compute_gpa

class TestService(unittest.TestCase):
    
    def setUp(self):
        # reset data before each test
        self.test_data = {
            "students": [],
            "courses": [],
            "enrollments": []
        }
        save_data(self.test_data)

    def test_add_students(self):
        student_id = add_student("TestStudent")
        self.assertEqual(student_id, 1)

    def test_add_grade_and_average(self):
        # setup
        student_id = add_student("TestStudent")
        add_course("CS", "Computer Science")
        enroll(student_id, "CS")

        # add grades
        add_grade(student_id, "CS", 80)
        add_grade(student_id, "CS", 100)

        avg = compute_average(student_id, "CS")
        self.assertEqual(avg, 90)

    def test_add_grade_invalid(self):
        student_id = add_student("TestStudent")
        add_course("CS", "Computer Science")
        enroll(student_id, "CS")

        # invalid grade
        with self.assertRaises(ValueError):
            add_grade(student_id, "CS", 200)

    def test_gpa_computation(self):
        student_id = add_student("StudentGPA")
        add_course("MATH", "Mathematics")
        add_course("CS", "Computer Science")
        enroll(student_id, "MATH")
        enroll(student_id, "CS")

        add_grade(student_id, "MATH", 100)
        add_grade(student_id, "CS", 80)

        gpa = compute_gpa(student_id)
        self.assertEqual(gpa, 90)  # average of 100 and 80

if __name__ == "__main__":
    unittest.main()