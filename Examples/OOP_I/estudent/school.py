import random

from OOP_I.estudent.student import Student


class School:

    # Konstruktor może zawierać również obiekty
    # nie musi "wprost przypiwyać przekazanych wartości, może wykonywać swoją logikę
    def __init__(self, name, students=None):
        self.name = name
        # if len(students) > 10:
        # students = students[:10]
        if students is None:
            students = []
        self.students = students
        # z konstruktora możemy wywoływać inne funkcje
        self.promote_lucky_students()

    def __str__(self):
        students = ""
        for student in self.students:
            students += "\n"
            students += str(student)

        return f"School: {self.name}, with {len(self.students)} students: {students}"

    def promote_lucky_students(self):
        for index, student in enumerate(self.students):
            if index % 3 == 0:
                student.promote()


# Funkcja może tworzyć i zwracać nowe obiekty
def create_school_with_students(school_name):
    number_of_students = random.randint(1, 20)  # zakres od 1 do 20 włącznie
    students = []
    for student_number in range(number_of_students):  # licząc od zera
        first_name = f"Student--{student_number}"
        last_name = "Smith"
        students.append(Student(first_name, last_name))

    school = School(school_name, students)
    return school
