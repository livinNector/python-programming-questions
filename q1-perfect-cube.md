---
title: Check if a number is a perfect cube
---

# Problem Statement

Given a positive integer `n`, return `True` if the number is a perfect cube (i.e., the cube root of `n` is an integer), and `False` otherwise.

**Example**
```py3
is_perfect_cube(27) # True, cube root is 3
is_perfect_cube(64) # True, cube root is 4
is_perfect_cube(20) # False, cube root is not an integer
is_perfect_cube(1)  # True, cube root is 1
```



# Solution
```py3 test.py -r 'python test.py'
<prefix>
# some prefix   
</prefix>
<template>
def is_perfect_cube(n: int) -> bool:
    '''
    Given a positive integer, check if it is a perfect cube.

    Arguments:
    n: int - the number to check.

    Return: bool - True if it is a perfect cube, else False.
    '''
    <los>...</los>
    <sol>return n == int(n ** (1/3)) ** 3</sol>
    test = <los>...</los><sol>'test'</sol> #tests
</template>
<suffix>
# some suffix
</suffix>
<suffix_invisible>
{% include './function_type_and_modify_check_suffix.py.jinja' %}
</suffix_invisible>
```


# Public Test Cases


## Input 1
```
is_equal(
    is_perfect_cube(27),
    True
)
```

## Output 1
```
True
```

## Input 2
```
is_equal(
    is_perfect_cube(64),
    True
)
```

## Output 2
```
True
```

## Input 3
```
is_equal(
    is_perfect_cube(20),
    False
) 
```

## Output 3
```
False
```

# Private Test Cases

## Input
```
n = 8
is_equal(
    is_perfect_cube(n),
    True
)

n = 1
is_equal(
    is_perfect_cube(n),
    True
)

n = 50
is_equal(
    is_perfect_cube(n),
    False
)

n = 125
is_equal(
    is_perfect_cube(n),
    True
)
```

## Output
```
True
True
False
True
```
