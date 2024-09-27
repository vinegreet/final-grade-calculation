import os
import pandas as pd

# Create a directory to store the CSV files if it doesn't exist
output_dir = 'calculated_final_grades'
os.makedirs(output_dir, exist_ok=True)

def generate_output(students, grades_total):
    # Create a DataFrame for students
    students_df = pd.DataFrame(students)
    students_sorted_by_net_id = students_df.sort_values(by='NetID')

    students_sorted_by_net_id['Final Grades'] = grades_total

    students_sorted_by_grades = students_sorted_by_net_id.sort_values(by='Final Grades', ascending=False)

    # Group the DataFrame by Group
    students_grouped = students_sorted_by_grades.groupby('Group')

    # Generate resulting sheets
    for group_number, group_df in students_grouped:
        # Drop unneeded columns
        group_df_cleaned = group_df.drop(columns=['NetID', 'Group'])

        # Create a CSV file path
        csv_filename = os.path.join(output_dir, f'group_{group_number}.csv')
        
        # Save the group's DataFrame to the CSV file
        group_df_cleaned.to_csv(csv_filename, index=False)

    # Create a dict of students, grouped by their groups
    # students_grouped_dict = students_grouped.apply(lambda student: student.to_dict('records')).to_dict()
