---
title: Data Processing I/O- Find Unique Words
tags: [aggregation, filtering, I/O, definite input]
---

# Problem Statement

Write a program that reads a paragraph from standard input and prints all unique words (case-insensitive) sorted alphabetically.

# Solution
```python test.py -r 'python test.py'
<template>
<sol>
text = input()
words = text.lower().replace('.', '').replace(',', '').replace('!', '').split()
unique = sorted(set(words))
for word in unique:
    print(word)
</sol>
</template>
```

# Public Test Cases

## Input 1
```
Hello world! Hello again.
```

## Output 1
```
again
hello
world
```

## Input 2
```
Python is great. Python is fun!
```

## Output 2
```
fun
great
is
python
```


# Private Test Cases


## Input 1
```
One fish, two fish, red fish, blue fish.
```

## Output 1
```
blue
fish
one
red
two
```

## Input 2
```
Hello, world! This is a test. Hello world.
```

## Output 2
```
a
hello
is
test
this
world
```