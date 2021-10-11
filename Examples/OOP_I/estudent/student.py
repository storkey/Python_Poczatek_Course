class Student:

    # Konstruktor zostanie wywołany podczas tworzenia obiektu
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False
        self.final_grades = []

    def __repr__(self):
        return f"<Student first_name= {self.first_name}, last_name = {self.last_name}, promoted = {self.promoted}, " \
               f"final_grades = {self.final_grades}>"

    # Nie print! Musi zwracać stringa
    # Służy do obsługi funkcji wbudowanej str
    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}, promoted: {self.promoted} " \
               f"Final grades: {self.final_grades}"

    def promote(self):
        self.promoted = True

    def add_final_grade(self, grade):
        self.final_grades.append(grade)
        if grade == 1:
            self.promoted = False
