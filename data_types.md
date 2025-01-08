---
title: Key-Value Transformation in a Dictionary
tags: ['python', 'functions']
---
# Problem Statement
Write a function reverse_dict(d: dict) -> dict that reverses the keys and values of a dictionary. Assume values are unique and hashable.
**Sample Input**
```
{1: 'a', 2: 'b', 3: 'c'}
```
**Sample Output**
```
{'a': 1, 'b': 2, 'c': 3}
```
# Solution
```py test.py -r 'python3 test.py'
<prefix>
def reverse_dict(d: dict) -> dict:
    """
    Reverses the keys and values of the given dictionary.

    Arguments:
    d: dict - a dictionary where the values are unique and hashable.

    Returns:
    dict - a new dictionary with the keys and values reversed.
    """
</prefix>
<template>
    return <sol>{value: key for key, value in d.items()}</sol>
</template>

```
# Public Test Cases
## Input 1
```
{1: 'a', 2: 'b', 3: 'c'}
```
## Output 1
```
{'a': 1, 'b': 2, 'c': 3}
```
## Input 2
```
{'x': 10, 'y': 20, 'z': 30}
```
## Output 2
```
{10: 'x', 20: 'y', 30: 'z'}
```
## Input 3
```
{100: 'apple', 200: 'banana'}
```
## Output 3
```
{'apple': 100, 'banana': 200}
```

# Private Test Cases
## Input 1
```
{'cat': 1, 'dog': 2, 'mouse': 3}
```
## Output 1
```
{1: 'cat', 2: 'dog', 3: 'mouse'}
```