---
title: Password Strength Validator
tags: ['python', 'functions', 'strings', 'lists', 'type-check']
---
# Problem Statement
Write a function that evaluates the strength of a given password based on specific criteria.

The password must satisfy all the following conditions:
1. Password should have at least 8 characters
2. Password should contain at least one uppercase letter
3. Password should contain at least one lowercase letter
4. Password should contain atleast one digit
5. Password should contain at least one special character from: @#$%^&*

**Input Format:** A single string representing the password  
**Output Format:** A tuple containing (boolean, list) where:
- boolean indicates if the password meets all criteria (True/False)
- list contains feedback number for the unmet criteria (empty list if all criteria are met)

**Sample Input**
```
Hello123@
```
**Sample Output**
```
(True, [])
```
# Solution
```py test.py -r 'python3 test.py'
<prefix>
def check_password_strength(password: str) -> tuple:
    '''
    Evaluate password strength based on given criteria.
    Returns (True, []) if password is strong,
    (False, feedback) if criteria not met.
    '''
</prefix>
<template>
    feedback = []
    <sol>
    if len(password) < 8:
        feedback.append(1)
    
    if not any(c.isupper() for c in password):
        feedback.append(2)
    
    if not any(c.islower() for c in password):
        feedback.append(3)
    
    if not any(c.isdigit() for c in password):
        feedback.append(4)
    
    special_chars = "@#$%^&*"
    if not any(c in special_chars for c in password):
        feedback.append(5)
    
    if feedback:
        return (False, feedback)
    return (True, [])
    </sol>
    <los>pass</los>
</template>
<suffix>
password = input().strip()
result = check_password_strength(password)
print(result)
</suffix>
```
# Public Test Cases
## Input 1
```
Hello123@
```
## Output 1
```
(True, [])
```
## Input 2
```
hello123
```
## Output 2
```
(False, [2, 5])
```
## Input 3
```
Ab1@defgh
```
## Output 3
```
(True, [])
```

# Private Test Cases
## Input 1
```
Ab1
```
## Output 1
```
(False, [1, 5])
```
## Input 2
```
HELLO123@
```
## Output 2
```
(False, [3])
```
## Input 3
```
HelloWorld#1
```
## Output 3
```
(True, [])
```