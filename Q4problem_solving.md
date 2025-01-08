---
title: Student Grade Management System
tags: ['python', 'functions', 'dictionary']
---

# Problem Statement
Design a simple grade management system for students with the following functionality:

1. **Add Student**: Add a new student with their `name` and initial `grade`.
2. **Update Grade**: Update a student's grade.
3. **Get Highest Grade**: Get the student with the highest grade.
4. **Get Student Info**: Get the grade of a specific student.


# Solution
```python test.py  -r 'python test.py'
<prefix>

</prefix>
<template>
class GradeManagementSystem:
    def __init__(self):
        # Initialize an empty dictionary to store student grades
        self.students = {}

    def add_student(self, name: str, grade: float) -> None:
        '''
        Adds a new student to the system with the given name and grade.
        
        Arguments:
        name: str - the name of the student.
        grade: float - the grade of the student.
        
        Returns:
        None
        '''
        self.students[name] = grade

    def update_grade(self, name: str, grade: float) -> None:
        '''
        Updates the grade of an existing student.
        
        Arguments:
        name: str - the name of the student whose grade will be updated.
        grade: float - the new grade to be assigned.
        
        Returns:
        None
        '''
        if name in self.students:
            self.students[name] = grade
        else:
            print(f"Student {name} not found.")

    def get_highest_grade(self) -> str:
        '''
        Returns the name of the student with the highest grade.
        
        Returns:
        str - the name of the student with the highest grade.
        '''
        if not self.students:
            return "No students available."
        highest_grade_student = max(self.students.items(), key=lambda x: x[1])[0]
        return highest_grade_student

    def get_student_info(self, name: str) -> float:
        '''
        Returns the grade of a specific student.
        
        Arguments:
        name: str - the name of the student.
        
        Returns:
        float - the grade of the student.
        '''
        return self.students.get(name, "Student not found")


</template>
<suffix>

</suffix>
<suffix_invisible>

</suffix_invisible>
```

# Public Test Cases

## Input 1

```
system = GradeManagementSystem()
system.add_student("Alice", 85.5)
system.add_student("Bob", 92.0)
system.update_grade("Alice", 90.0)
print(system.get_highest_grade())  # Output: Bob
```

## Output 1

```
Bob
```


## Input 2

```
system = GradeManagementSystem()
system.add_student("Charlie", 78.0)
system.add_student("Dave", 88.5)
system.update_grade("Charlie", 80.0)
print(system.get_student_info("Charlie"))  # Output: 80.0
```

## Output 2

```
80.0
```


## Input 3

```
system = GradeManagementSystem()
system.add_student("Eve", 75.0)
system.add_student("Frank", 65.5)
system.update_grade("Eve", 80.0)
system.update_grade("Frank", 85.0)
print(system.get_highest_grade())  # Output: Eve
```

## Output 3

```
Eve
```

# Private Test Cases

## Input 1

```
system = GradeManagementSystem()
system.add_student("Grace", 95.0)
system.add_student("Hank", 88.0)
system.update_grade("Grace", 96.0)
print(system.get_highest_grade())  # Output: Grace
```

## Output 1

```
Grace
```

## Input 2

```
system = GradeManagementSystem()
system.add_student("Ivy", 72.5)
system.add_student("Jack", 85.0)
system.update_grade("Ivy", 75.5)
print(system.get_student_info("Jack"))  # Output: 85.0
```

## Output 2

```
85.0
```

## Input 3

```
system = GradeManagementSystem()
system.add_student("Ken", 60.0)
system.add_student("Leo", 95.0)
system.update_grade("Ken", 70.0)
print(system.get_student_info("Ken"))  # Output: 70.0
```

## Output 3

```
70.0
```
