import json
import csv
import numpy as np

from constants import HW_MULTIPLIER, QUIZ_MULTIPLIER, EXAM_MULTIPLIER
from generate_output import generate_output
from helpers import sort_by_SID
from extract_grades import extract_grades_hw_and_exams, extract_quiz_grades

QUIZ_QUANTITY = 2

### Parsing data

with open('./../data-grades/Students.json', 'r') as students_json:
    students = json.loads(json.load(students_json))

with open('./../data-grades/Homework and exams.csv', 'r') as hw_and_exams_csv_data:
    hw_and_exams_data = list(csv.DictReader(hw_and_exams_csv_data))

with open('./../data-grades/quiz_1_grades.csv', 'r') as quiz_1_csv_data:
    quiz_1_data = list(csv.DictReader(quiz_1_csv_data))

with open('./../data-grades/quiz_2_grades.csv', 'r') as quiz_2_csv_data:
    quiz_2_data = list(csv.DictReader(quiz_2_csv_data))


### Homeworks and exams grades

hw_and_exams_data_sorted_by_SID = sort_by_SID(hw_and_exams_data)

homework_grade_lists, exam_grades = extract_grades_hw_and_exams(hw_and_exams_data_sorted_by_SID)

### Quizzes grades

quiz_1_data_sorted_by_SID = sort_by_SID(quiz_1_data)
quiz_2_data_sorted_by_SID = sort_by_SID(quiz_2_data)

quiz_1_grades = np.array(extract_quiz_grades(quiz_1_data_sorted_by_SID)) / QUIZ_QUANTITY
quiz_2_grades = np.array(extract_quiz_grades(quiz_2_data_sorted_by_SID)) / QUIZ_QUANTITY

### Calculating total grades with applying multipliers

homework_grades = np.sum(homework_grade_lists, axis=1) / len(homework_grade_lists[0])
homeworks_total = homework_grades * HW_MULTIPLIER

exams_total = np.array(exam_grades) * EXAM_MULTIPLIER

quizzes_total = quiz_1_grades * QUIZ_MULTIPLIER + quiz_2_grades * QUIZ_MULTIPLIER


### Calculating total grades

grades_total_floats = quizzes_total + exams_total + homeworks_total
grades_total = grades_total_floats.astype(int)

### Generating the output

generate_output(students, grades_total)

# print(grades_total)
