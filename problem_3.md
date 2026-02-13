---
title: City Temperatures
---

# Problem Statement

Write a program that reads city temperatures from stdin. The input contains lines of the format <city> <temperature>. Print the average temperature and the name of the city with the highest temperature(no two cities have highest temperature). Input ends when an empty line is encountered.

**Example**
```
Input:
Delhi 30
Mumbai 35
Chennai 33

Output:
Average Temperature: 32.67
City with Highest Temperature: Mumbai
```

# Solution

```py3 test.py -r 'python test.py'
<template>
import sys

def main():
    '''
    Calculate the average temperature and find the city with the highest temperature.

    Input: Reads lines containing '<city> <temperature>'. Ends on an empty line.
    Output: Prints average temperature and city with highest temperature.
    '''
    <los>...</los>
    <sol>
    lines = sys.stdin.read().strip().split('\n')
    data = [line.split() for line in lines if line]
    cities = [d[0] for d in data]
    temps = [float(d[1]) for d in data]

    avg_temp = round(sum(temps) / len(temps), 2)
    highest_temp_city = cities[temps.index(max(temps))]

    print(f"Average Temperature: {avg_temp}")
    print(f"City with Highest Temperature: {highest_temp_city}")
    </sol>
</template>
<suffix_invisible>
{% include '../function_type_and_modify_check_suffix.py.jinja' %}
</suffix_invisible>
```

# Public Test Cases

## Input 1

```
NYC 20
London 25
Berlin 22
```

## Output 1

```
Average Temperature: 22.33
City with Highest Temperature: London
```

# Private Test Cases

## Input 1

```
Delhi 27
Bhopal 24
Indore 21
```

## Output 1

```
Average Temperature: 24.00
City with Highest Temperature: Delhi
```
