---
title: Data Processing- Group by Key and Aggregate
---

# Problem Statement

Write a function group_and_sum(data) that takes a list of tuples data, where each tuple contains a category (string) and a value (int). The function should return a dictionary where the keys are the unique categories and the values are the sum of all values for that category.

**Example**
```py3
group_and_sum([("A", 10), ("B", 5), ("A", 7)])
# Output: {'A': 17, 'B': 5}
```

# Solution

```py3 test.py -r 'python test.py'
<prefix>
def group_and_sum(data: list):
    """
    Group by key and sum values.
    
    Args:
    data: list - List of tuples containing category and value.

    Returns:
    dict: A dictionary with summed values for each category.
    """   
</prefix>
<template>
    <sol>
    grouped = {}
    for category, value in data:
        if category in grouped:
            grouped[category] += value
        else:
            grouped[category] = value
    return grouped
    </sol>
</template>
<suffix_invisible>
{% include '../function_type_and_modify_check_suffix.py.jinja' %}
</suffix_invisible>
```

# Public Test Cases

## Input 1

```
group_and_sum([("X", 2), ("Y", 3), ("X", 4)])
```

## Output 1

```
{'X': 6, 'Y': 3}
```

## Input 2

```
group_and_sum([])
```

## Output 2

```
{}
```


# Private Test Cases

## Input 1

```
group_and_sum([("Cat", 1), ("Dog", 3), ("Cat", 2), ("Bird", 5)])
group_and_sum([("January", 200), ("February", 150), ("January", 250), ("March", 300)])
group_and_sum([("Electronics", 100), ("Furniture", 200), ("Electronics", 150), ("Clothing", 50)])
group_and_sum([("Alice", 8), ("Bob", 6), ("Alice", 7), ("Charlie", 9), ("Bob", 5)])
```

## Output 1

```
{'Cat': 3, 'Dog': 3, 'Bird': 5}
{'January': 450, 'February': 150, 'March': 300}
{'Electronics': 250, 'Furniture': 200, 'Clothing': 50}
{'Alice': 15, 'Bob': 11, 'Charlie': 9}
```