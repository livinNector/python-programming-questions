---
title: String Manipulation - Split and Join
tags: ['strings', 'basic operations', 'split', 'join']
---

# Problem Statement

You are given a string `line` consisting of space-separated words. Your task is to split the string by spaces and then join the resulting words using a hyphen `-` as a delimiter.

Write a function `split_and_join(line: str) -> str` that takes a string as input and returns the resulting string where words are joined by `-`.

**Example**
```py3
split_and_join(this is a string) # this-is-a-string
split_and_join(my name is xyz)  #my-name-is-xyz
split_and_join(hello world) #hello-world
```

# Solution
```python test.py  -r 'python test.py'
<prefix>
  def split_and_join(line: str) -> str:
    '''
    Given a string, split using " ",and join using"-".

    Arguments:
    line: str - a string to split and join.

    Return: str - return the string joined using "-" after splitting using " ".
    '''
</prefix>
<template>
    return<sol> "-".join(line.split())</sol>
<suffix>
l = input()
print(split_and_join(l))
</suffix>
<suffix_invisible>
{% include './utils.py.jinja' %}
</suffix_invisible>
</template>
```

# Public Test Cases

## Input 1

```
is_equal(split_and_join("this is a string"),"this-is-a-string")

```

## Output 1

```
this-is-a-string

```


## Input 2

```
is_equal(split_and_join("hello world"),"hello-world")

```

## Output 2

```
hello-world

```


## Input 3

```
is_equal(split_and_join("python is fun"),"python-is-fun")

```

## Output 3

```
python-is-fun

```


# Private Test Cases

## Input 1

```
is_equal(split_and_join("learning python is awesome"),"learning-python-is-awesome")

```

## Output 1

```
learning-python-is-awesome

```

## Input 2
```

is_equal(split_and_join("split and join example"),"split-and-join-example")

```

## Output 2

```
split-and-join-example

```

## Input 3

```
is_equal(split_and_join("we are learning new skills"),"we-are-learning-new-skills")

```

## Output 3

```
we-are-learning-new-skills

```

## Input 4

```
is_equal(split_and_join("let's join and split words"),"let's-join-and-split-words")

```

## Output 4

```
let's-join-and-split-words

```

## Input 5

```
is-equal("split_and_join("string manipulation task"),"string-manipulation-task")

```

## Output 5

```
string-manipulation-task

```
