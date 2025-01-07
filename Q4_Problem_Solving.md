---
title: Trapping Rain Water
tags: ['Array' , 'Two Pointers']
---

# Problem Statement
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Implement the function trap for the same


Example 1:

![image_example](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]

Output: 6

Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]

Output: 9

# Solution
```python test.py  -r 'python test.py'
<template>
def trap(height) -> int:
    '''
    Given a list of non-negative integers representing the height of bars,
    compute how much water can be trapped between the bars after raining.

    Arguments:
    height: A list of integers where each integer represents the height of a bar.

    Return:
    int: The total amount of water trapped between the bars.
    '''
    <los>...</los>
    <sol>
    n = len(height) # Number of elements in the input array
    water = 0       # Variable to store the total trapped water

    # Arrays to store maximum height to the left and right of each index
    l_max = [0] * n
    r_max = [0] * n

    # Calculate the maximum height to the left of each index
    l_max[0] = height[0] # First element's maximum height to the left is itself
    for i in range(1, n):
        l_max[i] = max(height[i], l_max[i - 1])

    # Calculate the maximum height to the right of each index
    r_max[n - 1] = height[n - 1] # Last element's maximum height to the right is itself
    for i in range(n - 2, -1, -1):
        r_max[i] = max(height[i], r_max[i + 1])

    # Iterate through each index (excluding the first and last)
    for i in range(1, n - 1):
        # Calculate the maximum water current height can hold above itself
        water += min(r_max[i], l_max[i]) - height[i]

    return water </sol>
</template>
<suffix_invisible>
{% include './utils.py.jinja' %}
</suffix_invisible>
```

# Public Test Cases

## Input 1

```
d = [0,1,0,2,1,0,1,3,2,1,2,1]
is_equal(
    trap(d),
    6
)
```

## Output 1

```
6
```

## Input 2

```
height = [0, 1, 2, 3, 4, 5, 6]
is_equal(
    trap(height),
    0
)
```

## Output 2
```
0
```

## Input 3

```
height = [4, 2, 0, 3, 1, 2]
is_equal(
    trap(height),
    5
)
```

## Output 3

```
5
```


# Private Test Cases

## Input 1

```
height = [4,2,0,3,2,5]
is_equal(
    trap(height),
    9
)
```

## Output 1

```
9
```

## Input 2

```
height = [1, 3, 2, 4, 1, 2, 3]
is_equal(
    trap(height),
    4
)
```

## Output 2

```
4
```

## Input 3

```
height = [5, 2, 1, 2, 1, 5]
is_equal(
    trap(height),
    14
)
```

## Output 3

```
14
```

## Input 4

```
height = [3, 1, 2, 4, 1, 2, 3]
is_equal(
    trap(height),
    6
)
```

## Output 4

```
6
```




