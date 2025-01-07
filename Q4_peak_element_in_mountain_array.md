---
title:Peak Element in a Mountain Array
---

# Problem Statement

A mountain array is defined as an array where:

1. The elements initially increase to a single peak element.
2. The elements then strictly decrease.
You are given a mountain array arr. Your task is to find the index of the peak element using binary search to achieve efficient performance.

3. The peak element is the one that is greater than its neighbors.

**Example**
```
input: arr = [1, 2, 3, 1]
```
Output : 2 which is index of element 3


# Solution

```py3 test.py -r 'python test.py'
<template>
def peak_index_in_mountain_array(arr: list[int]) -> int:
    """
    Find the peak element in a mountain array using binary search.

    Args:
    arr (list[int]): A list of integers representing the mountain array.

    Returns:
    int: The index of the peak element.
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    
    return left
</template>

<suffix>
# Input handling (for testing purposes only)
if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    print(peak_index_in_mountain_array(arr))
</suffix>

```

# Public Test Cases

## Input 1

```
arr = [1, 2, 1, 3, 5, 6, 4, 2]
```

## Output 1

```
5
```

## Input 2

```
arr = [10, 20, 30, 40, 50, 60, 50, 40, 30, 20, 10]
```

## Output 2

```
5
```

## Input 3

```
arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]
```

## Output 3

```
4
```

# Private Test Cases

## Input 1

```
arr = [5, 6, 7, 8, 9, 5, 3, 1]
```

## Output 1

```
4
```
