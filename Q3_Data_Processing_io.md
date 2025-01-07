---
title: Maximum Consecutive Difference
tags: ['sample tag1', 'sample tag2']
---

# Problem Statement

Write a Python program to find the maximum difference between two consecutive elements in a sorted list of integers. The input should be read from standard input (stdin) as a space-separated string of integers. The program should first parse the input, sort the integers in ascending order, compute the differences between consecutive elements, and then output the maximum difference.

**Example Input (from stdin):**  
```
4 1 7 3 9
```

**Example Output:**  
```
4
```

**Explanation:**  
- Sorted list: `1, 3, 4, 7, 9`
- Consecutive differences: `2, 1, 3, 2`
- Maximum difference: `4`
# Solution
```python test.py  -r 'python test.py'
<template>
def calculate_differences(numbers):
    """
    Calculate differences between consecutive elements in a sorted list.
    
    Args:
        sorted_list (list): A list of integers sorted in ascending order.
    
    Returns:
        list: A list of differences between consecutive elements.
    """
    <los>...</los>
<sol>
    return [abs(numbers[i+1] - numbers[i]) for i in range(len(numbers) - 1)] </sol>
</template>
<suffix>
differences = calculate_differences(list(map(int, input().split())))
max_difference = max(differences)

# Output the maximum difference
print(max_difference)
</suffix>
```

# Public Test Cases

## Input 1

```
4 1 7 3 9
```

## Output 1

```
6
```

## Input 2

```
10 20 5 15
```

## Output 2

```
15
```

## Input 3

```
100 90 80 70
```

## Output 3

```
10
```

# Private Test Cases

## Input 1

```
10 50 20 40 90
```

## Output 1

```
50
```

## Input 2

```
-10 0 10 -5 5
```

## Output 2
```
15
```

## Input 3

```
5 5 5 5 5
```

## Output 3

```
0
```

## Input 4

```
7 15 3 11 20
```

## Output 4

```
12
```
