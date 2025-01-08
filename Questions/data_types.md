---
title: Data Types- Perform Basic Operations
---

# Problem Statement

Write a function datatype_operations(a, b, c, lst) that performs the following operations:

Returns the sum of a and b if a and b are integers.
Returns the concatenation of c and the string " completed!" if c is a string.
Appends a to the list lst and returns the updated list.

**Example**
```py3
datatype_operations(10, 20, "Task", [1, 2, 3]) 
# Output: (30, 'Task completed!', [1, 2, 3, 10])
```

# Solution

```py3 test.py -r 'python test.py'
<prefix>
def datatype_operations(a: int, b: int, c: str, lst: list):
    """
    Perform operations based on the inputs' data types.
    
    Args:
    a: int
    b: int
    c: str
    lst: list

    Returns:
    tuple: A tuple containing the results of the operations.
    """  
</prefix>
<template>
    <sol>
    sum_result = a + b
    string_result = c + " completed!"
    updated_list = lst + [a]
    return (sum_result, string_result, updated_list)
    </sol>
</template>
<suffix_invisible>
{% include '../function_type_and_modify_check_suffix.py.jinja' %}
</suffix_invisible>
```

# Public Test Cases

## Input 1

```
datatype_operations(5, 7, "Done", [2, 4])
```

## Output 1

```
(12, 'Done completed!', [2, 4, 5])
```

## Input 2

```
datatype_operations(3, 9, "Test", [])
```

## Output 2

```
(12, 'Test completed!', [3])
```


# Private Test Cases

## Input 1

```
datatype_operations(-10, 10, "Example", [0])
datatype_operations(0, 100, "Practice", [4,8])
```

## Output 1

```
(0, 'Example completed!', [0, -10])
(100, 'Practice completed!', [4, 8, 0])
```