---
title: Data Processing Operations
tags: ['list', 'filter', 'map']
---

# Problem Statement

Write a function `process_numbers(input_list: list[int]) -> int` that takes a list of integers as input. The function should:

1. **Filter out the negative numbers** from the list.
2. **Double the remaining values** in the list.
3. **Find the unique values** after doubling.
4. **Calculate and return the sum** of the unique doubled values.

### Constraints:
- The input list will be non-empty.
- The list will contain only integers (both positive and negative).

### Examples:

`process_numbers([1, -3, 4, 2, -5, 2])` should return `14` (after filtering, doubling, finding unique values, and summing).

`process_numbers([1, 2, 3, -4, -5, 3])` should return `18` (after filtering, doubling, finding unique values, and summing).

`process_numbers([10, 10, -5, -5, 7])` should return `34` (after filtering, doubling, finding unique values, and summing).

`process_numbers([-1, -2, -3])` should return `0` (no positive numbers to double and sum).


# Solution
```python test.py  -r 'python test.py'
<prefix>

def process_numbers(input_list):
    # Your code here  
    pass  

</prefix>
<template>
<sol>
def process_numbers(input_list):
    positive_numbers = [num for num in input_list if num >= 0]
    
    doubled_values = [num * 2 for num in positive_numbers]
    
    unique_values = set(doubled_values)
    
    return sum(unique_values)
</sol>
</template>
<suffix>  
if __name__ == "__main__":
    input_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
    result = process_numbers(input_list)
    print(result)
</suffix>
<suffix_invisible>

</suffix_invisible>

<prefix>

</prefix>
<template>
<sol>  </sol>
</template>
<suffix>

</suffix>
<suffix_invisible>

</suffix_invisible>
```

# Public Test Cases
## Input 1

```
1, -3, 4, 2, -5, 2
```

## Output 1

```
14
```


## Input 2

```
1, 2, 3, -4, -5, 3
```

## Output 2

```
18
```


## Input 3

```
10, 10, -5, -5, 7
```

## Output 3

```
34
```


## Input 4

```
-1, -2, -3
```

## Output 4

```
0
```


# Private Test Cases

## Input 1

```
100, 50, -50, 100
```

## Output 1

```
300
```

## Input 2

```
5, -5, -5, 5
```

## Output 2

```
10
```
