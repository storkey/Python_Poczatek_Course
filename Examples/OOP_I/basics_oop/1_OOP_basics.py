class Student:

    # Konstrukt zostanie wywołany podczas tworzenia obiektu
    def __init__(self):
        self.first_name = "Jan"
        self.last_name = "Piotrowski"
        self.age = 63


class Grade:
    pass


class School:
    pass


def run_example():
    student_jan = Student()
    my_grade = Grade()
    primary_school = School()

    print(student_jan)
    print(my_grade)
    print(primary_school)

    print("Type of student_piotr object:", type(student_jan))
    print("Type of my_grade object:", type(my_grade))
    print("Type of primary_school object:", type(primary_school))


if __name__ == "__main__":
    run_example()
