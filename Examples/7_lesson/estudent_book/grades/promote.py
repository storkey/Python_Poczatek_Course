from estudent_book.grades import promotion_status

FAILED_GRADE = 1


def check_promotion(subjects_final_grades):
    for grade in subjects_final_grades.values():
        if grade == FAILED_GRADE:
            return promotion_status.FAILED

    return promotion_status.PASSED
