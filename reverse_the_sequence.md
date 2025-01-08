---
title: Reverse the sequence 
---

# Problem Statement

Given a sequence of integers as input that terminates with a 0, create a recursive function to print the sequence in reverse order.

**Note:** Don't use lists or other data structures.

**Input Format:** A sequence of integers, one per line and ends with 0.

**Output Format:** The sequence of integers in reverse order, one per line.

**Sample Input**
```
1
2
3
0
```
**Sample Output**
```
0
3
2
1
```

# Solution
```python test.py  -r 'python test.py'
<prefix>
def reverse() -> None:
    '''
    Print the sequence of integers
    in reverse order.
    '''
</prefix>
<template>
<sol>
    n = int(input())
    if n != 0:
        reverse()
    print(n)
</sol>
</template>
<suffix>
reverse()
</suffix>
```

# Public Test Cases

## Input 1

```
1
2
3
0
```

## Output 1

```
0
3
2
1
```


## Input 2

```
8
7
2
3
1
4
5
0
```

## Output 2

```
0
5
4
1
3
2
7
8
```


## Input 3

```
1
0
```

## Output 3

```
0
1
```


# Private Test Cases

## Input 1

```
0
```

## Output 1

```
0
```

## Input 2

```
1
2
3
4
5
6
7
8
9
0
```

## Output 2

```
0
9
8
7
6
5
4
3
2
1
```
