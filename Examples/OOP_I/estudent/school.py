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

    def promote_lucky_students(self):
        for index, student in enumerate(self.students):
            if index % 3 == 0:
                student.promote()
