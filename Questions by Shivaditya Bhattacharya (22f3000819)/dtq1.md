---
title: Playing with Data Types
tags: [datatypes, int, float, str, list, dictionary]
---

# Problem Statement
You are given the following:

1. First name and last name of a person in lower-case. Make only the first character of each upper-case and contatenate them to make the full name.

2. The person's monthly salary and performance bonus percentage. Calculate the bonus amount and total salary for the month.

3. A comma-seperated string of the person's projects. Find the number of projects he's worked on without using a loop.

Return a dictionary of the format:
{
&emsp;"full_name": str,
&emsp;"bonus": float,
&emsp;"salary_after_bonus": float,
&emsp;"number_of_projects": int,
&emsp;"projects": list,
}

# Solution
```python test.py -r 'python test.py'
<prefix>
# some prefix   
</prefix>
<template>
def employee_records(first_name: str, last_name: str, salary: int, bonus_percent: float, projects: str) -> dict:
    '''
    Write a function employee_records(first_name, last_name, salary, bonus_percent, projects). Capitalise the first character of first name and last name and contatenate to get full name, calculate bonus amount and total salary after bonus and create list of projects and count number of projects without using a loop.

    Arguments:
    first_name: str
    last_name: str
    salary: int
    bonus_percent: float
    projects: str

    Return: a dictionary in the form {
                    "full_name": str,
                    "bonus": float,
                    "salary_after_bonus": float,
                    "number_of_projects": int,
                    "projects": list,
                }
    '''
    
    <los>...</los>
    <sol>
    return {
        "full_name": first_name[0].upper() + first_name[1:] + ' ' + last_name[0].upper() + last_name[1:],
        "bonus": salary*bonus_percent/100,
        "salary_after_bonus": salary + salary*bonus_percent/100,
        "number_of_projects": len(projects.split(',')),
        "projects": projects.split(','),
    }
    </sol>
    test = <los>...</los><sol>'test'</sol> #tests
</template>
<suffix>
# some suffix
</suffix>
<suffix_invisible>
{% include '../function_type_and_modify_check_suffix.py.jinja' %}
</suffix_invisible>
```

# Public Test Cases

## Input 1
```
first_name = 'vineet'
last_name = 'solanki'
salary = 45000
bonus_percent = 8.356
projects = "DigiCop,eSuraksha,KaviSammelan"
```

## Output 1
```
{'full_name': 'Vineet Solanki', 'bonus': 3760.2, 'salary_after_bonus': 48760.2, 'number_of_projects': 3, 'projects': ['DigiCop', 'eSuraksha', 'KaviSammelan']}
```


# Private Test Cases


## Input 1
```
first_name = 'ayushi'
last_name = 'saha'
salary = 72758
bonus_percent = 9
projects = "NLP-ChatBot,ClientHelp"
```

## Output 1
```
{'full_name': 'Ayushi Saha', 'bonus': 6548.22, 'salary_after_bonus': 79306.22, 'number_of_projects': 2, 'projects': ['NLP-ChatBot', 'ClientHelp']}
```