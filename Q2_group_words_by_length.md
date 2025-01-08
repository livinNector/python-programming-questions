---
title: Group Words by Length
---

# Problem Statement

Given a list of words, group them by their lengths and return a dictionary where the keys are the lengths, and the values are lists of words with that length.
**Example**
```
words = ["apple", "bat", "car", "door", "ant", "elephant"]

```
The output should be:
{3: ["bat", "car", "ant"], 5: ["apple"], 4: ["door"], 8: ["elephant"]}


# Solution

```py3 test.py -r 'python test.py'
<template>
def group_words_by_length(words: list) -> dict:
    '''
    Groups words by their lengths.

    Arguments:
    words: list - a list of strings.

    Return:
    dict - a dictionary with lengths as keys and lists of words as values.
    '''
    <los>...</los>
    <sol>
    from collections import defaultdict
    length_dict = defaultdict(list)
    for word in words:
        length_dict[len(word)].append(word)
    return dict(length_dict)
    </sol>
</template>

<suffix_invisible>
{% include '../function_type_and_is_equal_suffix.py.jinja' %}
</suffix_invisible>

```

# Public Test Cases

## Input 1

```
words = ["cat", "dog", "bird", "fish", "horse"]
is_equal(
    group_words_by_length(words),
    {3: ["cat", "dog"], 4: ["bird", "fish"], 5: ["horse"]}
)

```

## Output 1

```
{3: ["cat", "dog"], 4: ["bird", "fish"], 5: ["horse"]}

```

## Input 2

```
words = ["a", "to", "the", "quick", "brown", "fox"]
is_equal(
    group_words_by_length(words),
    {1: ["a"], 2: ["to"], 3: ["the"], 5: ["quick"], 4: ["brown", "fox"]}
)

```

## Output 2

```
{1: ["a"], 2: ["to"], 3: ["the"], 5: ["quick"], 4: ["brown", "fox"]}

```

# Private Test Cases

## Input 1

```
words = ["blue", "red", "yellow", "pink", "orange"]
is_equal(
    group_words_by_length(words),
    {4: ["blue", "pink"], 3: ["red"], 6: ["yellow"], 6: ["orange"]}
)

```

## Output 1

```
{4: ["blue", "pink"], 3: ["red"], 6: ["yellow", "orange"]}

```
