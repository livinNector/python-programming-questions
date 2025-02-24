---
title: Process License Plate into state, RTO code, series, unique id
tags: ['dict', 'I/O', 'list slicing','loop','multiple inputs']
---

# Problem Statement

User inputs license-plates. Process these license-plates and **print a list of dictionaries** with keys as:
1. `state`: (str) two letters which indicates the State or Union Territory in which the vehicle is registered.
2. `RTO code`: (int) a two-digit number allocated to a district RTO(s) within the respective state or Union Territory.
3. `series`: (str) 1 or 2 letter; show the ongoing registration series of respective RTO
4. `unique id` (int) between 1 and 9999; unique to each registration.

Input preconditions: 
- 1st: number of lines of input (no. of license-plates inputted)
- 2nd line onwards license-plate in the format `TN 12 L 2421`. Press enter if multiple license-plates.

# Solution
```python test.py  -r 'python test.py'
<prefix>
num = int(input()) 
license_plates = []
for _ in range(num):
    license_plates.append(input().strip())
</prefix>
<template>
<sol>
outlist = []
for license_plate in license_plates:
    parts = license_plate.split()
    
    license_dict = {
        "state": parts[0],
        "RTO code": int(parts[1]),
        "series": parts[2],
        "unique id": int(parts[3])
    }
    outlist.append(license_dict)
print(outlist)
</sol>
<los>print()</los>
</template>
```

# Public Test Cases

## Input 1

```
5
MH 12 L 2039
MH 12 LQ 2930
KA 13 ZJ 4567
TN 08 B 7890
DL 09 X 1023
```

## Output 1

```python
[{'state': 'MH', 'RTO code': 12, 'series': 'L', 'unique id': 2039}, {'state': 'MH', 'RTO code': 12, 'series': 'LQ', 'unique id': 2930}, {'state': 'KA', 'RTO code': 13, 'series': 'ZJ', 'unique id': 4567}, {'state': 'TN', 'RTO code': 8, 'series': 'B', 'unique id': 7890}, {'state': 'DL', 'RTO code': 9, 'series': 'X', 'unique id': 1023}]
```

## Input 2

```
3
KA 10 AB 1234
MH 05 XY 5678
TN 03 PQ 9999
```

## Output 2

```python
[{'state': 'KA', 'RTO code': 10, 'series': 'AB', 'unique id': 1234}, {'state': 'MH', 'RTO code': 5, 'series': 'XY', 'unique id': 5678}, {'state': 'TN', 'RTO code': 3, 'series': 'PQ', 'unique id': 9999}]
```


# Private Test Cases

## Input 1

```
0
```

## Output 1

```python
[]
```
