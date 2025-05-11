from constants import HW_QUANTITY, QUIZ_DATA_CONVERT_MULTIPLIER


def extract_grades_hw_and_exams(hw_and_exams_data):
    # Calculate averages for homework grades
    homework_grades = [
        int((int(row['Homework 1']) + int(row['Homework 2']) + int(row['Homework 3'])) / HW_QUANTITY)
        for row in hw_and_exams_data]

    # Extract exam grades
    exam_grades = [int(student['Exam']) for student in hw_and_exams_data]

    return homework_grades, exam_grades

def extract_quiz_grades(quiz_data):
    return [
        int(int(student['Grade']) * QUIZ_DATA_CONVERT_MULTIPLIER) 
        for student in quiz_data]
