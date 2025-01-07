---
title: Implement a basic calculator with multiple operations
---

# Problem Statement

Implement a basic calculator with the following operations:

1. `add(a, b)` – Adds two numbers and returns the result.
2. `subtract(a, b)` – Subtracts `b` from `a` and returns the result.
3. `multiply(a, b)` – Multiplies two numbers and returns the result.
4. `divide(a, b)` – Divides `a` by `b` and returns the result. If `b` is zero, return `"Cannot divide by zero"`.

Your task is to implement these four functions. The driver code will call these functions with different inputs.

**Example**
```
add(3, 5) # 8
subtract(10, 3) # 7
multiply(4, 6) # 24
divide(9, 3) # 3.0
divide(9, 0) # "Cannot divide by zero"
```

# Solution
```py3 test.py -r 'python test.py'
<prefix>
# some prefix   
</prefix>
<template>
def add(a: int, b: int) -> int:
    '''
    Add two numbers.

    Arguments:
    a: int - the first number.
    b: int - the second number.

    Return: int - the result of a + b.
    '''
    <los>...</los>
    <sol>return a + b</sol>
    
def subtract(a: int, b: int) -> int:
    '''
    Subtract two numbers.

    Arguments:
    a: int - the first number.
    b: int - the second number.

    Return: int - the result of a - b.
    '''
    <los>...</los>
    <sol>return a - b</sol>

def multiply(a: int, b: int) -> int:
    '''
    Multiply two numbers.

    Arguments:
    a: int - the first number.
    b: int - the second number.

    Return: int - the result of a * b.
    '''
    <los>...</los>
    <sol>return a * b</sol>

def divide(a: int, b: int) -> float:
    '''
    Divide two numbers.

    Arguments:
    a: int - the numerator.
    b: int - the denominator.

    Return: float - the result of a / b if b != 0, else returns "Cannot divide by zero".
    '''
    <los>...</los>
    <sol>return a / b if b != 0 else "Cannot divide by zero"</sol>
    
test = <los>...</los><sol>'test'</sol> #tests
</template>
<suffix>
# some suffix
</suffix>
<suffix_invisible>
{% include './function_type_and_modify_check_suffix.py.jinja' %}
</suffix_invisible>
```

# Public Test Cases

## Input 1
```
is_equal(
    add(3, 5),
    8
)
```

## Output 1
```
8
```

## Input 2
```
is_equal(
    subtract(10, 3),
    7
)
```

## Output 2
```
7
```

## Input 3
```
is_equal(
    multiply(4, 6),
    24
)
```

## Output 3
```
24
```

## Input 4
```
is_equal(
    divide(9, 3),
    3.0
)
```

## Output 4
```
3.0
```

# Private Test Cases

## Input
```
is_equal(
    divide(9, 0),
    "Cannot divide by zero"
)

is_equal(
    divide(9, 0),
    "Cannot divide by zero"
)

is_equal(
    subtract(100, 50),
    50
)

is_equal(
    multiply(0, 100),
    0
)
```

## Output
```
"Cannot divide by zero"
0
50
0
```
