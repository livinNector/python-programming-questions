---
title: Calculate the sum of even numbers in a list
---

# Problem Statement

You are given a list of integers. Your task is to read the list from standard input, process it to find the sum of all even numbers, and then print the result to the standard output.

The input consists of a single line containing space-separated integers. Your task is to output the sum of all even integers in the list.

**Example**

**Input**:
```
1 2 3 4 5 6 7 8 9 10
```
**Output**:
```
30
```
**Explanation**:
The sum of even number in the list is evaluated like this 2+4+6+8+10=`30`

# Solution
```py test.py -r 'python test.py'
<template>
def sum_of_evens(numbers: list) -> int:
    '''
    Given a list of integers, return the sum of all even numbers in the list.

    Arguments:
    numbers: list - a list of integers.

    Return: int - the sum of all even numbers in the list.
    '''
    <los>...</los>
    <sol>return sum(num for num in numbers if num % 2 == 0)</sol>
</template>
<suffix>
# Driver code
l = list(map(int, input().split()))
print(sum_of_evens(l))
</suffix>
```

# Public Test Cases

## Input 1
```
1 2 3 4 5 6 7 8 9 10
```

## Output 1
```
30
```

## Input 2
```
11 13 15
```

## Output 2
```
0
```

## Input 3
```
2 4 6 8 10
```

## Output 3
```
30
```


# Private Test Cases

## Input 1
```
3 5 7 9 11
```
## Output 1
```
0
```

## Input 2
```
-2 4 6 8 -10
```
## Output 2
```
6
```

## Input 3
```
0 1 2 3 4 5 6
```
## Output 3
```
12
```

## Input 4
```
10 11 12 13 14
```
## Output 4
```
36
```
