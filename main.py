import argparse
from gradebook.service import (
    add_student,
    add_course,
    enroll,
    add_grade,
    list_students,
    list_courses,
    list_enrollments,
    compute_average,
    compute_gpa
)

def main():
    parser = argparse.ArgumentParser(description="Gradebook CLI")
    subparsers = parser.add_subparsers(dest="command")

    parser_add_student = subparsers.add_parser("add-student")
    parser_add_student.add_argument("--name", required=True)

    parser_add_course = subparsers.add_parser("add-course")
    parser_add_course.add_argument("--code", required=True)
    parser_add_course.add_argument("--title", required=True)

    parser_enroll = subparsers.add_parser("enroll")
    parser_enroll.add_argument("--student-id", type=int, required=True)
    parser_enroll.add_argument("--course", required=True)
    parser_enroll.add_argument("--grade", type=int, nargs="+")  # opsionale me vendos note, nargs="+" me shtu multiple nota 

    parser_add_grade = subparsers.add_parser("add-grade")
    parser_add_grade.add_argument("--student-id", type=int, required=True)
    parser_add_grade.add_argument("--course", required=True)
    parser_add_grade.add_argument("--grade", type=int, nargs="+", required=True)

    parser_list = subparsers.add_parser("list")
    parser_list.add_argument("entity", choices=["students", "courses", "enrollments"])
    parser_list.add_argument("--sort", choices=["name", "code"], default=None)

    parser_avg = subparsers.add_parser("avg")
    parser_avg.add_argument("--student-id", type=int, required=True)
    parser_avg.add_argument("--course", required=True)

    parser_gpa = subparsers.add_parser("gpa")
    parser_gpa.add_argument("--student-id", type=int, required=True)

    args = parser.parse_args()

    try:
        if args.command == "add-student":
            student_id = add_student(args.name)
            print(f"Added student {args.name} with ID {student_id}")

        elif args.command == "add-course":
            add_course(args.code, args.title)
            print(f"Added course {args.code}: {args.title}")

        elif args.command == "enroll":
            enroll(args.student_id, args.course)
            print(f"Student {args.student_id} enrolled in {args.course}")
            if args.grade is not None:
                for g in args.grade:
                    add_grade(args.student_id, args.course, g)
                print(f"Added grades {args.grade} for student {args.student_id} in {args.course}")

        elif args.command == "add-grade":
            for g in args.grade:
                add_grade(args.student_id, args.course, g)
            print(f"Added grades {args.grade} for student {args.student_id} in {args.course}")

        elif args.command == "list":
            if args.entity == "students":
                students = list_students()
                for s in sorted(students, key=lambda x: x["name"].lower() if args.sort=="name" else x["id"]): # .lower() per me i sortu alfabetikisht
                    print(s)
            elif args.entity == "courses":
                courses = list_courses()
                for c in sorted(courses, key=lambda x: x["code"].lower() if args.sort=="code" else x["title"]):
                    print(c)
            elif args.entity == "enrollments":
                enrollments = list_enrollments()
                for e in enrollments:
                    print(e)

        elif args.command == "avg":
            avg = compute_average(args.student_id, args.course)
            print(f"Average for student {args.student_id} in {args.course}: {avg:.2f}")

        elif args.command == "gpa":
            gpa = compute_gpa(args.student_id)
            print(f"GPA for student {args.student_id}: {gpa:.2f}")

        else:
            parser.print_help()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()