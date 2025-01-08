---
title: Data Processing I/O
---
# Problem Statement
Write a Python program that processes a list of student grades. The program should:

Take a list of student names and their respective grades in multiple subjects as input.
Compute and output:
The average grade for each student.
The highest grade for each student.
The lowest grade for each student.
**Sample Input**
```
3
Alice 85 90 92
Bob 78 88 82
Charlie 95 87 91
```
**Sample Output**
```
Name: Alice
Average Grade: 89.0
Highest Grade: 92
Lowest Grade: 85

Name: Bob
Average Grade: 82.67
Highest Grade: 88
Lowest Grade: 78

Name: Charlie
Average Grade: 91.0
Highest Grade: 95
Lowest Grade: 87
```
# Solution
```py test.py -r 'python3 test.py'
<template>
def process_studentgrades():
    """
    Processes student grades to compute the average, highest, and lowest grades
    for each student and outputs the results in a specific format.
    """
    # Read the number of students
    <sol>
    n = int(input())

    #Loop over the number of students
    for  in range(n):
        # Read each student's data (name and grades)
        data = input().split()

        #First part is the name, the rest are the grades
        name = data[0]
        grades = list(map(int, data[1:]))

        #Calculate average, highest, and lowest grades
        average = sum(grades) / len(grades)
        highest = max(grades)
        lowest = min(grades)
        </sol>

        #Print the results for each student
        print(f"Name: {name}")
        print(f"Average Grade: {average:.2f}")
        print(f"Highest Grade: {highest}")
        print(f"Lowest Grade: {lowest}")
        print()  # Blank line between students

#Call the function to start processing
process_student_grades()
</template>
```
# Public Test Cases
## Input 1
```
3
Alice 85 90 92
Bob 78 88 82
Charlie 95 87 91
```
## Output 1
```
Name: Alice
Average Grade: 89.0
Highest Grade: 92
Lowest Grade: 85

Name: Bob
Average Grade: 82.67
Highest Grade: 88
Lowest Grade: 78

Name: Charlie
Average Grade: 91.0
Highest Grade: 95
Lowest Grade: 87
```
## Input 2
```
2
John 70 80 90 85
Emily 95 88 92 100
```
## Output 2
```
Name: John
Average Grade: 81.25
Highest Grade: 90
Lowest Grade: 70

Name: Emily
Average Grade: 93.75
Highest Grade: 100
Lowest Grade: 88
```
## Input 3
```
1
Zara 50 60 70 80
```
## Output 3
```
Name: Zara
Average Grade: 65.0
Highest Grade: 80
Lowest Grade: 50
```

# Private Test Cases
## Input 1
```
Adam 50 60 70
Eve 60 65 70 75
Sam 100 90 95 85
Lily 95 85 100
```
## Output 1
```
Name: Adam
Average Grade: 60.0
Highest Grade: 70
Lowest Grade: 50

Name: Eve
Average Grade: 70.0
Highest Grade: 75
Lowest Grade: 60

Name: Sam
Average Grade: 92.5
Highest Grade: 100
Lowest Grade: 85

Name: Lily
Average Grade: 93.33
Highest Grade: 100
Lowest Grade: 85
```