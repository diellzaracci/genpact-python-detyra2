class Student:
    """Class Student(id, name)"""

    def __init__(self, student_id, name):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        self.id = student_id
        self.name = name

    def __str__(self):
        return f"Student {self.id}: {self.name}"


class Course:
    """Class Course(code, title)"""

    def __init__(self, code, title):
        if not code.strip() or not title.strip():
            raise ValueError("Code or title cannot be empty")
        self.code = code
        self.title = title

    def __str__(self):
        return f"Course {self.code}: {self.title}"


class Enrollment:
    """Class Enrollment(student_id, course_code, grades)"""

    def __init__(self, student_id, course_code, grades=None):
        self.student_id = student_id
        self.course_code = course_code
        self.grades = grades or []

    def add_grade(self, grade):
        if not (0 <= grade <= 100):
            raise ValueError("Grade must be between 0 and 100")
        self.grades.append(grade)

    def __str__(self):
        return f"Enrollment: Student {self.student_id} in {self.course_code} with grades {self.grades}"
