---
title: Reverse Vowels in a String
tags: ['loop', 'string manipulation', 'reverse', 'conditional statements']
---

# Problem Statement

Write a function that takes a string as input and returns a new string with the positions of all vowels reversed.  
For this problem, vowels are defined as the characters: `a, e, i, o, u` (both uppercase and lowercase).  
The order of all other characters in the string should remain unchanged.

### **Input Format**
- A single string containing alphabets and other characters.

### **Output Format**
- A string where the vowels are reversed, and all other characters remain in their original positions.

### **Example Usage**
```plaintext
reverse_vowels("hello world") ➞ "hollo werld"
reverse_vowels("aeIOu") ➞ "uOIea"
reverse_vowels("Reverse Vowels") ➞ "Revorse Vewels"
```

# Solution

```python reverse_vowels.py -r 'python reverse_vowels.py'
<prefix>
# Prefix to initialize or handle utility definitions
</prefix>
<template>
def reverse_vowels(s: str) -> str:
    '''
    Reverses the vowels in the given string while keeping other characters unchanged.

    Arguments:
    s: str - the input string.

    Returns:
    str - the string with reversed vowels.
    '''
    vowels = "aeiouAEIOU"
    s_list = list(s)
    i, j = 0, len(s) - 1

    while i < j:
        if s_list[i] not in vowels:
            i += 1
        elif s_list[j] not in vowels:
            j -= 1
        else:
            s_list[i], s_list[j] = s_list[j], s_list[i]
            i += 1
            j -= 1
    return ''.join(s_list)
</template>
<suffix>
# Driver code
input_string = input("Enter a string: ")
print(reverse_vowels(input_string))
</suffix>
```

# Public Test Cases

## Input 1

```
hello world
```

## Output 1

```
hollo werld
```


## Input 2

```
aeIOu
```

## Output 2

```
uOIea
```


## Input 3

```
Reverse Vowels
```

## Output 3

```
Revorse Vewels
```


# Private Test Cases

## Input 1

```
Python Programming
```

## Output 1

```
Pythin Pragrommong
```

## Input 2

```
bcdfgBCDFG!@#$%^a
```

## Output 2

```
bcdfgBCDFG!@#$%^a
```

## Input 3

```
!
```

## Output 3

```
!
```

## Input 4

```
abcdefghijklmnopqrstuvwxyz
```

## Output 4

```
ubcdofghijklmnepqrstavwxyz
```

## Input 5

```
heeeellooo wooorld
```

## Output 5

```
hoooollooe weeerld
```
