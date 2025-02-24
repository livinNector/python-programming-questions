---
title: Find Repeated Elements
tags: ['set', 'filtering','lambda','data-processing']
---

# Problem Statement

Given a list of any type, return a set containing elements **which are repeated**. (case, type sensistive ==)

**Example:**
```python
input list -> [1, 2, 3, '2', 3, 3, 4,'A','b','B','A'] #here 3,'A' have repetitions
output list -> {3, 'A'}
```
**Refrain from for/while loops. Use functional programming like lambda/mapping etc...**

# Solution

```python test.py  -r 'python test.py'
<template>
def find_repeated_elements(data: list) -> list:
    '''
    Find elements that are repeated in the input list.
    Argument:
    - data: List of items

    Return:
    - A set of repeated elements (order does not matter)
    '''
    <los>return ...</los>
    <sol>
    return set(filter(lambda x: data.count(x) > 1, set(data)))
    </sol>
</template>
<suffix_invisible>
{% include '../is_equal_loops_modify_check_suffix.py.jinja' %}
</suffix_invisible>
```

# Public Test Cases

## Input 1

```
if not check_for_loops(find_repeated_elements):
    is_equal(
        (find_repeated_elements([1, 2, 3, 2, 4, 5, 3, 6, 1])),
        ({1, 2, 3})
        )
```

## Output 1

```
{1, 2, 3}
```

## Input 2

```
if not check_for_loops(find_repeated_elements):
    is_equal(
        find_repeated_elements(['apple', 'banana', 'apple', 'cherry', 'banana']),
        {'apple', 'banana'}
        )        
```
## Output 2

```
{'apple', 'banana'}
```

## Input 3

```
if not check_for_loops(find_repeated_elements):
    is_equal(
        find_repeated_elements([10, 20, 30, 40]),
        set()
        )
```

## Output 3

```
{}
```

# Private Test Cases

## Input 1

```
if not check_for_loops(find_repeated_elements):
    is_equal(
        find_repeated_elements([7, 7, 7, 7, 7]),
        {7}
        )
    is_equal(
        find_repeated_elements([1, 2, 'apple', 2, 'banana', 'apple', 'bAnana']),
        {2, 'apple'}
        )
    is_equal(
        find_repeated_elements([]),
        set()
        )
```

## Output 1

```
{7}
{'apple', 2}
{}
```
