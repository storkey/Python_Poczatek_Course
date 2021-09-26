import random


class Student:

    # Konstrukt zostanie wywołany podczas tworzenia obiektu
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = 63
        self.promoted = False


class Grade:
    pass


class School:

    # Konstruktor może zawierać również obiekty
    def __init__(self, name, students):
        self.name = name
        self.students = students


# Obiekty możemy przekazywać jako argumenty do funkcji
def print_student(student):
    print(f"Student: {student.first_name} {student.last_name}, promoted: {student.promoted}")


# W funkcji możemy zmodyfikować stan obiektu (side effect)
def promote_student(student):
    student.promoted = True


# Funkcja może tworzyć i zwracać nowe obiekty
def create_school_with_students(school_name):
    number_of_students = random.randint(1, 20)  # zakres od 1 do 20 włącznie
    students = []
    for student_number in range(number_of_students): # licząc od zera
        first_name = f"Student--{student_number}"
        last_name = "Smith"
        students.append(Student(first_name, last_name))

    school = School(school_name, students)
    return school


def run_example():
    student = Student(first_name="Jan", last_name="Kowalski")

    print(student.first_name)
    print(student.last_name)
    print(student.age)

    print_student(student)
    promote_student(student)
    print_student(student)

    # my_grade = Grade()
    # primary_school = School()
    #
    # print(student)
    # print(my_grade)
    # print(primary_school)
    #
    # print("Type of student_piotr object:", type(student))
    # print("Type of my_grade object:", type(my_grade))
    # print("Type of primary_school object:", type(primary_school))


if __name__ == "__main__":
    run_example()
