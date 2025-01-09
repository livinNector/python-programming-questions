---
title: "Remedial Classes: List of Students with Scores Below 50 and Gender-Wise Count"
---

# Problem Statement

You are given a 2D list `scores` where each inner list represents a student's data in the following format:
[Name, Gender, Mathematics, Physics, Chemistry]

Write a function `find_remedial_students` that takes the `scores` list as input and:
1. Returns a list of names of students who have scored below 50 in any subject.
2. Returns a tuple with the gender-wise count of remedial students and total students in the format:

(remedial_males/total_males, remedial_females/total_females)

**Example**
```python
scores = [ ["John", "M", 55, 40, 60], ["Alice", "F", 70, 80, 90], ["Bob", "M", 30, 60, 50], ["Emma", "F", 40, 45, 55] ] find_remedial_students(scores)

# Output: (['John', 'Bob', 'Emma'], (2/2, 1/2))

```
In this example:
- The list of remedial students is `['John', 'Bob', 'Emma']`.
- There are 2 male students in total, and 2 of them are in remedial.
- There are 2 female students in total, and 1 of them is in remedial.

# Solution

```py3 test.py -r 'python test.py'
<template>
def find_remedial_students(scores: list) -> tuple:
    '''
    Identify students with scores below 50 and return their names along with gender-wise count.

    Arguments:
    scores: list - A 2D list where each inner list contains:
                    [Name, Gender, Mathematics, Physics, Chemistry]

    Return: tuple - (List of names of remedial students, 
                     (remedial_males/total_males, remedial_females/total_females))
    '''
    <sol>
    remedial_students = []
    total_males = 0
    total_females = 0
    remedial_males = 0
    remedial_females = 0

    for student in scores:
        name, gender, math, physics, chemistry = student
        if math < 50 or physics < 50 or chemistry < 50:
            remedial_students.append(name)
            if gender == "M":
                remedial_males += 1
            elif gender == "F":
                remedial_females += 1
        
        if gender == "M":
            total_males += 1
        elif gender == "F":
            total_females += 1

    return (remedial_students, 
            (f"{remedial_males}/{total_males}", f"{remedial_females}/{total_females}"))
    </sol>
</template>
<suffix_invisible>
{% include '../function_type_and_modify_check_suffix.py.jinja' %}
</suffix_invisible>
```

# Public Test Cases

## Input 1

```
scores = [    ["Alex", "M", 45, 55, 65],
    ["Sophia", "F", 75, 80, 90],
    ["Chris", "M", 40, 60, 50],
    ["Olivia", "F", 30, 45, 55]
]
is_equal(
    find_remedial_students(scores),
    (['Alex', 'Chris', 'Olivia'], ('2/2', '1/2'))
)


```

## Output 1

```
(['Alex', 'Chris', 'Olivia'], ('2/2', '1/2'))

```


## Input 2

```
scores = [    ["Michael", "M", 70, 80, 90],
    ["Sarah", "F", 65, 70, 60]
]
is_equal(
    find_remedial_students(scores),
    ([], ('0/1', '0/1'))
)

```

## Output 2

```
([], ('0/1', '0/1'))

```


# Private Test Cases

## Input 1

```
scores = [    ["David", "M", 50, 50, 49],
    ["Emily", "F", 55, 45, 60],
    ["James", "M", 30, 30, 30],
    ["Lily", "F", 20, 70, 70],
    ["Mark", "M", 70, 80, 90],
    ["Anna", "F", 60, 90, 100],
    ["Steve", "M", 49, 49, 49],
    ["Nina", "F", 45, 30, 55],
    ["Tom", "M", 80, 70, 60],
    ["Jane", "F", 65, 75, 85]
]
is_equal(
    find_remedial_students(scores),
    (['David', 'Emily', 'James', 'Lily', 'Steve', 'Nina'], 
     ('4/5', '2/5'))
)

```

## Output 1

```
(['David', 'Emily', 'James', 'Lily', 'Steve', 'Nina'], ('4/5', '2/5'))

```
