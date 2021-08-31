from students_data import students, find_student_by_name


def calculate_final_grade(all_grades):
    avg = sum(all_grades) / len(all_grades)
    final_grade = int(avg + 0.5)
    return final_grade


