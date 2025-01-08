---
title: Data processing Question
tags: ['map','filter','tuple','sorting','expression','ord','chr','']
---

# Problem Statement
## Implement the following function code 

    If suppose you are given an `sentence` in an english language and an arbitrary ASCII value `k`.
    Sort and return the sentence based on the ASCII value of the characters. 
    Now say let `x` be the count of charcters that are below or equal to k and `y` be the count of characters above k.
    return the sorted sentence along with the expression`x^2+y^2` in a tuple.

Note: Use ord() function to get the ASCII value of a character.

**example**
```py3
sentence = "The quick brown fox jumps over the lazy dog"
k = 111
data_processing(sentence,k) #returns ('        Tabcdeeefghhijklmnoooopqrrstuuvwxyz',1069)

sentence = "IITM_is_a_prestigious_institue"
k = 96
data_processing(sentence,k) #returns ("IIMT____aeegiiiiinoprsssstttuu",548)
```
# Solution
```python test.py  -r 'python test.py'
<prefix>
#Do not use loops in the solution.
</prefix>
<template>
def chr_to_ascii_map(chr_list:list)->list:
    <sol>
    ascii = list(map(lambda x: ord(x),chr_list))
    return ascii
    </sol>
def ascii_to_char_map(ascii_list:list)->list:
    <sol>
    char = list(map(lambda x: chr(x),ascii_list))
    return char
    </sol>
def ascii_less_than_or_eq_k(ascii_list:list,k:int)->int:
    <sol>
    af = filter(lambda x : x<=k,ascii_list)
    af = list(af)
    res = len(af)
    return res
    </sol>
def ascii_greater_than_k(ascii_list:list,k:int)->int:
    <sol>
    af = filter(lambda x : x>k,ascii_list)
    af = list(af)
    res = len(af)
    return res
    </sol>
def ascii_sorted_string(ascii_list:list)->str:
    <sol>
    ascii_list.sort()
    ch = ascii_to_char_map(ascii_list)
    from functools import reduce
    res = str(reduce(lambda x,y : x+y,ch))
    return res
    </sol>

def data_processing(sentence:str,k:int)->tuple:
    <sol>
    sen_list = list(sentence)
    ascii_sen_list = chr_to_ascii_map(sen_list)
    sorted_string = ascii_sorted_string(ascii_sen_list)
    ascii_sen_list = chr_to_ascii_map(sen_list)
    x = ascii_less_than_or_eq_k(ascii_sen_list,k)
    ascii_sen_list = chr_to_ascii_map(sen_list)
    y = ascii_greater_than_k(ascii_sen_list,k)
    res = x**2+y**2
    return (sorted_string,res)
    </sol>


</template>

<suffix_invisible>
{% include '../util.py.jinja' %}
</suffix_invisible>
```

# Public Test Cases

## Input 1

```
sentence = "The quick brown fox jumps over the lazy dog"
k = 111
is_equal(data_processing(sentence,k),('        Tabcdeeefghhijklmnoooopqrrstuuvwxyz',1069))

check_for_loops_in_solution(chr_to_ascii_map,data_processing,ascii_sorted_string,ascii_greater_than_k,ascii_less_than_or_eq_k,ascii_to_char_map)

```

## Output 1

```
('        Tabcdeeefghhijklmnoooopqrrstuuvwxyz', 1069)
```


## Input 2

```
sentence = "IITM_is_a_prestigious_institue"
k = 96
is_equal(data_processing(sentence,k),('IIMT____aeegiiiiinoprsssstttuu', 548)) 
check_for_loops_in_solution(chr_to_ascii_map,data_processing,ascii_sorted_string,ascii_greater_than_k,ascii_less_than_or_eq_k,ascii_to_char_map)
```

## Output 2
```
('IIMT____aeegiiiiinoprsssstttuu', 548)
```


# Private Test Cases

## Input 1

```
sentence = "hello world"
k = 110
is_equal(data_processing(sentence,k),(' dehllloorw', 65))
check_for_loops_in_solution(chr_to_ascii_map,data_processing,ascii_sorted_string,ascii_greater_than_k,ascii_less_than_or_eq_k,ascii_to_char_map)
```

## Output 1

```
(' dehllloorw', 65)

```

## Input 2

```
sentence = "Sorting123"
k = 100
is_equal(data_processing(sentence,k),('123Sginort', 52))
check_for_loops_in_solution(chr_to_ascii_map,data_processing,ascii_sorted_string,ascii_greater_than_k,ascii_less_than_or_eq_k,ascii_to_char_map)

```

## Output 2

```
('123Sginort', 52)

```

## Input 3

```
sentence = "Python is Fun!"
k = 105
is_equal(data_processing(sentence,k),('  !FPhinnostuy', 98))
check_for_loops_in_solution(chr_to_ascii_map,data_processing,ascii_sorted_string,ascii_greater_than_k,ascii_less_than_or_eq_k,ascii_to_char_map)

```

## Output 3

```
('  !FPhinnostuy', 98)

```


