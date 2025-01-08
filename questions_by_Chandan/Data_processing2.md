---
title: Basic Data Processing
tags: [mapping, filter aggragation, sorting, grouping, Basic Data Processing]
---

# Problem Statement

---

You need to implement the following functions:

1. **square_numbers(d)**
    - Description: Given a list 'd' of numbers, returns a new list with each number squared.
    - Example:
    
    ```python
    square_numbers([1,2,3,4,5]) # Output: [1,4,9,16,25]
    square_numbers([-1,0,-3,5,2]) # Output: [1,0,9,25,4]
    ```


2. **filter_aggregation(d, k)**
    - Description: Given a list 'd' of numbers and threshold, returns the sum of numbers greater than or equal to the given threshold.
    - Example:
    
    ```python
    filter_even_numbers([3,6,10,23,16], 10) # Output: 49
    filter_even_numbers([1,2,3,45,6], 6) # Output: 51
    ```

3. **`sort_strings(d)`**
    - Description: Given a list 'd' of strings, return a new list with strings sorted alphabetically.
    - Example:
    ```python
    sort_strings(['Rohan', 'Sohan', 'Bharath']) # Output: ['Bharath', 'Rohan', 'Sohan']
    sorti_strings(['Elizabeth', 'Sudharshini', 'Nanditha']) # Output: ['Elizabeth', Nanditha', Sudharshini']
    ```

4. **group_by_key(d)**
    - Description: Given a list 'd' of tuples(key, value), returns a dictionary where keys map to list of values.
    - Example:
    
    ```python
    group_by_key([("fruit", "apple"), ("fruit", "banana"), ("veg", "carrot")]) # Output: {'fruit': ['apple', 'banana'], 'veg':['carrort']}
    group_by_key([("electronics", "smartphone"),("clothing", "t-shirt"),("electronics", "laptop"),("clothing", "jeans"),("grocery", "milk")])  
    # Output : {'electronics':['smartphone', 'laptop'], 'clothing': ['t-shirt', 'jean'], 'grocery':['milk']}
    ```

# Solution
```py3 test.py -r 'python test.py'
<template>
def square_numbers(d:list)->list:
    '''
    Given a list 'd' of numbers, returns a new list with each number squared.

    Argument:
    d: a list of numbers

    Return:
    list: A new list with each number squared
    '''

    <los>...</los>
    <sol>
    return list(map(lambda x: x ** 2, d))</sol>

def filter_aggregation(d:list, threshold:int)->int:
    '''Given a list 'd' of numbers and threshold, returns the sum of numbers greater than or equal to the given threshold.

    Argument:
    d: a list of numbers
    threshold: a threshold value

    Return:
    int: Sum of all such numbers whihc are greater than or equal to the threshold value
    '''

    <los>...</los>
    <sol>
    filtered_data = filter(lambda x: x >= threshold, d)
    # Aggregate (sum) the filtered data
    result = sum(filtered_data)
    return result</sol>

def sort_strings(d:list)->list:
    '''
    Given a list 'd' of strings, return a new list with strings sorted alphabetically.

    Argument:
    d: a list of strings
    
    Return:
    list: a new list of strings sorted alphabetically 
    '''

    <los>...</los>
    <sol>
    return sorted(d)</sol>

def group_by_key(d:list)->dict:
    '''
    Given a list 'd' of tuples(key, value), returns a dictionary where keys map to list of values.

    Argument:
    d: a list of tuples(key, value)

    Return:
    dict: a dictionary where keys map to list of values
    '''

    <los>...</los>
    <sol>
    result = {}
    for key, value in d:
        if key not in result:
            result[key] = []  # Manually initialize the list
        result[key].append(value)
    return result</sol>
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
d = [1,2,3,4]
is_equal(
    square_numbers(d), 
    [1,4,9,16]
)

d = [23, 14, 7, 8, 5]
threshold = 8
is_equal(
    filter_aggregation(d, threshold),
    45
)

d = ['Bharath', 'Kavya', 'Sudharshini', 'David']
is_equal(
    sort_strings(d),
    ['Bharath', 'David', 'Kavya', 'Sudharshini']
)

d = [("fruit", "apple"), ("fruit", "banana"), ("veg", "carrot")]
is_equal(
    group_by_key(d),
    {'fruit':['apple', 'banana'], 'veg':['carrot']}
)
```
## Output 1
```
[1, 4, 9, 16]
45
['Bharath', 'David', 'Kavya', 'Sudharshini']
{'fruit': ['apple', 'banana'], 'veg': ['carrot']}
```
## Input 2

```
d = [5, 6, 7, 8]
is_equal(
    square_numbers(d),
    [25, 36, 49, 64]
)

d = [12, 5, 9, 7, 3]
threshold = 9
is_equal(
    filter_aggregation(d, threshold),
    21
)

d = ['Zara', 'Alex', 'Chandan', 'Meera']
is_equal(
    sort_strings(d),
    ['Alex', 'Chandan', 'Meera', 'Zara']
)

d = [("animal", "cat"), ("animal", "dog"), ("bird", "parrot")]
is_equal(
    group_by_key(d),
    {'animal': ['cat', 'dog'], 'bird': ['parrot']}
)
```
## Output 2
```
[25, 36, 49, 64]
21
['Alex', 'Chandan', 'Meera', 'Zara']
{'animal': ['cat', 'dog'], 'bird': ['parrot']}
```

## Input 3
```
d = [10, 11, 12, 13]
is_equal(
    square_numbers(d),
    [100, 121, 144, 169]
)

d = [18, 15, 7, 3, 2]
threshold = 10
is_equal(
    filter_aggregation(d, threshold),
    33
)

d = ['Ananya', 'Vikas', 'Sameer', 'Esha']
is_equal(
    sort_strings(d),
    ['Ananya', 'Esha', 'Sameer', 'Vikas']
)

d = [("color", "red"), ("color", "blue"), ("shape", "circle")]
is_equal(
    group_by_key(d),
    {'color': ['red', 'blue'], 'shape': ['circle']}
)
```
## Output 3

```
[100, 121, 144, 169]
33
['Ananya', 'Esha', 'Sameer', 'Vikas']
{'color': ['red', 'blue'], 'shape': ['circle']}
```

# Private Test Cases

## Input 1

```
d = [2, 4, 6, 8]
is_equal(
    square_numbers(d),
    [4, 16, 36, 64]
)

d = [25, 18, 10, 7, 3]
threshold = 15
is_equal(
    filter_aggregation(d, threshold),
    43
)

d = ['Ravi', 'Suresh', 'Neha', 'Alok']
is_equal(
    sort_strings(d),
    ['Alok', 'Neha', 'Ravi', 'Suresh']
)

d = [("city", "Delhi"), ("city", "Mumbai"), ("country", "India")]
is_equal(
    group_by_key(d),
    {'city': ['Delhi', 'Mumbai'], 'country': ['India']}
)
```
## Output 1
```
[4, 16, 36, 64]
43
['Alok', 'Neha', 'Ravi', 'Suresh']
{'city': ['Delhi', 'Mumbai'], 'country': ['India']}
```