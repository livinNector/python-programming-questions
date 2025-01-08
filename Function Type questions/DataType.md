---
title : Data Type Operation
---
# Problem statement
Write a function data_type_operations that performs various operations on different data types.

The function should take the following inputs:

1. An integer num
2. A float decimal
3. A string text
4. A list lst
5. A dictionary dct
6. A set st

It should return a tuple of results as described below:

1. The square of the integer num.
2. The product of the float decimal with 2.5.
3. The string text reversed.
4. A new list obtained by appending the integer num to the list lst.
5. A dictionary where the key "new_key" is added with the value equal to the length of the string text.
6. A new set obtained by adding the float decimal to the set st.

**Example**

```python
data_type_operation(3, 4.2 , "hello" , [1,2,3] , {"key1" : 10} , {1,2,3}) # output (9, 10.5, "olleh", [1, 2, 3, 3], {'key1': 10, 'new_key': 5}, {1, 2, 3, 4.2})
```


#Solution

<prefix>  
# some prefix  
</prefix>  
<template>  
def data_type_operations(num: int, decimal: float, text: str, lst: list, dct: dict, st: set) -> tuple:  
    '''  
    Perform operations on various data types.  

    Arguments:  
    num: int - an integer  
    decimal: float - a float  
    text: str - a string  
    lst: list - a list  
    dct: dict - a dictionary  
    st: set - a set  

    Return: tuple - results of the operations described in the problem statement  
    '''  

    <los>...</los>  
    <sol>  
    # Perform operations
    result_1 = num ** 2  
    result_2 = decimal * 2.5  
    result_3 = text[::-1]  
    result_4 = lst + [num]  
    result_5 = {**dct, "new_key": len(text)}  
    result_6 = st | {decimal}  

    return result_1, result_2, result_3, result_4, result_5, result_6  
    </sol>  
</template>  
<suffix>  
# some suffix  
</suffix>  
<suffix_invisible>  
{% include '../function_type_and_check.py.jinja' %}  
</suffix_invisible>  

```

# Public Test Cases

## Input 1
```
is_equal(  
    data_type_operations(3, 4.2, "hello", [1, 2, 3], {"key1": 10}, {1, 2, 3}),  
    (9, 10.5, "olleh", [1, 2, 3, 3], {'key1': 10, 'new_key': 5}, {1, 2, 3, 4.2})  
)  


```

## Output 2
```
(9, 10.5, "olleh", [1, 2, 3, 3], {'key1': 10, 'new_key': 5}, {1, 2, 3, 4.2})  


```

## Input 2

```
is_equal(  
    data_type_operations(5, 1.1, "world", [4, 5], {}, {7}),  
    (25, 2.75, "dlrow", [4, 5, 5], {'new_key': 5}, {1.1, 7})  
)  


```

```
## Output 2
(25, 2.75, "dlrow", [4, 5, 5], {'new_key': 5}, {1.1, 7})
```

# Private test case

#Input 1
```
is_equal(  
    data_type_operations(2, 3.0, "abc", [10, 20], {"a": 1}, {5}),  
    (4, 7.5, "cba", [10, 20, 2], {"a": 1, "new_key": 3}, {3.0, 5})  
)
```

```
## Ouput 1 
(4, 7.5, "cba", [10, 20, 2], {"a": 1, "new_key": 3}, {3.0, 5}) 
```


## Input 2
```
is_equal(  
    data_type_operations(0, 0.0, "", [], {}, set()),  
    (0, 0.0, "", [0], {"new_key": 0}, {0.0})  
)  

```

```
## Output 2
(0, 0.0, "", [0], {"new_key": 0}, {0.0})
```
