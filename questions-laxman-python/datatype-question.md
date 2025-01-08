---
title: Perform Operations on Nested Data Types
---

# Problem Statement

Write a function `nested_operations` that performs the following operations on nested data types:
1. Add an integer and a float and return the result.
2. Append a string to the inner list of a dictionary under a given key. If the key doesn't exist, create the key with the string as the first element of a new list.
3. Check if a key exists in the dictionary and return `True` or `False`.
4. Add an element to the set nested inside a list and return the updated list of sets.

**Function Signature**
```python
def nested_operations(a: int, b: float, s: str, key: str, d: dict, lst_of_sets: list) -> tuple:
    pass
```

**Example**
```python
a = 5
b = 3.2
s = "apple"
key = "fruits"
d = {"vegetables": ["carrot"]}
lst_of_sets = [{1, 2}, {3, 4}]

result = nested_operations(a, b, s, key, d, lst_of_sets)
# result: (8.2, {"vegetables": ["carrot"], "fruits": ["apple"]}, True, [{1, 2, 5}, {3, 4}])
```

# Solution

```py3 solution.py -r 'python solution.py'
<template>
def nested_operations(a: int, b: float, s: str, key: str, d: dict, lst_of_sets: list) -> tuple:
    '''
    Perform operations on nested data types.

    Arguments:
    a: int - an integer.
    b: float - a float.
    s: str - a string.
    key: str - a dictionary key to check or update.
    d: dict - a dictionary.
    lst_of_sets: list - a list containing sets.

    Returns:
    A tuple containing:
        - Sum of a and b (int + float).
        - Updated dictionary with the string appended to the list under the key.
        - Boolean indicating if key exists in the dictionary.
        - Updated list of sets with the integer added to the first set.
    '''
    <los>...</los>
    <sol>
    sum_result = a + b
    if key in d:
        d[key].append(s)
    else:
        d[key] = [s]
    key_exists = key in d
    if lst_of_sets:
        lst_of_sets[0].add(a)
    return (sum_result, d, key_exists, lst_of_sets)
    </sol>
</template>
```

# Public Test Cases

## Input 1

```
a, b, s, key, d, lst_of_sets = 2, 2.5, "banana", "fruits", {"fruits": ["apple"]}, [{1, 2}, {3, 4}]
modify_check(
    lambda x: nested_operations(*x),
    (a, b, s, key, d, lst_of_sets), 
    (4.5, {"fruits": ["apple", "banana"]}, True, [{1, 2, 2}, {3, 4}]),
    should_modify=False
)
```

## Output 1

```
(4.5, {'fruits': ['apple', 'banana']}, True, [{1, 2}, {3, 4}])
```

## Input 2

```
a, b, s, key, d, lst_of_sets = -1, 1.5, "grape", "berries", {}, [{0}]
modify_check(
    lambda x: nested_operations(*x),
    (a, b, s, key, d, lst_of_sets), 
    (0.5, {"berries": ["grape"]}, True, [{0, -1}]),
    should_modify=False
)
```

## Output 2

```
(0.5, {'berries': ['grape']}, True, [{0, -1}])
```

# Private Test Cases

## Input 1

```
a, b, s, key, d, lst_of_sets = 0, 0.0, "hello", "greeting", {}, [set()]
modify_check(
    lambda x: nested_operations(*x),
    (a, b, s, key, d, lst_of_sets), 
    (0.0, {"greeting": ["hello"]}, True, [{0}]),
    should_modify=False
)
```

## Output 1

```
(0.0, {'greeting': ['hello']}, True, [{0}])
```

## Input 2

```
a, b, s, key, d, lst_of_sets = 10, -2.5, "pear", "fruits", {"vegetables": ["carrot"]}, [{7}]
modify_check(
    lambda x: nested_operations(*x),
    (a, b, s, key, d, lst_of_sets), 
    (7.5, {"vegetables": ["carrot"], "fruits": ["pear"]}, True, [{7, 10}]),
    should_modify=False
)
```

## Output 2

```
(7.5, {'vegetables': ['carrot'], 'fruits': ['pear']}, True, [{7, 10}])
```
