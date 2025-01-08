---
title: Character Frequency Counter
tags: ['dictionary', 'data processing', 'sorting', 'stdin']
---

# Problem Statement

Given a string \( s \), count the frequency of each **alphanumeric character** in the string.  
Print the character frequencies in a sorted order (by keys) in the following format:

- Each key-value pair on a new line.
- Format: `character: frequency`.

Symbols and spaces are ignored during processing.

# Solution
```python test.py  -r 'python test.py'
<template>
def count_char_frequencies(s: str) -> None:
    '''
    Given a string, count the frequency of each alphanumeric character
    and print the frequencies sorted by character.

    Args:
    s: str - input string

    Output:
    Print the frequencies in the format 'character: frequency', one per line.
    '''
<sol> from collections import Counter

    # Filter alphanumeric characters and count frequencies
    freq = Counter(char for char in s if char.isalnum())

    # Sort and print the results
    for char in sorted(freq):
        print(f"{char}: {freq[char]}") </sol>
<suffix_invisible>
{% include './utils.py.jinja' %}
</suffix_invisible>
</template>
```

# Public Test Cases

## Input 1

```
hello world!
```

## Output 1

```
d: 1
e: 1
h: 1
l: 3
o: 2
r: 1
w: 1
```


## Input 2

```
aAaAA12345!!

```

## Output 2

```
1: 1
2: 1
3: 1
4: 1
5: 1
A: 3
a: 2

```

# Private Test Cases

## Input 1

```
123abc!@#ABC123

```

## Output 1

```
1: 2
2: 2
3: 2
A: 1
B: 1
C: 1
a: 1
b: 1
c: 1

```

## Input 2

```
aAaAaA  123
```

## Output 2

```
1: 1
2: 1
3: 1
A: 3
a: 3
```

## Input 3

```
  abc!!!123xyz!!ABC###999
```

## Output 3

```
1: 1
2: 1
3: 1
9: 3
A: 1
B: 1
C: 1
X: 1
Y: 1
Z: 1
a: 1
b: 1
c: 1
x: 1
y: 1
z: 1

```

## Input 4

```
N1!N2!N3#N4!N5#1234
```

## Output 4

```
1: 1
2: 1
3: 1
4: 2
5: 1
N: 5

```
