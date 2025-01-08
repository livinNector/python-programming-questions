---
title: Process Student Marks
tags: ['data processing', 'student marks', ]
---

# Problem Statement
Write a function `process_student_marks` that processes student marks and performs the following operations:

1. Read the number of students (`n`) and their respective names and marks.
2. Compute the average mark (rounded to 2 decimal places).
3. Determine the student(s) with the highest mark.
4. Print the results:
   - Each student's name and mark, sorted alphabetically by name.
   - The average mark.
   - The names of the top-performing students (alphabetically sorted in case of a tie).

### Input
The first line contains an integer `n`, the number of students.  
The next `n` lines each contain a student's name and mark, separated by a space.

### Output
The output should include:
1. Each student's name and mark in alphabetical order.
2. The average mark (rounded to 2 decimal places).
3. The names of the top-performing students.

# Solution
```python test.py -r 'python test.py'
<prefix>
def process_student_marks(n: int) -> str:
    '''
    Process student marks and generate results based on the given rules.
    
    Arguments:
    n: int - Number of students.
    
    Returns:
    str - Formatted string with student details, average mark, and top performers.
    '''
</prefix>
<template>
    <sol>
    # Initialize dictionary to store student marks
    student_marks = {}
    # Read input and store marks
    for _ in range(n):
        name, mark = input().split()
        mark = float(mark)
        student_marks[name] = mark
    # Compute average
    average = round(sum(student_marks.values()) / n, 2)
    # Find top performers
    highest_mark = max(student_marks.values())
    top_performers = sorted([name for name, mark in student_marks.items() if mark == highest_mark])
    # Prepare result
    result = []
    for name in sorted(student_marks.keys()):
        result.append(f"{name}: {student_marks[name]:.2f}")
    result.append(f"average: {average:.2f}")
    result.append(f"top_performers: {', '.join(top_performers)}")
    return "\n".join(result)
    </sol>
    <los>pass</los>
</template>
<suffix>
n = int(input())
print(process_student_marks(n))
</suffix>
<suffix_invisible>

</suffix_invisible>
```
# Public Test Cases

## Input 1

```
3
Alice 85
Bob 90
Charlie 85
```

## Output 1

```
Alice: 85.00
Bob: 90.00
Charlie: 85.00
average: 86.67
top_performers: Bob
```


## Input 2

```
4
Daisy 78
Ella 95
Fiona 95
George 88
```

## Output 2

```
Daisy: 78.00
Ella: 95.00
Fiona: 95.00
George: 88.00
average: 89.00
top_performers: Ella, Fiona

```


## Input 3

```
2
Hank 75
Ivy 85
```

## Output 3

```
Hank: 75.00
Ivy: 85.00
average: 80.00
top_performers: Ivy
```


# Private Test Cases

## Input 1

```
5
John 60
Jane 95
Jack 60
Jill 80
Jerry 95
```

## Output 1

```
Jack: 60.00
Jane: 95.00
Jerry: 95.00
Jill: 80.00
John: 60.00
average: 78.00
top_performers: Jane, Jerry
```

## Input 2

```
3
Kim 70
Liam 85
Mia 85
```

## Output 2

```
Kim: 70.00
Liam: 85.00
Mia: 85.00
average: 80.00
top_performers: Liam, Mia
```

## Input 3

```
4
Nancy 90
Oscar 85
Paul 85
Quincy 90
```

## Output 3

```
Nancy: 90.00
Oscar: 85.00
Paul: 85.00
Quincy: 90.00
average: 87.50
top_performers: Nancy, Quincy
```
