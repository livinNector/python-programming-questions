---
title: Find the Student with the Highest Grade
---

# Problem Statement

Given a list of student names and their grades, find the name of the student with the highest grade. If multiple students have the same highest grade, return the lexicographically smallest name among them.

**Input Format:**  
A semicolon-separated list of student name-grade pairs in the format `name,grade`. Each pair is separated by a semicolon.  

**Output Format:**  
The name of the student with the highest grade.

**Sample Input**
```
Alice,85;Bob,92;Charlie,92;David,88
```

**Sample Output**
```
Bob
```

**Explanation**  

The highest grade is 92, and the students with this grade are Bob and Charlie. Among them, "Bob" is lexicographically smaller.

# Solution
```py test.py -r 'python3 test.py' 
<prefix>
def highest_grade_student(data: str) -> str:
    '''
    Return the name of the student with the highest grade.
    '''
</prefix>
<template>
    students = [tuple(item.split(',')) for item in data.split(';')]
    max_grade = max(int(grade) for _, grade in students)
    top_students = [name for name, grade in students if int(grade) == max_grade]
    return <sol>min(top_students)</sol><los>...</los>
</template>
<suffix>
data = input().strip()
print(highest_grade_student(data))
</suffix>
```

# Public Test Cases

## Input 1

```
Alice,85;Bob,92;Charlie,92;David,88
```

## Output 1 

```
Bob
```

## Input 2

```
Emma,75;Liam,90;Olivia,90;Sophia,90
```

## Output 2 

```
Liam
```

## Input 3

```
John,50;Jane,75;Doe,75;Adam,40
```

## Output 3 

```
Doe
```

# Private Test Cases

## Input 1

```
Michael,80;Sarah,95;Alex,95;Zara,85
```

## Output 1

```
Alex
```

## Input 2

```
Aaron,100;Zoe,100;Clara,99
```

## Output 2

```
Aaron
```

## Input 3

```
Isabella,0
```

## Output 3

```
Isabella
```
