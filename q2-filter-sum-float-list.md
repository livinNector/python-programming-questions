---
title: Filter and Sum List of Floats
---

# Problem Statement

Given a list of floats `data` and a threshold value `threshold`, filter out values greater than the threshold and return the sum of the remaining values.

**Example**
```
filter_and_sum([1.2, 2.5, 3.8, 0.7], 2.5) # 3.9
filter_and_sum([10.1, 15.5, 6.2], 10) # 16.3
filter_and_sum([0.9, 1.5, 3.0, 7.5], 4) # 5.4
```

# Solution
```py3 test.py -r 'python test.py'
<prefix>
# some prefix   
</prefix>
<template>
def filter_and_sum(data: list, threshold: float) -> float:
    '''
    Given a list of floats and a threshold, return the sum of all values <= threshold.

    Arguments:
    data: list - list of floats.
    threshold: float - threshold value.

    Return: float - sum of filtered values.
    '''
    <los>...</los>
    <sol>return sum(filter(lambda x: x <= threshold, data))</sol>
    test = <los>...</los><sol>'test'</sol> #tests
</template>
<suffix>
# some suffix
</suffix>
```

# Public Test Cases

## Input 1
```
filter_and_sum([1.2, 2.5, 3.8, 0.7], 2.5) 
```

## Output 1
```
3.9
```

## Input 2
```
filter_and_sum([10.1, 15.5, 6.2], 10) 
```

## Output 2
```
16.3
```

## Input 3
```
filter_and_sum([0.9, 1.5, 3.0, 7.5], 4) 
```

## Output 3
```
5.4
```

# Private Test Cases

## Input
```
n = [5.5, 6.6, 3.4, 4.0]
filter_and_sum(n, 6)

n = [1.1, 2.2, 3.3]
filter_and_sum(n, 2.5)

n = [10.5, 5.3, 7.9]
filter_and_sum(n, 6)

n = [3.0, 6.5, 2.2, 4.8]
filter_and_sum(n, 4)
```

## Output
```
7.4
3.3
15.3
6.2
```
