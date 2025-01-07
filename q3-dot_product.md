---
title: dot_product
---

# Problem Statement

Given two lists of integers `L1` and `L2`, return the dot product of the lists.

The first line of the input is list1 of integers separated by spaces
The second line of the input is list2 of integers separated by spaces

**Example**
```py3
dot_product([1,2,3,4],[5,6,7,8]) # 70 
dot_product([1,2],[0,0]) # 0
dot_product([1,-1,0],[0,1,1],4) # -1
```

# Solution

```py3 test.py -r 'python test.py'
<prefix>
# some prefix   
</prefix>
<template>
def dot_product(L1: list,L2: list) -> int:
    '''
    Given two lists of integers `L1` and `L2`, return the dot product of the lists.

    Arguments:
    L1: list - a list of integers
    L2: list - a list of integers

    Return: int - dot product of the lists
    '''
    <los>...</los>
    <sol>
    dot = 0
    for i in range(len(L1)):
        dot += L1[i]*L2[i]
    return dot
    </sol>
    test = <los>...</los><sol>'test'</sol> #tests
</template>
<suffix>
# Driver code
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
print(dot_product(l1,l2))
</suffix>
<suffix_invisible>
{% include '../function_type_and_modify_check_suffix.py.jinja' %}
</suffix_invisible>
```

# Public Test Cases

## Input 1

```
1 2 3 4
5 6 7 8
```

## Output 1

```
70
```

## Input 2

```
1 2
0 0
```

## Output 2

```
0
```

## Input 3 

```
1 -1 0
0 1 1
```

## Output 3

```
-1
```

# Private Test Cases

## Input 1

```
0 0
0 0
```

## Output 1

```
0
```

## Input 2

```
1 7
2 9
```

## Output 2

```
65
```

## Input 3 

```
1 0
0 1
```

## Output 3

```
0
```

## Input 4 

```
100 50
20 10
```

## Output 4

```
2500
```