---
title: Top Student
---

# Problem Statement

Implement the function top_student(students: list) -> dict that takes a list of dictionaries where each dictionary contains 'name' and 'marks' of a student. Return a dictionary with the following keys:

- 'average': the average marks rounded to 2 decimal places.
- 'topper': the name of the student with the highest marks.

*Example*

students = [
    {"name": "lucky", "marks": 85},
    {"name": "Rocky", "marks": 92},
    {"name": "Chocky", "marks": 78}
]
top_student(students) # Output: {"average": 85.0, "topper": "Rocky"}


# Solution

py3 test.py -r 'python test.py'
<template>
def top_student(students: list) -> dict:
    '''
    Find the average marks and the student with the highest marks.
    Arguments:
    students: list - a list of dictionaries containing 'name' and 'marks'.
    Return: dict - a dictionary with 'average' and 'topper'.
    '''
    <los>...</los>
    <sol>
    average = round(sum(s['marks'] for s in students) / len(students), 2)
    topper = max(students, key=lambda x: x['marks'])['name']
    return {'average': average, 'topper': topper}  </sol>

</template>
<suffix_invisible>
{% include '../function_type_and_modify_check_suffix.py.jinja' %}
</suffix_invisible>


# Public Test Cases

## Input 1


students = [
    {"name": "Johny", "marks": 70},
    {"name": "Dony", "marks": 90},
    {"name": "Smithy", "marks": 80}
]
is_equal(
    top_student(students),
    {"average": 80.0, "topper": "Dony"}
)


## Output 1


{"average": 80.0, "topper": "Dony"}


# Private Test Cases

## Input 1


students = [
    {"name": "Ammu", "marks": 88},
    {"name": "Evuram", "marks": 92}
]
is_equal(
    top_student(students),
    {"average": 90.0, "topper": "Evuram"}
)


## Output 1


{"average": 90.0, "topper": "Evuram"}


## Input 2


students = [
    {"name": "Manvendra", "marks": 70},
    {"name": "Lokendra", "marks": 86}
]
is_equal(
    top_student(students),
    {"average": 78.0, "topper": "Lokendra"}
)


## Output 2


{"average": 78.0, "topper": "lokendra"}
