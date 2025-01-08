---
title: Problem-Solving- Employee Data Analysis
---

# Problem Statement

Write the following functions for analyzing employee data:

average_salary(data) - Given a list of dictionaries, calculate the average salary.
department_count(data) - Return a dictionary with the number of employees in each

**Example**
```py3
employees = [
    {"name": "Alice", "department": "HR", "salary": 50000},
    {"name": "Bob", "department": "IT", "salary": 70000},
    {"name": "Charlie", "department": "IT", "salary": 60000},
]

average_salary(employees) 
# Output: 60000.0

department_count(employees) 
# Output: {'HR': 1, 'IT': 2}
```

# Solution
```python test.py -r 'python test.py'
<template>
<sol>
def average_salary(data: list):
    total_salary = sum(emp['salary'] for emp in data)
    return total_salary / len(data) if data else 0

def department_count(data: list):
    counter = {}
    for emp in data:
        if emp['department'] in counter:
            counter[emp['department']] += 1
        else:
            counter[emp['department']] = 1
    return counter
</sol>
</template>
<suffix>
employees = input_employees()
print(average_salary(employees))
print(department_count(employees))
</suffix>
<suffix_invisible>
def input_employees():
    # Prompt the user for the input in the form of a list of dictionaries
    employees_input = input("Enter the list of employees as a list of dictionaries: ")
    
    # Use eval() to convert the input string into a list of dictionaries
    try:
        employees = eval(employees_input)
        
        # Validate that the input is a list of dictionaries
        if isinstance(employees, list) and all(isinstance(emp, dict) for emp in employees):
            return employees
        else:
            print("Invalid format: The input must be a list of dictionaries.")
            return []
    except Exception as e:
        print(f"Invalid input! Error: {e}")
        return []
</suffix_invisible>
```

# Public Test Cases

## Input 1
```
employees = [
    {"name": "Alice", "department": "HR", "salary": 50000},
    {"name": "Bob", "department": "IT", "salary": 70000},
]
```

## Output 1
```
60000.0
{'HR': 1, 'IT': 1}
```


# Private Test Cases


## Input 1
```
employees = [
    {"name": "Alice", "department": "HR", "salary": 50000},
    {"name": "Bob", "department": "IT", "salary": 70000},
    {"name": "Charlie", "department": "Finance", "salary": 85000},
    {"name": "Diana", "department": "HR", "salary": 55000},
    {"name": "Eve", "department": "Finance", "salary": 75000},
]
```

## Output 1
```
67000.0
{'HR': 2, 'IT': 1, 'Finance': 2}
```

## Input 2
```
employees = []
```

## Output 2
```
0
{}
```

## Input 3
```
employees = [
    {"name": "Alice", "department": "HR", "salary": 0},
    {"name": "Bob", "department": "IT", "salary": -5000},
    {"name": "Charlie", "department": "Finance", "salary": 30000},
    {"name": "Diana", "department": "IT", "salary": 20000},
]
```

## Output 3
```
11250.0
{'HR': 1, 'IT': 2, 'Finance': 1}
```

## Input 4
```
employees = [
    {"name": "Alice", "department": "HR and Admin", "salary": 60000},
    {"name": "Bob", "department": "Finance/Accounts", "salary": 75000},
    {"name": "Charlie", "department": "HR and Admin", "salary": 65000},
    {"name": "Diana", "department": "IT", "salary": 70000},
    {"name": "Eve", "department": "Finance/Accounts", "salary": 80000},
]
```

## Output 4
```
70000.0
{'HR and Admin': 2, 'Finance/Accounts': 2, 'IT': 1}
```

## Input 5
```
employees = [
    {"name": "Alice", "department": "HR", "salary": 100000},
    {"name": "Bob", "department": "IT", "salary": 20000},
    {"name": "Charlie", "department": "Finance", "salary": 30000},
    {"name": "Diana", "department": "IT", "salary": 25000},
    {"name": "Eve", "department": "Finance", "salary": 50000},
    {"name": "Frank", "department": "HR", "salary": 90000},
]
```

## Output 5
```
52500.0
{'HR': 2, 'IT': 2, 'Finance': 2}
```