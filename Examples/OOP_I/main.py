import random

from OOP_I.estudent.school import create_school_with_students


def run_example():
    school = create_school_with_students("Hogwart")
    print(30 * "*")
    for student in school.students:
        print(student)
    print(30 * "*")

    for student in school.students:
        student.promote()
    print("=" * 20)

    for student in school.students:
        final_grade = random.randint(1, 3)
        student.add_final_grade(final_grade)
    print(school)

    repr_first_student = repr(school.students[0])
    print("\n")
    print(repr_first_student)

    print(repr(school))
    school_as_number = int(school)
    print(school_as_number)


if __name__ == "__main__":
    run_example()
