---
title: LCM HCF
tags: ['LCM', 'HCF', 'GCD', 'Function', 'Input Output', 'loop']
---

# Problem Statement
Create a program that will find LCM and HCF of 2 or more numbers.

LCM:
Lowest common multiple (or least common multiple)

e.g. Find LCM of [6,12,15,30]

lcm(6,12) = 12
lcm(12,15) = 60
lcm(60,30) = 60

=> lcm([6,12,15,30]) = 60


HCF:
Highest common factor (or Greatest common divisor)

e.g. Find HCF of [6,12,15,30]

hcf(6,12) = 6
hcf(6,15) = 3
hcf(3,30) = 3

=> hcf([6,12,15,30]) = 3

For simplicity, you may assume that:
User will always give you atlest 2 integers before giving 'done'.
User either give you +ve interger or 'done', noting else. 
It simply means you don't need error-handling here.


# Solution
```python test.py  -r 'python test.py'
<prefix>

</prefix>
<template>
def hcf(a, b):
    '''
    Write a function to find hcf of two numbers a and b
    '''
<sol>
    while b != 0:
        a, b = b, a % b
    return a
</sol>

def lcm(a, b):
    '''
    write a function to find lcm of two numbers a and b
    '''
<sol>
    return (a * b) // hcf(a, b)
</sol>

def lcm_of_list(numbers):
    '''
    Use lcm of two numbers function to find lcm of all the numbers in that list
    '''
<sol>
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
    return result
</sol>

def hcf_of_list(numbers):
    '''
    Use hcf of two numbers to find hcf of all numbers in list
    '''
<sol>
    result = numbers[0]
    for num in numbers[1:]:
        result = hcf(result, num)
    return result
</sol>

'''
create a list numbers and keep appending all the numbers user enteres to it until user enters "done" 
'''

'''
use lcm_of_list and hcf_of_list functions to find lcm and hcf of all numbers in list "numbers"
'''

<sol>
numbers = []

while True:
    user_input = input().strip()
    if user_input.lower() == 'done':
        break
    numbers.append(int(user_input))
</sol>


print(lcm_of_list(numbers))
print(hcf_of_list(numbers))


</template>
<suffix>

</suffix>
<suffix_invisible>

</suffix_invisible>
```

# Public Test Cases

## Input 1

```
6
9
done
```

## Output 1

```
18
3
```

## Input 2

```
24
36
18
done
```

## Output 2

```
72
6
```

## Input 3

```
24    
36
18
48
done
```

## Output 3

```
144
6
```

# Private Test Cases

## Input 1

```
3
5
10
12
done
```

## Output 1

```
60
1
```

## Input 2

```
3
1
done
```

## Output 2

```
3
1
```

## Input 3

```
15    
105
85
40
done
```

## Output 3

```
14280
5
```

