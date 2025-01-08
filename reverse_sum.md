---
title: Reverse of Sum of First and Last Elements of a List
tags: ['list manipulation', 'basic operations', 'reverse', 'sum']
---

# Problem Statement
Write a function `reverse_sum_of_indices` that takes a list of integers as an argument and performs the following steps:

1. Computes the sum of the first and last elements of the list.
2. Reverses the digits of the resulting sum.
3. Returns the reversed number as an integer.

### Constraints:
- The list will always contain at least two integers.
- The list elements are integers and may be negative or positive.

### Example Usage
```plaintext
reverse_sum_of_indices([12, 34, 56, 78]) ➞ 9  # 12 + 78 = 90, reverse is 9
reverse_sum_of_indices([1, 2, 3, 4]) ➞ 5      # 1 + 4 = 5, reverse is 5
reverse_sum_of_indices([-10, 20, 30, -40]) ➞ -5 # -10 + -40 = -50, reverse is -5
```


# Solution

```python reverse_sum.py  -r 'python reverse_sum.py'
<prefix>
# some prefix
</prefix>
<template>
def reverse_sum_of_indices(lst: list) -> int:
    """
    Computes the sum of the first and last elements of a list and returns the reversed sum.

    Arguments:
    lst: list - A list of integers.

    Returns:
    int - The reversed sum of the first and last elements.
    """
    <los>...</los>
    <sol>
    total = lst[0] + lst[-1]
    reversed_sum = int(str(total)[::-1]) if total >= 0 else -int(str(abs(total))[::-1])
    return reversed_sum
    </sol>

</template>
<suffix>
# Driver code
l = list(map(int, input().split(',')))
print(reverse_sum_of_indices(l))
</suffix>
```

# Public Test Cases

## Input 1

```
10,20,30,40,50
```

## Output 1

```
6
```


## Input 2

```
123,456,789
```

## Output 2

```
219
```


## Input 3

```
7,0,0,4
```

## Output 3

```
11
```


# Private Test Cases

## Input 1

```
-15,5,20,-35

```

## Output 1

```
-5

```

## Input 2

```
1,2,3,4,5,6,7,8,9,-10

```

## Output 2

```
-9
```

## Input 3

```
0,10,20,30,40,50
```

## Output 3

```
5
```

## Input 4

```
-100,0,0,100
```

## Output 4

```
0
```

## Input 5

```
9876,0,0,0,0,6789
```

## Output 5

```
56661
```
