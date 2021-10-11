import random

from OOP_I.estudent.school import create_school_with_students
from OOP_I.estudent.student import Student


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
    school_len = len(school)
    print(school_len)

    # związane z __bool__ w klasie Student
    some_student = Student(first_name="Grzegorz", last_name="Zima")
    print(bool(some_student))
    some_student.promoted = True
    print(bool(some_student))
    # zastosowanie np. w if
    if some_student:
        print(f"Zadziałała funkcja bool, która dała wartość: {bool(some_student)}")


if __name__ == "__main__":
    run_example()
