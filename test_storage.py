from gradebook.storage import load_data, save_data

data = load_data()

new_student = {"id":1, "name":"Diellzaaa"}
data["students"].append(new_student)
save_data(data)

new_course = {"code":"DS", "title":"Data Science"}
data["courses"].append(new_course)
save_data(data)

new_enrollment = {"student_id":1, "course_code":"DS"}
data["enrollments"].append(new_enrollment)
save_data(data)

print(data)