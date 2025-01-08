---
title: Process Student Grades
tags: ["data processing", "sorting", "Python"]
---

# Problem Statement

Write a function `process_student_grades` that takes a list of tuples as input. Each tuple contains a student's name (string) and their grade (integer). The data is incomplete, as each student gets additional bonus marks of 5, capping the total marks to 100.

The function should return the name of the student with the highest grade after applying the bonus. If there is a tie, return the alphabetically smallest name among the highest scorers.

---

# Solution

```python test.py  -r 'python3 test.py'
<prefix>

</prefix>
<template>
def process_student_grades(student_data):
   '''
   Given the students data in form of a tuple:
   - Adds 5 bonus marks to each grade, capping at 100.
   - Sort to find the highest grade
   - Make sure to return alphabetically smallest name interms of a tie.

   Arguments:
   student_data: list of tuples - (name (str), grade (int))

   Return:
   str - student with the highest grade
   '''
   <los>...</los>
   <sol>
   # Generate the data, after bonus is added
   after_bonus_data = list(map(lambda x: (x[0], min(x[1] + 5, 100)), student_data))
   # Sort with both the parameters at the same time
   sorted_list_short = sorted(after_bonus_data, key=lambda x: (-x[1], x[0]))
   return sorted_list_short[0][0]
</sol>
</template>
<suffix>
input_data = input().strip()
student_data = eval(input_data)
result = process_student_grades(student_data)
print(result)
</suffix>
<suffix_invisible>
</suffix_invisible>
```

---

# Public Test Cases

## Input 1

```
[("Alice", 85), ("Bob", 92), ("Charlie", 92), ("David", 88)]
```

## Output 1

```
Bob
```

## Input 2

```
[("Eve", 90), ("Frank", 87), ("Grace", 90), ("Heidi", 85)]
```

## Output 2

```
Eve
```

---

# Private Test Cases

## Input 1

```
[("Anna", 99), ("Bella", 98), ("Cara", 97)]
```

## Output 1

```
Anna
```

## Input 2

```
[("Zack", 88), ("Yasmin", 88), ("Xander", 88)]
```

## Output 2

```
Xander
```

## Input 3

```
[("Maya", 75), ("Noah", 70), ("Olivia", 80), ("Liam", 85)]
```

## Output 3

```
Liam
```

## Input 4

```
[("Ivy", 95), ("Jack", 95), ("Hannah", 95)]
```

## Output 4

```
Hannah
```
