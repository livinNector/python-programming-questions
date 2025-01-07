---
title: pairs less than pair
---

# Problem Statement
You are given a list of 2D points, represented as pairs (x, y) in a string with random spacing, and a reference point (xr, yr). A point (xi, yi) is considered strictly less than (xr, yr) if both xi < xr and yi < yr.

Write a program to count how many points in the list are strictly less than the reference point and return these points as a list.

**Example**
```py3
pairs_less_than("[(4,5  )     , (-1,           -2)   ,(1,1)]  ",(1,2)) # 1 -> (-1,-2)
pairs_less_than("[ (  4 ,5  ) , (  -1,-2) ,  (  1,1 )  ,   (  2,3), ( 6 ,   7 )]",  (2,3)) # 2 -> (-1,-2),(1,1)
pairs_less_than("[  (3,4),( 5 ,6)   , (0,  0  ), ( -2 ,   -1)  ,( 7  ,8 ) ] ",  (4,-4)) # 0
```

# Solution

```py3 test.py -r 'python test.py'
<prefix>
# some prefix   
</prefix>
<template>
def pairs_less_than(s: string,p: tuple) -> int:
    '''
    You are given a list of 2D points, represented as pairs (x, y) in a string with random spacing, and a reference point (xr, yr). A point (xi, yi) is considered strictly less than (xr, yr) if both xi < xr and yi < yr.

    Write a program to count how many points in the list are strictly less than the reference point and return these points as a list.

    Arguments:
    s: list - a string having a list of integer tuples
    p: tuple - reference point

    Return: int - count of pairs less than p
    '''
    <los>...</los>
    <sol>
    s = s.replace(' ','')
    s = s.replace('[','')
    s = s.replace(']','')
    s = s.replace('(','')
    s = s.replace(')','')
    s = s.replace(',',' ')
    L = list(map(int,s.split()))
    M = []
    for i in range(0,len(L),2):
        M.append(tuple(L[i:i+2]))
    count = 0
    for i in M:
        if i[0] < p[0] and i[1] < p[1]:
            count+=1
    return count
    </sol>
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
    pairs_less_than("[(4,5  )     , (-1,           -2)   ,(1,1)]  ",(1,2)),
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
    pairs_less_than("[ (  4 ,5  ) , (  -1,-2) ,  (  1,1 )  ,   (  2,3), ( 6 ,   7 )]",  (2,3)),
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
    pairs_less_than("[  (3,4),( 5 ,6)   , (0,  0  ), ( -2 ,   -1)  ,( 7  ,8 ) ] ",  (4,-4)),
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
L = "[ ( 2,2 ),( 1,1 ),(   3,4 )  ,(0 ,0  ) ,   ( 5 ,5)] "
p = (2,3)
is_equal(
    pairs_less_than(L,p),
    3
)

L = "[ (8,  9), (  2,3 ),(  6 , 5),(  -1,-1) , (10 ,12 ) ]"
p = (11,13)

is_equal(
    pairs_less_than(L,p),
    5
)

L = "[(1,1)]"
p = (2,3)

is_equal(
    pairs_less_than(L,p),
    1
)

```

## Output 1

```
3
5
1