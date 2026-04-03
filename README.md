# Gradebook CLI

## Overview
A Python command-line application to manage students, courses, enrollments, and grades.

## Features
- Add students
- Add courses
- Enroll students to courses
- Add grades
- Compute student averages and GPA
- List students, courses, and enrollments

## Setup
1. Clone the repo: git clone https://github.com/diellzaracci/genpact-python-detyra2.git
2. Create a virtual environment: python -m venv venv
3. Activate it:
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`
4. Install dependencies (if any): pip install -r requirements.txt

## Usage
### Seed sample data
>  python -m scripts.seed
### CLI commands
- To add a new student:
  >  python main.py add-student --name "StudentName"
- To add a new course:
  >  python main.py add-course --code ML --title "Machine Learning"
- To enroll a student to a course:
  >  python main.py enroll --student-id 1 --course ML --grade 95
- To list students:
  >  python main.py list students --sort name
- To list courses:
  >  python main.py list courses --sort code
- To list enrollments:
  >  python main.py list enrollments
- To calculate course average of student:
  >  python main.py avg --student-id 1 --course ML
- To calculate GPA of student:
  >  python main.py gpa --student-id 1


## Design Decisions & Limitations
- Chose JSON for data storage to keep persistence simple and human-readable.
- Grades must be integers 0-100.
- GPA is the mean of course averages per student.
- No advanced authentication or multi-user handling.
