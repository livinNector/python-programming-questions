---
title: Sorting Dictionary by Keys and Values with Multiple Functions
tags: ['dictionary', 'sorting', 'reverse', 'flter']
---

# Problem Statement
Write multiple functions to perform operations on a dictionary:

1. **`sort_dict_by_keys`**: Sorts the dictionary by its keys in ascending order.
2. **`sort_dict_by_values`**: Sorts the dictionary by its values in ascending order.
3. **`reverse_dict`**: Reverses the keys and values in the dictionary.
4. **`filter_dict`**: Filters the dictionary based on a threshold value for its values.
---

## Example Usage
```plaintext
# Input dictionary
sample_dict = {'z': 3, 'a': 10, 'm': 7, 'k': 1}

# Sort by keys
sort_dict_by_keys(sample_dict) ➞ {'a': 10, 'k': 1, 'm': 7, 'z': 3}

# Sort by values
sort_dict_by_values(sample_dict) ➞ {'k': 1, 'z': 3, 'm': 7, 'a': 10}

# Reverse keys and values
reverse_dict(sample_dict) ➞ {3: 'z', 10: 'a', 7: 'm', 1: 'k'}

# Filter by values greater than 5
filter_dict(sample_dict, 5) ➞ {'a': 10, 'm': 7}
```

# Solution
```python operations_on_dictionary.py  -r 'python operations_on_dictionary.py'
<prefix>
# some prefix
</prefix>
<template>
<sol
def sort_dict_by_keys(d: dict) -> dict:
    """
    Sorts the dictionary by keys in ascending order.

    Arguments:
    d: dict - The dictionary to be sorted.

    Returns:
    dict - A dictionary sorted by keys.
    """
    return dict(sorted(d.items()))</sol>

def sort_dict_by_values(d: dict) -> dict:
    """
    Sorts the dictionary by values in ascending order.

    Arguments:
    d: dict - The dictionary to be sorted.

    Returns:
    dict - A dictionary sorted by values.
    """
    return dict(sorted(d.items(), key=lambda item: item[1]))

def reverse_dict(d: dict) -> dict:
    """
    Reverses the keys and values in the dictionary.

    Arguments:
    d: dict - The dictionary to be reversed.

    Returns:
    dict - A dictionary with keys and values swapped.
    """
    return {v: k for k, v in d.items()}

def filter_dict(d: dict, threshold: int) -> dict:
    """
    Filters the dictionary based on a threshold value for its values.

    Arguments:
    d: dict - The dictionary to be filtered.
    threshold: int - The threshold value.

    Returns:
    dict - A dictionary containing items with values greater than the threshold.
    """
    return {k: v for k, v in d.items() if v > threshold}</sol>

</template>
<suffix>
# some suffix
</suffix>


```

# Public Test Cases

## Input 1
```python
sort_dict_by_keys({'b': 5, 'a': 3, 'c': 1})
```

## Output 1
```plaintext
{'a': 3, 'b': 5, 'c': 1}
```

## Input 2
```python
sort_dict_by_values({'x': 10, 'y': 2, 'z': 5})
```

## Output 2
```plaintext
{'y': 2, 'z': 5, 'x': 10}
```

## Input 3
```python
reverse_dict({'apple': 1, 'banana': 2, 'cherry': 3})
```

## Output 3
```plaintext
{1: 'apple', 2: 'banana', 3: 'cherry'}
```

# Private Test Cases

## Input 1
```python
filter_dict({'a': 4, 'b': 10, 'c': 2}, 3)
```

## Output 1
```plaintext
{'a': 4, 'b': 10}
```

## Input 2
```python
sort_dict_by_keys({'mango': 20, 'apple': 30, 'banana': 10})
```

## Output 2
```plaintext
{'apple': 30, 'banana': 10, 'mango': 20}
```

## Input 3
```python
sort_dict_by_values({'p': 8, 'q': 6, 'r': 10})
```

## Output 3
```plaintext
{'q': 6, 'p': 8, 'r': 10}
```

## Input 4
```python
reverse_dict({'key1': 100, 'key2': 200, 'key3': 300})
```

## Output 4
```plaintext
{100: 'key1', 200: 'key2', 300: 'key3'}
```

## Input 5
```python
filter_dict({'x': 5, 'y': 15, 'z': 10}, 10)
```

## Output 5
```plaintext
{'y': 15}
