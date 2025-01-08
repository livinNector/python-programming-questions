---
title: Basic Data types
tags: [truncation,float,string_functions,type_checking,Basic Data Types]
---

# Problem Statement

---

You need to implement the following functions:

1. **`float_truncate(d)`**  
   - Description: This function accepts a float and truncates it to an integer, then returns the result.  
   - Example:  
     ```python
     float_truncate(10.9)  # Output: 10
     float_truncate(-5.7)  # Output: -5
     ```

2. **`is_it_integer(d)`**  
   - Description: This function accepts any data type and returns a boolean indicating whether the input is an integer.  
   - Example:  
     ```python
     is_it_integer(5)  # Output: True
     is_it_integer("Hello")  # Output: False
     is_it_integer(3.14)  # Output: False
     ```

3. **`Reverse_str(s)`**  
   - Description: This function accepts a string and returns the reversed version of the string. You should not use loops to achieve this.  
   - Example:  
     ```python
     Reverse_str("hello")  # Output: "olleh"
     Reverse_str("Python")  # Output: "nohtyP"
     ```

4. **`Max_set(s)`**  
   - Description: This function accepts a set `s` and returns the maximum element from the set.  
   - Example:  
     ```python
     Max_set({1, 2, 3, 4})  # Output: 4
     Max_set({-10, -5, -1})  # Output: -1
     ```

5. **`List_sum(l)`**  
   - Description: This function accepts a list `l` and returns the sum of all elements in the list. You should not use loops.  
   - Example:  
     ```python
     List_sum([1, 2, 3])  # Output: 6
     List_sum([10, -5, 7])  # Output: 12
     ```

6. **`Dict_keys_find(d)`**  
   - Description: This function accepts a dictionary `d` and returns a list of all the keys in the dictionary.  
   - Example:  
     ```python
     Dict_keys_find({"a": 1, "b": 2})  # Output: ["a", "b"]
     Dict_keys_find({"name": "Alice", "age": 25})  # Output: ["name", "age"]
     ```

# Solution

```py3 test.py -r 'python test.py'
<template>
def float_truncate(d:float)->int:
    '''
    Given a float truncate to an integer by removing the Decimal Part
    
    Argument:
    d: a float number
    Return int - float number truncated
    '''
    <los>...</los>
    <sol>
    return int(d)</sol>
def Max_set(d:set)->int:
    '''
    Given a set of numbers, return the maximum element in the set.
    
    Argument:
    d: a set of numbers
    Return:
    int: the maximum element in the set
    '''
    <los>...</los>
    <sol>
    return max(d)</sol>
def is_it_integer(d)-> bool : 
    '''
    Given any data type, check if it is an integer.
    
    Argument:
    d: any data type
    Return:
    bool: True if d is an integer, False otherwise
    ''' 
    <los>...</los> 
    <sol>
    return type(d) == int </sol>
def Reverse_str(s:str)->str:
    '''
    Given a string, return its reversed version.
    
    Argument:
    s: a string
    Return:
    str: the reversed string
    '''
    <los>...</los>
    <sol>
    return s[::-1] </sol>
def List_sum(l:list)->int:
    '''
    Given a list of numbers, return the sum of all elements in the list.
    
    Argument:
    l: a list of numbers
    Return:
    int: the sum of all elements in the list
    '''
    <los>...</los>
    <sol>
    return sum(l) </sol>
def Dict_keys_find(d:dict)->list: 
    '''
    Given a dictionary, return all the keys in the dictionary as a list.
    
    Argument:
    d: a dictionary
    Return:
    list: a list of keys from the dictionary
    ''' 
    <los>...</los>   
    <sol>
    return list(d.keys())   
    </sol>        
</template>
<suffix>

</suffix>
<suffix_invisible>
{% include '../function_type_and_modify_check_suffix.py.jinja' %}
</suffix_invisible>
```

# Public Test Cases

## Input 1

```
d = 7.6
is_equal(
    float_truncate(d), 
    7
)

d = "Hello"
is_equal(
    is_it_integer(d), 
    False
)

is_equal(
    Reverse_str("Python"), 
    'nohtyP'
)

s = {1, 2, 3, 4}
is_equal(
    Max_set(s), 
    4
)

l = [1, 2, 3, 4]
is_equal(
    List_sum(l), 
    10
)

d = {"name": "Alice", "age": 25}
is_equal(
    Dict_keys_find(d), 
    ['name', 'age']
)

```

## Output 1

```
7
False
'nohtyP'
4
10
['name', 'age']

```

## Input 2

``` 
d = 3.14
is_equal(
    float_truncate(d),
    3
)

d = 5
is_equal(
    is_it_integer(d), 
    True
)

is_equal(
    Reverse_str("world"), 
    'dlrow'
)

s = {10, 20, 30}
is_equal(
    Max_set(s),
    30
)

is_equal(
    List_sum([5, 10, 15]),
    30
)

d = {"name": "Alice", "age": 25}
is_equal(
    Dict_keys_find(d),
    ['name', 'age']
)

```

## Output 2

```
3
True
'dlrow'
30
30
['name', 'age']

```

## Input 3

```
d = 16.9
is_equal(
    float_truncate(d),
    16
)

d = [1, 2, 3]
is_equal(
    is_it_integer(d),
    False
)

is_equal(
    List_sum([5, 10, 15]),
    30
)

d = {"fruit": "apple", "color": "red"}
is_equal(
    Dict_keys_find(d),
    ['fruit', 'color']
)

```

## Output 3

```
16
False
30
['fruit', 'color']

```

# Private Test Cases

## Input 1

```
d = 8.2
is_equal(
    float_truncate(d),
    8
)

d = 'Python'
is_equal(
    is_it_integer(d), 
    False
)

is_equal(
    List_sum([10,20,30,40,50]),
    150
)

is_equal(
    Max_set({1,2,3,4,5}), 
    5
)

is_equal(
    Reverse_str('Amit'),
    'timA'
)

d = {'one':1, 'two':2, 'three': 3}
is_equal(
    Dict_keys_find(d), 
    ['one', 'two', 'three']
)

```


## Output 1

```
8
False
150
5
'timA'
['one', 'two', 'three']

```