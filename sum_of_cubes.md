---
title: Sum of cubes of dict keys
---

# Problem Statement

Given a dictionary `d` and two keys `k1` and `k2`, return the sum of the cubes of the values corresponding to those keys. If either of the keys are not in the given dictionary return '0'.

**Example**
```
d = {'a': 2, 'b': 3, 'c': 4}
sum_of_cubes(d, 'a','b') # Output: 35
sum_of_cubes(d, 'a','e') # Output: 0
```
First case: The sum of cubes is `2^3 + 3^3 = 8 + 27 = 35`, so the result is `35`.
Second case: The key 'e' is not present in the dict, so the result is `0`.


# Solution

```py3 sum_of_cubes.py -r 'python sum_of_cubes.py'
<template>
def sum_of_cubes(d: dict, k1: str, k2: str) -> int:
    '''
    Given a dictionary and two keys, return the sum of the cubes 
    of the values corresponding to those keys. If either of the keys
    are not in the given dictionary return 0.

    Arguments:
    d: dict - a dictionary with key-value pairs.
    k1: str - the first key.
    k2: str - the second key.

    Return: int - sum of cubes of values of k1 and k2.
    '''
    <los>...</los>
    <sol>
    if k1 in d and k2 in d:
        return d[k1]**3 + d[k2]**3
    return 0  </sol>

</template>

```

# Public Test Cases

## Input 1

```
d = {'x': 1, 'y': 2, 'z': 3}
is_equal(
    sum_of_cubes(d, 'y', 'x'),
    9
)
```

## Output 1

```
9
```

## Input 2

```
d = {'a': 4, 'b': 5, 'c': 6}
is_equal(
    sum_of_cubes(d, 'c', 'b'),
    341
)
```

## Output 2

```
341
```

## Input 3

```
d = {'p': 7, 'q': 8}
is_equal(
    sum_of_cubes(d, 'p', 'r'),
    0
)
```

## Output 3

```
0
```

# Private Test Cases

## Input 1

```
d = {'a': 2, 'b': 3, 'c': 4}
is_equal(
    sum_of_cubes(d, 'c', 'a'),
    72
)
d = {'m': 1, 'n': -1}
is_equal(
    sum_of_cubes(d, 'm', 'n'),
    0
)
d = {'u': 3}
is_equal(
    sum_of_cubes(d, 'u', 'u'),
    54
)
is_equal(
    sum_of_cubes(d, 'x', 'u'),
    0
)
```

## Output 1

```
72
0
54
0
```