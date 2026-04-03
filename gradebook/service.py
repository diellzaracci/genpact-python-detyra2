from gradebook.models import Student, Course, Enrollment
from gradebook.storage import load_data, save_data

def add_student(name):
    """Add a new student and return their ID"""
    data = load_data()
    new_id = max([s["id"] for s in data["students"]], default=0)+1  # id e re
    
    student_obj = Student(new_id, name)     # me kriju objekt per mi validu & strukturu t'dhanat

    student = {"id": student_obj.id, "name": student_obj.name}
    data["students"].append(student)
    save_data(data)
    return new_id

def add_course(code, title):
    """Add a new course with code and title"""
    data = load_data()
    if any(c["code"]==code for c in data["courses"]):       # me check nese vecse ekziston qaj kod
        raise ValueError(f"Course {code} already exists")
    
    course_obj = Course(code, title)

    course = {"code": course_obj.code, "title": course_obj.title}
    data["courses"].append(course)
    save_data(data)

def enroll(student_id, course_code):
    """Add a new enrollment of a student in a course"""
    data = load_data()
    if not any(s["id"] == student_id for s in data["students"]):    # validation per a ekziston qaj student
        raise ValueError(f"No student with id {student_id}")
    if not any(c["code"]==course_code for c in data["courses"]):    # validation per a ekziston qajo lande
        raise ValueError(f"No course with code {course_code}")
    if any(e["student_id"]==student_id and e["course_code"]==course_code for e in data["enrollments"]):     # me kqyr nese vecse osht studenti i regjistrum n qat lande
        raise ValueError(f"Student {student_id} already enrolled in {course_code}")
    
    enrollment_obj = Enrollment(student_id, course_code)

    enrollment = {"student_id": enrollment_obj.student_id, "course_code":enrollment_obj.course_code, "grades": enrollment_obj.grades}
    data["enrollments"].append(enrollment)
    save_data(data)

def add_grade(student_id, course_code, grade):
    """Add grades to enrollments"""
    data = load_data()
    if not (0 <= grade <= 100):
        raise ValueError("Grade must be 0-100")
    for e in data["enrollments"]:
        if e["student_id"]==student_id and e["course_code"]==course_code:
            enrollment_obj = Enrollment(e["student_id"], e["course_code"], e.get("grades", []))
            enrollment_obj.add_grade(grade)

            e["grades"] = enrollment_obj.grades
            save_data(data)
            return
    raise ValueError("Enrollment not found")
    
def list_students():
    """List students alphabetically"""
    data = load_data()
    return sorted(data["students"], key=lambda s: s["name"].lower())   # me sort alfabetik pa dallim uppercase/lowercase - case-insensitive

def list_courses():
    """List courses alphabetically"""
    data = load_data()
    return sorted(data["courses"], key=lambda c: c["code"].lower())   # me sort alfabetik

def list_enrollments():
    """List enrollments alphabetically"""
    data = load_data()
    return data["enrollments"]

def compute_average(student_id, course_code):
    """Compute average grade in a course for a student"""
    data = load_data()
    for e in data["enrollments"]:
        if e["student_id"] ==student_id and e["course_code"]==course_code:
            grades=e.get("grades",[])
            if grades:
                return sum(grades) / len(grades)
            return 0
    raise ValueError("Enrollment not found")

def compute_gpa(student_id):
    """Compute GPA of student"""
    data = load_data()
    course_averages =[]
    for e in data["enrollments"]:
        if e["student_id"]==student_id:
            grades = e.get("grades", [])
            if grades:
                course_averages.append(sum(grades)/len(grades))
    if course_averages:
        return sum(course_averages)/len(course_averages)
    return 0