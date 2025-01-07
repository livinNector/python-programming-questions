---
title: Integer with decimal
---

# Problem Statement

Given an integer `n`, return the digits of absolute value of `n` separated by `.`

**Example**
```py3
integer_sep_decimal(123) # 1.2.3
integer_sep_decimal(-105) # 1.0.5
integer_sep_decimal(1) # 1
```

# Solution

```py3 test.py -r 'python test.py'
<prefix>
# some prefix   
</prefix>
<template>
def integer_sep_decimal(n: int) -> str:
    '''
    Given an integer, return the digits separated by '.'

    Arguments:
    n: int - an integer

    Return: str - string separated by '.'
    '''
    <los>...</los>
    <sol>return '.'.join(str(abs(n)))</sol>
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
    integer_sep_decimal(123),
    '1.2.3'
)
```

## Output 1

```
'1.2.3'
```

## Input 2

```
is_equal(
    integer_sep_decimal(-105),
    '1.0.5'
)
```

## Output 2

```
'1.0.5'
```

## Input 3 

```
is_equal(
    integer_sep_decimal(1),
    '1'
)
```

## Output 3

```
'1'
```

# Private Test Cases

## Input 1

```
n = 0
is_equal(
    integer_sep_decimal(n),
    '0'
)

n = -1
is_equal(
    integer_sep_decimal(n),
    '1'
)

n = 100
is_equal(
    integer_sep_decimal(n),
    '1.0.0'
)
n = 1729
is_equal(
    integer_sep_decimal(n),
    '1.7.2.9'
)
```

## Output 1

```
'0'
'1'
'1.0.0'
'1.7.2.9'
```