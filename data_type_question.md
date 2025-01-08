---
title: Data Type Operations
tags: ['python', 'data-types', 'strings', 'lists', 'dictionaries', 'sets', 'type-conversion']
---
# Problem Statement
Implement a function `transform_data(num, text, items)` that performs the following operations:

1. Takes three parameters:
   - `num`: An integer or float
   - `text`: A string
   - `items`: A list of elements

2. The function should:
   - Convert the number to its absolute value and round it to 2 decimal places
   - Convert the text to uppercase and remove any leading/trailing spaces
   - Convert the list into a set to remove duplicates, then back to a sorted list
   - Create a dictionary with three keys:
     - 'number': processed number
     - 'text': processed text
     - 'items': processed list
   
3. Return the resulting dictionary

Example:
```python
Input: transform_data(-15.3267, "  Hello world  ", [1, 3, 2, 1, 4, 2])
Output: {'number': 15.33, 'text': 'HELLO WORLD', 'items': [1, 2, 3, 4]}
```

# Solution
```python test.py  -r 'python3 test.py'
<prefix>
def transform_data(num, text, items):
</prefix>
<template>
<sol>
    # Process the number
    processed_num = round(abs(num), 2)
    
    # Process the text
    processed_text = text.strip().upper()
    
    # Process the list
    processed_items = sorted(list(set(items)))
    
    # Create and return the dictionary
    return {
        'number': processed_num,
        'text': processed_text,
        'items': processed_items
    }
</sol>
</template>
<suffix>
num = float(input())
text = input()
items = eval(input())
result = transform_data(num, text, items)
print(result)
</suffix>
<suffix_invisible>
</suffix_invisible>
```

# Public Test Cases
## Input 1
```
-15.3267
  Hello world  
[1, 3, 2, 1, 4, 2]
```
## Output 1
```
{'number': 15.33, 'text': 'HELLO WORLD', 'items': [1, 2, 3, 4]}
```
## Input 2
```
42.0
   Python  
[5, 5, 5, 5]
```
## Output 2
```
{'number': 42.0, 'text': 'PYTHON', 'items': [5]}
```

# Private Test Cases
## Input 1
```
-0.0056
  ALREADY upper  
[10, 20, 30, 20, 10]
```
## Output 1
```
{'number': 0.01, 'text': 'ALREADY UPPER', 'items': [10, 20, 30]}
```
## Input 2
```
789.98765
   spaces   everywhere   
[]
```
## Output 2
```
{'number': 789.99, 'text': 'SPACES   EVERYWHERE', 'items': []}
```
## Input 3
```
-123456.789
NoSpaces
[1, 2, 3, 2, 1]
```
## Output 3
```
{'number': 123456.79, 'text': 'NOSPACES', 'items': [1, 2, 3]}
```
## Input 4
```
0.0
   
[9, 8, 7, 8, 9]
```
## Output 4
```
{'number': 0.0, 'text': '', 'items': [7, 8, 9]}
```