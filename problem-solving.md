---
title: Problem Solving Game
tags: ['problem-solving', 'filtering','loops']
---

# Problem Statement
You are tasked with writing a function that simulates a "number elimination game". Given a list of integers, the game proceeds as follows:

Sum up all the odd numbers in the list.
Multiply all the even numbers by 2.
After completing the above transformations, eliminate all numbers that are divisible by 5 from the list.
Finally, return the list after the transformations. If no numbers remain after the eliminations, return "No numbers left".
Input
A space-separated string of integers. The list will contain between 1 and 1000 integers.
Each integer can range from -10^9 to 10^9.
Output
Return the modified list after performing all transformations. If no numbers remain, print "No numbers left".

# Solution
```python test.py  -r 'python test.py'
<template>
<sol>
nums = list(map(int, input().split()))
odd_sum = sum(num for num in nums if num % 2 != 0)

nums = [num * 2 if num % 2 == 0 else num for num in nums]

nums = [num for num in nums if num % 5 != 0]

if nums:
    print(nums)
else:
    print("No numbers left")
</sol>
</template>

```

# Public Test Cases

## Input 1:
1 2 3 4 5 6 10 7
## Output 1:
[2, 4, 12, 14]

## Input 2:
5 10 15 20
## Output 2:
No numbers left

## Input 3:
-1 -2 -3 -4 0
## Output 3:
[-4, 0]

---

# Private Test Cases

## Input 1:
11 22 33 44 55
## Output 1:
[44, 88]

## Input 2:
6 7 8 9 10
## Output 2:
[12, 14]

## Input 3:
-5 0 -7 8 10
## Output 3:
[0, 16]