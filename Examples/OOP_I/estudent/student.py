class Student:

    # Konstruktor zostanie wywołany podczas tworzenia obiektu
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = 63
        self.promoted = False

    def print_student(self):
        print(f"Student: {self.first_name} {self.last_name}, promoted: {self.promoted}")
