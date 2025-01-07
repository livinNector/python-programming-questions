## Problem Statement

You are given the number of student `n` and their names along with their marks. Write a program to process them and print the following:
1. The total number of students.
2. The names of student who scored more than 50, sorted alphabetically.
3. The average marks of all students.

The **Input** will be in the following format:
- The first line contains an integer `n` (1 ≤ n ≤ 1000), which represents the number of students.
- Each of the next `n` lines contains a student's name and marks (separated by a space).

**Output Format:**
- Print total number of students.
- Print the list of names of students who scored above 50, sorted alphabetically.
- Print the average marks of all students, rounded to two decimal places.

*(If in doubt about output format, refer to the test cases.)*

## Solution 
```python
n = int(input())    # Number of students
students = []
total_marks = 0

for i in range(n):
    name, marks = input().split()   # Input name and marks
    marks = int(marks)
    students.append((name, marks))
    total_marks += marks
    
stud_above_50 = []
for x in students:
    if x[1] > 50:
        stud_above_50.append(x[0])
stud_above_50.sort()
avg_marks = total_marks/n

print(f"Total students: {n}")
print(f"Students who scored above 50: {stud_above_50}")
print(f"Average marks: {avg_marks:.2f}")
```

## Public Test Cases

### Test Case 1:
**Input:**
```
5
John 60
Alice 40
Bob 80
Charlie 55
David 45
```
**Expected Output:**
```
Total Students: 5
Students who scored above 50: ['Bob', 'Charlie', 'John']
Average marks: 56.00
```

### Test Case 2:
**Input:**
```
3
Eve 30
Frank 60
Grace 90
```
**Expected Output:**
```
Total students: 3
Students who scored above 50: ['Frank', 'Grace']
Average marks: 60.00
```

## Private Test Cases

### Test Case 1:
**Input:**
```
4
Adam 45
Ben 55
Cathy 65
Diana 75
```
**Expected Output:**
```
Total students: 4
Students who scored above 50: ['Ben', 'Cathy', 'Diana']
Average marks: 60.00
```

### Test Case 2:
**Input:**
```
6
Liam 60
Nina 80
Ivy 100
Jack 95
Maya 55
Oscar 50
```
**Expected Output:**
```
Total students: 6
Students who scored above 50: ['Ivy', 'Jack', 'Liam', 'Maya', 'Nina']
Average marks: 73.33
```

### Test Case 3:
**Input:**
```
2
Olivia 20
Paul 45
```
**Expected Output:**
```
Total students: 2
Students who scored above 50: []
Average marks: 32.50
```

### Test Case 4:
**Input:**
```
7
Fiona 85
Diana 60
Aaron 80
Ethan 45
Charlie 40
George 70
Bella 55
```
**Expected Output:**
```
Total students: 7
Students who scored above 50: ['Aaron', 'Bella', 'Diana', 'Fiona', 'George']
Average marks: 62.14
```
