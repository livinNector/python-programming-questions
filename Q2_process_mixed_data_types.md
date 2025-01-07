---
title: Process Mixed Data Types
---

# Problem Statement

Write a function process_data(data: dict) -> dict that takes a dictionary with the following keys and performs the described operations:
'int': Add 15 to the integer value.
'float': Multiply the float value by 1.5.
'str': Convert the string to uppercase.
'list': Reverse the list.
'set': Add the number 100 to the set.
'dict': Add a new key-value pair 'hello': 'haha'.

**Example**
```py3
data = {
    'int': 5,
    'float': 2.5,
    'str': 'hello',
    'list': [1, 2, 3],
    'set': {1, 2, 3},
    'dict': {'a': 1, 'b': 2}
}
process_data(data)
# Output:
{
    'int': 20,
    'float': 3.75,
    'str': 'HELLO',
    'list': [3, 2, 1],
    'set': {1, 2, 3, 100},
    'dict': {'a': 1, 'b': 2, 'hello': 'haha'}
}

```

# Solution

```py3 test.py -r 'python test.py'
<prefix>
# some prefix   
</prefix>
<template>
def process_data(data: dict) -> dict:
    '''
    Perform operations on mixed data types within a dictionary.

    Arguments:
    data: dict - a dictionary containing keys: 'int', 'float', 'str', 'list', 'set', and 'dict'.

    Return:
    dict - the updated dictionary after processing.
    '''
    <los>...</los>
    <sol>
    data['int'] += 15
    data['float'] *= 1.5
    data['str'] = data['str'].upper()
    data['list'] = data['list'][::-1]
    data['set'].add(100)
    data['dict']['hello'] = 'haha'
    return data
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
data = {
    'int': 10,
    'float': 4.0,
    'str': 'python',
    'list': [5, 6, 7],
    'set': {8, 9},
    'dict': {'x': 1}
}
is_equal(
    process_data(data),
    {
        'int': 25,
        'float': 6.0,
        'str': 'PYTHON',
        'list': [7, 6, 5],
        'set': {8, 9, 100},
        'dict': {'x': 1, 'hello': 'haha'}
    }
)

```

## Output 1

```
   {
        'int': 25,
        'float': 6.0,
        'str': 'PYTHON',
        'list': [7, 6, 5],
        'set': {8, 9, 100},
        'dict': {'x': 1, 'hello': 'haha'}
    }
```

## Input 2

```
data = {
    'int': 0,
    'float': 1.0,
    'str': 'test',
    'list': [],
    'set': set(),
    'dict': {}
}
is_equal(
    process_data(data),
    {
        'int': 15,
        'float': 1.5,
        'str': 'TEST',
        'list': [],
        'set': {100},
        'dict': {'hello': 'haha'}
    }
)

```

## Output 2

```
   {
        'int': 15,
        'float': 1.5,
        'str': 'TEST',
        'list': [],
        'set': {100},
        'dict': {'hello': 'haha'}
    }
```

# Private Test Cases

## Input 1

```
data = {
    'int': -5,
    'float': 0.0,
    'str': 'abcd',
    'list': [1],
    'set': {42},
    'dict': {'k1': 'v1'}
}
is_equal(
    process_data(data),
    {
        'int': 10,
        'float': 0.0,
        'str': 'ABCD',
        'list': [1],
        'set': {42, 100},
        'dict': {'k1': 'v1', 'hello': 'haha'}
    }
)

```

## Output 1

```
   {
        'int': 10,
        'float': 0.0,
        'str': 'ABCD',
        'list': [1],
        'set': {42, 100},
        'dict': {'k1': 'v1', 'hello': 'haha'}
    }
```
