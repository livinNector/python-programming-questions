---
title: Data type operations
---

# Problem Statement

Implement the function data_type_operations(data: dict) -> dict that takes a dictionary containing keys 'int', 'float', 'list', and 'set'. Perform the following operations:

For 'int', add 5.
For 'float', multiply by 1.5.
For 'list', append the length of the list.
For 'set', add the square of the size of the set.
Return the modified dictionary.

**Example**
```
data = {
    'int': 10,
    'float': 4.0,
    'list': [1, 2, 3],
    'set': {1, 2}
}
Result: {
    'int': 15,
    'float': 6.0,
    'list': [1, 2, 3, 3],
    'set': {1, 2, 4}
}
```

# Solution

```py3 test.py -r 'python test.py'
<template>
def data_type_operations(data: dict) -> dict:
    '''
    Modify the input dictionary as per the operations specified.

    Arguments:
    data: dict - Dictionary containing specific keys and values.

    Returns:
    dict - Modified dictionary after performing operations.
    '''
    <los>...</los>
    <sol>
    data['int'] += 5
    data['float'] *= 1.5
    data['list'].append(len(data['list']))
    data['set'].add(len(data['set'])**2)
    return data
    </sol>

</template>
<suffix_invisible>
{% include '../function_type_and_modify_check_suffix.py.jinja' %}
</suffix_invisible>

```

# Public Test Cases

## Input 1

```
data = {
    'int': 3,
    'float': 2.0,
    'list': [10, 20],
    'set': {2}
}
is_equal(
    data_type_operations(data),
    {
        'int': 8,
        'float': 3.0,
        'list': [10, 20, 2],
        'set': {2, 1}
    }
)
```

## Output 1

```
{
    'int': 8,
    'float': 3.0,
    'list': [10, 20, 2],
    'set': {2, 1}
}
```

# Private Test Cases

## Input 1

```
data = {
    'int': 0,
    'float': 0.0,
    'list': [],
    'set': set()
}
is_equal(
    data_type_operations(data),
    {
        'int': 5,
        'float': 0.0,
        'list': [0],
        'set': {0}
    }
)

```

## Output 1

```
{
    'int': 5,
    'float': 0.0,
    'list': [0],
    'set': {0}
}

```

## Input 2

```
data = {
    'int': -5,
    'float': 10.0,
    'list': [1, 2, 3, 4],
    'set': {1, 3, 5}
}
is_equal(
    data_type_operations(data),
    {
        'int': 0,
        'float': 15.0,
        'list': [1, 2, 3, 4, 4],
        'set': {1, 3, 5, 9}
    }
)

```

## Output 2

```
{
    'int': 0,
    'float': 15.0,
    'list': [1, 2, 3, 4, 4],
    'set': {1, 3, 5, 9}
}


```
