---
title : Store the fequency of each element in the dictionay.
---
# Problem statement

Given an matrix `m` , return the dictionay where keys are the elements in the matrix and values are the frequency of each element.

**Example**

```py3
frequency_count([
    [1,2,3],
    [4,1,6],
    [7,8,1]
])

# Returns : {1 : 3 , 2 : 1 , 3 : 1 , 4 : 1 , 6 : 1 , 7 : 1 , 8 : 1}

frequency_count([
    [4,4,4],
    [4,1,6],
    [7,8,1]
])

# Returns : {1 : 2 , 4 : 4 , 6 : 1 , 7 : 1 , 8 : 1}

```

First case: As we see 1 present 3 times in a matrix and 2 present 1 time in a matrix. So the frequency of 1 is 3 and frequency of 2 is 1 same thing happen with other elements.

Second case: As we see 4 present 4 times in a matrix and 1 present 2 time in a matrix. So the frequency of 4 is 4 and frequency of 1 is 2 same thing happen with other elements.


#Solution

```py3 test.py -r 'python test.py'
<prefix>
# some prefix
</prefix>
<template>
def frequency_count(m : list[list[int]]) -> dict[int,int]:
    '''
    Given a matrix , count the frequency of each element.

    Arguments:
    m: list[list[int]] - a 2D matrix of integers.

    Return : dict[int,int] - a dictionary where keys are elements, and values are their frequencies.
    '''
    
    <los>...</los>
    <sol>
    from collections import Counter
    flattened = [element for row in m for elements in row]
    return dict(Counter(flattened))
    </sol>
    test = <los>...</los><sol>'test'</sol> #tests
</template>
<suffix>
#some suffix
</suffix>
<suffix_invisble>
{% include '../function_type_and_modify_check_suffix.py.jinja'%}
</suffix_invisble>
```

# Public Test Cases

## Input 1
```
is_equal(
    frequency_count([
        [2,1,4],
        [5,4,3],
        [9,8,7]
    ]),
    {1 : 1 , 2 : 1 , 3 : 1, 4 : 2, 5 : 1, 8 : 1 , 7 : 1 , 9 : 1}
)

```

## Output 2
```
{1 : 1 , 2 : 1 , 3 : 1, 4 : 2, 5 : 1, 8 : 1 , 7 : 1 , 9 : 1}
```

## Input 2

```
is_equal(
    frequency_count([
        [4,5,6],
        [4,5,6]
    ]),
    {4 : 2 , 5 : 2 , 6 : 2}
)
```

```
## Output 2
{4 : 2 , 5 : 2 , 6 : 2}
```

## Input 3
```
is_equal(
    frequency_count([
        [1,1,1],
        [1,1,1]
    ]),
    {1 : 6}
)
```

```
## Output 3
{1 : 6}
```


# Private Test Cases
## Input 1
```
is_equal(
    frequency_count([
        [10 , 20 , 10],
        [30,10]
    ]),
    {10 : 3 , 20 : 1 , 30 : 1}
)
```

```
## Output 1
{10 : 3 , 20 : 1 , 30 : 1}
```

## Input 2
```
is_equal(
    frequency_count([]),
    {}
)
```

```
## Output 2
{}
```


## Input 3
```
is_equal(
    frequency_count([
        [-1 , -2 , -3],
        [-1 , -1 , -2]
    ]),
    {}
)
```

```
## Output 3
{-1 : 3 , -2: 2 , -3: 1}
```



