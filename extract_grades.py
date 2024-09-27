import numpy as np
from constants import QUIZ_DATA_CONVERT_MULTIPLIER


def extract_grades_hw_and_exams(hw_and_exams_data):
    # Extract exam grades
    exam_grades = [int(student['Exam']) for student in hw_and_exams_data]

    # Extract homework grades
    homework_grade_lists = []

    for row in hw_and_exams_data:
        # Extract homework grades and append them to the list
        homework_grades = [
            int(row['Homework 1']),
            int(row['Homework 2']),
            int(row['Homework 3'])
        ]
        homework_grade_lists.append(homework_grades)

    # Calculate averages for homeworks
    homework_grades = np.sum(homework_grade_lists, axis=1) / len(homework_grade_lists[0])

    return homework_grades, exam_grades

def extract_quiz_grades(quiz_data):
    return [
        int(int(student['Grade']) * QUIZ_DATA_CONVERT_MULTIPLIER) 
        for student in quiz_data]
