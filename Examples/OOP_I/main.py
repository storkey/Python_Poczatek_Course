from OOP_I.estudent.school import create_school_with_students, School
from OOP_I.estudent.student import Student


# Ponowny side effect
def assign_student_to_school(school, student):
    school.students.append(student)


def run_example():
    school = create_school_with_students("Eton")
    school_without_students = School("Empty school")
    john_doe = Student("John", 'Doe')
    assign_student_to_school(school_without_students, john_doe)
    for student in school_without_students.students:
        student.print_student()
    print(school)
    for student in school.students:
        student.print_student()


if __name__ == "__main__":
    run_example()
