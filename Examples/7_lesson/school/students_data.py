students = [
    {
        "name": "Piotr",
        "subjects_results": [
            {
                "subject": "matematyka",
                "grades": [2, 3, 4, 5, 2, 3.5]
            },
            {
                "subject": "historia",
                "grades": [5, 5, 5, 5, 4, 5]
            },
            {
                "subject": "fizyka",
                "grades": [3, 3, 2, 3, 4, 3]
            }
        ]
    },
    {
        "name": "Joanna",
        "subjects_results": [
            {
                "subject": "matematyka",
                "grades": [4, 3, 4, 5, 3, 4]
            },
            {
                "subject": "historia",
                "grades": [4, 4, 3, 2, 2, 3]
            },
            {
                "subject": "fizyka",
                "grades": [3.5, 4, 5, 4, 4, 4.5]
            }
        ]
    }
]


def find_student_by_name(name):
    for student in students:
        if student["name"] == name:
            return student


def is_student_in_school(name):
    if not find_student_by_name(name):
        return False
    return True
