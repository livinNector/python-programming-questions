---
title :  Find longest vowel substring in an original substring.
---

# Problem Statement
Write a program that takes a single line of input: a string `s`. The program should print the longest substring where each character is a vowel (`a,e,i,o,u`). If there are multiple substrings of the same length, print the first one. If no vowels are present, print an empty string.

**Example**
```
longest_vowel_substring('aeiouxyz') #output: 'aeiou'
longest_vowel_substring('oouuuaaeeii') #output: 'oouuuaaeeii'
longest_vowel_substring('rhythm') #output: ''
```

First case: The longest substring of vowels is 'aeiou' which is the entire string.

Second case: The longest substring of vowels is 'oouuuaaeeii' which is the entire string.

Third case: There are no vowels in the string 'rhythm', so the output is an empty.


# Solution
```py3 test.py -r 'python test.py'
<prefix>
# some prefix
</prefix>
<template>
def longest_vowel_substring():
    '''
    Given an input string, find the longest substring where all characters are vowels.

    Arguments:
    None - reads input from stdin.

    Return:
    None - prints the result to stdout.
    '''
    <los>...</los>
    <sol>
    s = input().strip()
    vowels = set("aeiou")
    max_length, max_substring, current = 0 , "" , ""
    for char in s: 
        if char in vowels:
            current+=char
            if len(current) > max_length:
                max_length = len(current)
                max_substring = current
            else:
                current = ""
    print(max_substring)
    </sol>
</template>
<suffix>
# some suffix
</suffix>
{% include '../function_type_and_modify_check_suffix.py.jinja' %}
</siffix_invisible>
```


# Public Test Cases

## Input 1
```
is_equal(
    
    longest_vowel_substring("earthproblem"),
    "ea"
)

```

## Output 2
```
"ea"
```

## Input 2

```
is_equal(
    
    longest_vowel_substring("try"),
    ""
)
```

```
## Output 2
""
```

## Input 3
```
is_equal(
    longest_vowel_substring("ioioio"),
    "ioio"
)
```

```
## Output 3
"ioio"
```


# Private Test Cases
## Input 1
```
is_equal(
    longest_vowel_substring("apple"),
    "a"
)
```

```
## Output 1
"a"
```

## Input 2
```
is_equal(
    longest_vowel_substring("aeiaeiouu"),
    "aeiaei"
)
```

```
## Output 2
"aeiaei"
```


## Input 3
```
is_equal(
    longest_vowel_substring("xyzxyzxyz"),
    ""
)
```

```
## Output 3
""
```

