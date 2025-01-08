---
title: Data Types Operations
tags: ['string', 'int','conversion','sum']
---

# Problem Statement
Write a function sum_first_last(input_str: str) -> int | str that takes a single string as input. The function should:

Check if the input string contains only numeric characters (0-9).
If the string contains only numbers, calculate the sum of the first and last digits and return the result.
If the string cannot be converted to an integer (contains any non-numeric characters), return the string "N/A".
Constraints:

The input string will be a non-empty string.
Length of string is more than or equal to 2.
Assume the string does not contain leading or trailing whitespace.
Do not use exception handling (try-except) for solving the problem.
Examples:

sum_first_last("12345") should return 6 (1 + 5).
sum_first_last("987654321") should return 10 (9 + 1).
sum_first_last("007") should return 7 (0 + 7).
sum_first_last("12a45") should return "N/A".
sum_first_last("abcd") should return "N/A".

# Solution
```python test.py  -r 'python test.py'  
<prefix>  
def convert_and_sum(input_str: str) -> int | str:  
    # Your code here  
    pass  
</prefix>  
<template>  
<sol>  
def convert_and_sum(input_str: str) -> int | str:  
    if input_str.isdigit():
        return sum(int(input_str[0])+int(input_str[-1]))
    else:  
        return "N/A"  
</sol>  
</template>  
<suffix>  

if __name__ == "__main__":  
    input_str = input("Enter a string: ")  
    result = convert_and_sum(input_str)  
    print(result)  
</suffix>
<suffix_invisible>  
</suffix_invisible>  


# Public Test Cases

## Input 1

```
12345
```

## Output 1

```
6
```


## Input 2

```
2098
```

## Output 2

```
10
```


## Input 3

```
1234a
```

## Output 3

```
N/A
```


## Input 4

```
a1234
```

## Output 4

```
N/A
```


# Private Test Cases

## Input 1

```
19
```

## Output 1

```
10
```

## Input 2

```
1a
```

## Output 2

```
N/A
```
