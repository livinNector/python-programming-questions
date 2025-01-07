## Problem Statement

Write a function `group_by_first_letter(words: list) -> dict` which takes a list of words as its argument. The function should **return** a **dictionary** where:
- The **keys** of the dictionary are the first letters of ther words.
- The **values** are lists of words starting with the letter the corresponding **key**.
- Words in each list should **sorted** in **ascending alphabetical order**
 
 ### Constraints
 - The input list will only contain strings.
 - Words will be lowercase alphabets only (No special characters or numbers.)
 - The list may contain duplicate words.

 ## Solution

```python
def group_by_first_letter(words: list) -> dict:
    grouped = {}
    for word in words:
        f_letter = word[0]
        if f_letter not in grouped:
            grouped[f_letter] = []
        grouped[first_letter].append(word)
    
    #sorting each list of words
    for key in grouped:
        grouped[key].sort()
    
    return grouped
```

## Public Test Cases

### Test Case 1:
**Input:**
```python
['apple', 'banana', 'ant', 'blueberry', 'cherry']
```
**Expected Output:**
```python
{'a': ['ant', 'apple'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
```

### Test Case 2:
**Input:**
```python
["dog", "cat", "deer", "antelope", "apple", "car"]
```
**Expected Output:**
```python
{'d': ['deer', 'dog'], 'c': ['car', 'cat'], 'a': ['antelope', 'apple']}
```

## Private Test Cases

### Test Case 1:
**Input:**
```python
["zoo", "zebra", "apple", "ant", "ant", "zebra",  "antelope"]
```
**Expected Output:**
```python
{'z': ['zebra', 'zebra', 'zoo'], 'a': ['ant', 'ant', 'antelope', 'apple']}
```

### Test Case 2:
**Input:**
```python
["kiwi", "kale", "kangaroo", "apple", "ant", "banana", "caulifla"]
```
**Expected Output:**
```python
{'k': ['kale', 'kangaroo', 'kiwi'], 'a': ['ant', 'apple'], 'b': ['banana'], 'c': ['caulifla']}
```

### Test Case 3:
**Input:**
```python
["carrot", "cucumber", "celery", "date", "dragonfruit", "gogeta", "gojo"]
```
**Expected Output:**
```python
{'c': ['carrot', 'celery', 'cucumber'], 'd': ['date', 'dragonfruit'], 'g': ['gogeta', 'gojo']}
```

### Test Case 4:
**Input:**
```python
["pine", "pear", "pomegranate", "peach", "plum"]
```
**Expected Output:**
```python
{'p': ['peach', 'pear', 'pine', 'plum', 'pomegranate']}
```

