---
title: Athelete Sort
tags: ['sorting', 'table', 'index', 'list']
---

# Problem Statement

You are given a spreadsheet that contains a list of athletes and their details (such as age, height, weight, and so on). You are required to sort the data based on the **k-th attribute** (1-based index) and print the final resulting table. Follow the example given below for better understanding.

![example](pic.png)



Note:
- If two attributes are the same for different rows, the row that appeared first in the input should be printed first.

### Input Format:
- The first line contains two integers, `n` (number of rows) and `m` (number of attributes).
- The next `n` lines contain `m` elements each, representing the details of each athlete.
- The last line contains a single integer `k`, representing the index (1-based) of the attribute based on which the data should be sorted.

### Constraints:
- `1 ≤ n ≤ 1000` (number of rows)
- `1 ≤ m ≤ 1000` (number of attributes)
- Each element in the rows will be an integer and will be within the range of `-10^9 ≤ element ≤ 10^9`.

### Output Format:
- Print the `n` lines of the sorted table.
- Each line should contain the space-separated elements of the respective row after sorting.


## Input Format
1. The first line contains the length of side \( AB \).
2. The second line contains the length of side \( BC \).

## Constraints
- \( AB \) and \( BC \) are natural numbers.

## Output Format
Output \( \theta \) (angle \( \angle MBC \)) in degrees, rounded to the nearest integer.


# Solution
```python test.py  -r 'python test.py'
<prefix>
import math
import os
import random
import re
import sys
</prefix>
<template>
nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    <sol>
    arr_sorted = sorted(arr, key=lambda x: x[k])

    # Print the sorted list of athlete details
    for row in arr_sorted:
        print(" ".join(map(str, row))) 
    </sol>
<suffix_invisible>
{% include './utils.py.jinja' %}
</suffix_invisible>
</template>
```

# Public Test Cases

## Input 1

```
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
2

```

## Output 1

```
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12

```


## Input 2

```
3 4
5 6 7 8
9 10 2 3
6 4 8 1
3

```

## Output 2

```
6 4 8 1
5 6 7 8
9 10 2 3

```

# Private Test Cases

## Input 1

```
4 2
8 10
6 12
5 15
9 5
2

```

## Output 1

```
9 5
8 10
6 12
5 15

```

## Input 2

```
3 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
4

```

## Output 2

```
5 4 3 2 1
1 2 3 4 5
2 3 4 5 6

```

## Input 3

```
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
```

## Output 3

```
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
```

## Input 4

```
100 10
64 79 18 94 46 81 74 97 71 92
46 24 23 20 68 15 53 93 24 91
17 66 34 64 28 5 55 25 44 96
16 71 80 84 5 79 63 77 69 77
33 77 24 13 58 81 41 36 73 62
93 26 16 55 61 51 39 69 29 45
44 85 1 48 23 59 52 82 50 37
77 74 9 21 35 54 81 57 32 76
82 21 72 49 98 21 77 64 6 63
68 17 93 83 12 43 84 28 96 86
9 16 3 89 38 11 70 25 41 38
49 99 31 19 85 97 80 63 16 69
50 85 80 75 36 48 56 69 63 94
78 80 83 86 92 60 56 90 22 73
69 81 45 9 67 25 82 46 68 82
98 38 23 31 38 83 37 76 69 82
95 48 21 64 25 6 38 96 69 23
44 97 46 54 21 56 65 51 66 34
87 22 27 24 55 48 90 10 8 51
```

## Output 4

```
4 76 57 28 60 3 46 4 6 17
93 85 99 87 67 3 54 16 98 57
17 66 34 64 28 5 55 25 44 96
95 48 21 64 25 6 38 96 69 23
48 91 7 56 41 6 4 26 96 39
81 38 65 40 80 7 90 82 33 13
90 30 98 28 92 8 83 71 24 62
73 85 64 17 46 9 79 54 27 15
9 16 3 89 38 11 70 25 41 38
76 57 5 2 25 12 46 62 32 68
8 98 51 73 32 13 59 12 56 92
25 85 54 43 53 13 52 70 38 76
74 19 15 66 17 14 34 50 57 16
46 24 23 20 68 15 53 93 24 91
92 22 72 60 96 15 17 4 79 27
41 86 3 29 41 15 99 50 82 84
6 66 54 5 82 17 41 25 3 71
14 15 11 1 34 20 54 58 45 38
63 82 58 75 13 20 79 89 55 89
82 21 72 49 98 21 77 64 6 63
```
