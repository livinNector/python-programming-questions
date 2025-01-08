---
title: Data Processing I/O
tags: [mapping, filtering, aggregation, sorting, grouping, I/O]
---

# Problem Statement

You need to implement the following functions. These functions should read inputs from stdin and write the output to stdout in the specified format.

1. **`sum_even_numbers(d)`**
    - Description: Given a list of numbers, sum all the even numbers and print the result to stdout.
    - Input: A list of integers `d`.
    - Output: Print the sum of all even numbers in the list.
    - Example:
    ```python
    sum_even_numbers([1, 2, 3, 4, 5])  # Output: 6
    sum_even_numbers([10, 21, 34, 50])  # Output: 94
    ```

2. **`filter_greater_than_threshold(d, threshold)`**
    - Description: Given a list of numbers and a threshold, filter out the numbers greater than or equal to the threshold and print them to stdout.
    - Input: A list of integers `d` and an integer `threshold`.
    - Output: Print the filtered list.
    - Example:
    ```python
    filter_greater_than_threshold([1, 2, 3, 4, 5], 3)  # Output: [3, 4, 5]
    filter_greater_than_threshold([10, 20, 30], 15)  # Output: [20, 30]
    ```

3. **`sort_and_print(d)`**
    - Description: Given a list of strings, sort them alphabetically and print the sorted list to stdout.
    - Input: A list of strings `d`.
    - Output: Print the sorted list.
    - Example:
    ```python
    sort_and_print(["banana", "apple", "cherry"])  # Output: ['apple', 'banana', 'cherry']
    sort_and_print(["mango", "kiwi", "apple"])  # Output: ['apple', 'kiwi', 'mango']
    ```

4. **`group_by_category(d)`**
    - Description: Given a list of tuples (category, item), group the items by category and print the grouped dictionary to stdout.
    - Input: A list of tuples `d`, where each tuple contains a category and an item.
    - Output: Print the dictionary with categories as keys and lists of items as values.
    - Example:
    ```python
    group_by_category([("fruit", "apple"), ("fruit", "banana"), ("veg", "carrot")])  
    # Output: {'fruit': ['apple', 'banana'], 'veg': ['carrot']}

    group_by_category([("animal", "cat"), ("animal", "dog"), ("bird", "sparrow")]) 
    # Output: {'animal': ['cat', 'dog'], 'bird': ['sparrow']}
    ```

# Solution

```py3 test.py -r 'python test.py'
<template>
def sum_even_numbers(d: list) -> int:
    '''Given a list of numbers, sums all even numbers and prints the result.'''

    <los>...</los>
    <sol>
    even_numbers = filter(lambda x: x % 2 == 0, d)
    result = sum(even_numbers)
    return(result)</sol>

def filter_greater_than_threshold(d: list, threshold: int) -> list:
    '''Filters out the numbers greater than or equal to the threshold and prints them.'''

    <los>...</los>
    <sol>
    filtered_numbers = filter(lambda x: x >= threshold, d)
    return(list(filtered_numbers))</sol>

def sort_and_print(d: list) -> list:
    '''Sorts the list of strings alphabetically and prints it.'''

    <los>...</los>
    <sol>
    sorted_list = sorted(d)
    return(sorted_list)</sol>

def group_by_category(d: list) -> dict:
    '''Groups items by category and prints the resulting dictionary.'''

    <los>...</los>
    <sol>
    result = {}
    for category, item in d:
        if category not in result:
            result[category] = []
        result[category].append(item)
    return(result)</sol>
</template>
<suffix>

</suffix>
<suffix_invisible>
{% include '../function_type_and_modify_check_suffix.py.jinja' %}
</suffix_invisible>
```

# Public Test Cases

## Input 1
```

d = [1, 2, 3, 4, 5]
is_equal(
    sum_even_numbers(d),
    6
)

d = [1, 2, 3, 4, 5]
threshold = 3
is_equal(
    filter_greater_than_threshold(d, threshold),
    [3, 4, 5]
)

d = ['apple', 'banana', 'cherry']
is_equal(
    sort_and_print(d),
    ['apple', 'banana', 'cherry']
)

d = [("fruit", "apple"), ("fruit", "banana"), ("veg", "carrot")]
is_equal(
    group_by_category(d),
    {'fruit': ['apple', 'banana'], 'veg': ['carrot']}
)

```

## Output 1

```
6
[3, 4, 5]
['apple', 'banana', 'cherry']
{'fruit': ['apple', 'banana'], 'veg': ['carrot']}

```

## Input 2

```
d = [10, 21, 34, 50]
is_equal(
    sum_even_numbers(d),
    94
)

d = [5, 6, 7, 8]
threshold = 6
is_equal(
    filter_greater_than_threshold(d, threshold),
    [6, 7, 8]
)

d = ['mango', 'kiwi', 'apple']
is_equal(
    sort_and_print(d),
    ['apple', 'kiwi', 'mango']
)

d = [("animal", "cat"), ("animal", "dog"), ("bird", "sparrow")]
is_equal(
    group_by_category(d),
    {'animal': ['cat', 'dog'], 'bird': ['sparrow']}
)

```

## Output 2

```
94
[6, 7, 8]
['apple', 'kiwi', 'mango']
{'animal': ['cat', 'dog'], 'bird': ['sparrow']}

```

# Private Test Cases


## Input 1

```

d = [12, 14, 16, 18]
is_equal(
    sum_even_numbers(d),
    60
)

d = [30, 40, 50]
threshold = 35
is_equal(
    filter_greater_than_threshold(d, threshold),
    [40, 50]
)

d = ['zebra', 'elephant', 'tiger']
is_equal(
    sort_and_print(d),
    ['elephant', 'tiger', 'zebra']
)

d = [("fruit", "mango"), ("veg", "carrot"), ("fruit", "apple")]
is_equal(
    group_by_category(d),
    {'fruit': ['mango', 'apple'], 'veg': ['carrot']}
)

```

## Output 1

```
60
[40, 50]
['elephant', 'tiger', 'zebra']
{'fruit': ['mango', 'apple'], 'veg': ['carrot']}

```

