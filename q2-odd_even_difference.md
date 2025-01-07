---
title: odd even difference
---

# Problem Statement

Given a list of two or more integers `L`, return the absolute difference of average of elements at odd indices and even indices
**Example**
```py3
odd_even_difference([1,2,3,4]) # 2
odd_even_difference([-1,0,5]) # 4
odd_even_difference([0,0,0,0]) # 0
```

# Solution

```py3 test.py -r 'python test.py'
<prefix>
# some prefix   
</prefix>
<template>
def odd_even_difference(L: list) -> int:
    '''
    Given an list of two or more integers, return the absolute difference of average of elements at odd indices and even indices

    Arguments:
    L: list - a list of integers

    Return: int - difference of elements
    '''
    <los>...</los>
    <sol>return abs((sum(L[::2])/len(L[::2])) - (sum(L[1::2])/len(L[1::2])))</sol>
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
    odd_even_difference([1,2,3,4]),
    1
)
```

## Output 1

```
1
```

## Input 2

```
is_equal(
    odd_even_difference([-1,0,5]),
    2
)
```

## Output 2

```
2
```

## Input 3 

```
is_equal(
    odd_even_difference([0,0,0,0]),
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
L = [1,7,2,9]
is_equal(
    odd_even_difference(L),
    6.5
)

L = [-1,0,1,0]
is_equal(
    odd_even_difference(L),
    0
)

L = [-1,1]
is_equal(
    odd_even_difference(L),
    2
)

L = [1,1]
is_equal(
    odd_even_difference(L),
    0
)
```

## Output 1

```
6.5
0
2
0