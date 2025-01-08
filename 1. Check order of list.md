---
title: Check order of list
---

# Problem Statement

Given a list `l` of string elements where len(l) <= 2, return `Ascending` if the first element of the
list comes before the second element in case-insensitive alphabetical order, and `Descending` otherwise.

**Example**
```py3
check_order(["apple", "banana"]) # Output: "Ascending"
check_order(["banana", "apple"]) # Output: "Descending"
check_order(["mango"]) # Output: "Descending"
```

# Solution

```py3 test.py -r 'python test.py'
<prefix>
# some prefix   
</prefix>
<template>
def check_order(l: list) -> str:
    '''
    Given a list, check if it is in ascending or descending order.

    Arguments:
    l: list - list of string elements to check.

    Return: str - Ascending if the first element comes before the second element in case-insensitive alphabetical order, else Descending.
    '''
    <los>...</los>
    <sol>
    if len(l) < 2:
        return "Descending"
    return "Ascending" if l[0].lower() < l[1].lower() else "Descending"
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
is_equal(
    check_order(["apple", "banana"]),
    "Ascending"
)
```

## Output 1

```
"Ascending"
```

## Input 2

```
is_equal(
    check_order(["BANANA", "APPLE"]),
    "Descending"
)
```

## Output 2

```
"Descending"
```

## Input 3 

```
is_equal(
    check_order(["orange", "grape"]),
    "Descending"
)
```

## Output 3

```
"Descending"
```

# Private Test Cases

## Input 1

```
l = ["Pineapple"]
is_equal(
    check_order(l),
    "Descending"
)
l = ["Apple", "Banana"]
is_equal(
    check_order(l),
    "Ascending"
)
l = ["mango", "mango"]
is_equal(
    check_order(l),
    "Descending"
)
l = ["orange", "grape"]
is_equal(
    check_order(l),
    "Descending"
)
```

## Output 1

```
"Descending"
"Ascending"
"Descending"
"Descending"
```
