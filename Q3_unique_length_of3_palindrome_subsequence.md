---
title: Unique Length-3 Palindromic Subsequences
---

# Problem Statement

Given a string s, find the number of unique palindromic subsequences of length 3 in the string. A subsequence is defined as a sequence derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

**Note:**

**Input Format:** A single string s (1 ≤ |s| ≤ 10^4) consisting of lowercase English letters. 

**Output Format:** he count of unique palindromic subsequences of length 3.

**Sample Input**
```
aabca
```
**Sample Output**
```
3
```

# Solution
```py test.py -r 'python test.py' 
<template>
def count_unique_palindromes(s):
    """
    Count the number of unique length-3 palindromic subsequences in the string.
    
    Args:
        s (str): The input string.
    
    Returns:
        int: The count of unique palindromic subsequences of length 3.
    """
    # Initialize a set to store unique characters
    unique_chars = set(s)
    count = 0

    # Iterate through all unique characters
    for letter in unique_chars:
        first_index = -1
        last_index = -1

        # Find the first and last occurrence of the letter
        for i, char in enumerate(s):
            if char == letter:
                if first_index == -1:
                    first_index = i
                last_index = i

        # Collect all characters between first and last occurrences
        between_elements = set(s[first_index + 1:last_index])

        # Add the count of unique characters between first and last
        count += len(between_elements)

    return count
</template>
<suffix>
# Input parsing
s = input().strip()

# Output the result
print(count_unique_palindromes(s))
</suffix>


```

# Public Test Cases

## Input 1

```
aabca
```

## Output 1 

```
3
```


## Input 2

```
aaa
```

## Output 2

```
1
```


## Input 3

```
abc
```

## Output 3

```
0
```


# Private Test Cases

## Input 1

```
abccba
```

## Output 1

```
3
```

## Input 2

```
xyzzyx
```

## Output 2

```
3
```
