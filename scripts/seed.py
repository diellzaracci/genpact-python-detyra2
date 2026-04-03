from gradebook.storage import save_data
from gradebook.service import add_student, add_course, enroll, add_grade

# Reset data
data = {"students": [], "courses": [], "enrollments": []}
save_data(data)

# Add students
s1 = add_student("Diellza")
s2 = add_student("Ili")
s3 = add_student("Dion")

# Add courses
add_course("DS", "Data Science")
add_course("ML", "Machine Learning")

# Enroll students
enroll(s1, "DS")
enroll(s1, "ML")
enroll(s2, "ML")
enroll(s3, "DS")

# Add grades
add_grade(s1, "ML", 99)
add_grade(s1, "DS", 88)
add_grade(s3, "DS", 82)
add_grade(s2, "ML", 70)

print("Sample data seeded successfully!")
