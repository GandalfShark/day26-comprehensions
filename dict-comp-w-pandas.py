"""
practice iterating trough dataframes
with dictionary comprehension and pandas
"""
import pandas as pd

student_scores = {
    'student': ['Johnny', 'Samantha', 'Fredrico', 'Alex', 'Amira', 'David', 'Norbert', 'Jasdeep', 'William'],
    'score': [36, 98, 68, 79, 91, 27, 87, 99, 20]
}

student_df = pd.DataFrame(student_scores)

# looping through a dataframe rows
for (index, rows) in student_df.iterrows():
    print(rows.student)
