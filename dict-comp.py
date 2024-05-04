"""
practice dictionary comprehension
"""
from random import randint
names = ['John', 'Samantha', 'Edina', 'Alex', 'Bob', 'David', 'Norbert', 'Peter', 'William', 'Joseph']
# new_dict = {new_key:new_value for item in iterable if test}

student_scores = {name: randint(1, 100) for name in names}
print(student_scores)

# passing_students = {student: student_scores[student] for student in student_scores if student_scores[student] >= 60}
# ^^^^^ it works, but it's not as correct as it could be

# more correct syntax: {new_key:new_value for (key, value) in dictionary.items() if test}
# .items() is used to create tuples that can be checked and are assigned to the vars key & value

passing_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(passing_students)

sentence = 'What is the average air speed velocity of an unladen swallow?'
word_count_dict = {word:len(word) for word in sentence.split()}
print(word_count_dict)

# temp conversion using dict comprehension
cel_temps = {
    'Monday' : 15,
    'Tuesday' : 14,
    'Wednesday' : 19,
    'Thursday' : 32,
    'Friday': 5,
    'Saturday' : 7,
    'Sunday' : 12
}


def celsius_to_fahrenheit(temp_input):
    return temp_input * 9 / 5 + 32


fahrenheit_temps = {day: celsius_to_fahrenheit(temp) for (day, temp) in cel_temps.items()}
print(fahrenheit_temps)
