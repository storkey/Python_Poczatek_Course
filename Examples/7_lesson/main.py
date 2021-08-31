from school.students_data import is_student_in_school

print("Witaj w elektronicznym dzienniku!")

student_name = input("Podaj imię ucznia, żeby dowiedzieć się czy zdał do następnej klasy: ")

if not is_student_in_school(student_name):
    print(f"Niestety, {student_name} nie ma na liście...")
    