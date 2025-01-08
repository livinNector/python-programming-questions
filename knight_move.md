---
title: Knight Move
---

# Problem Statement

In a game of chess, the knight moves like the letter L. It can move two cells horizontally and one cell vertically, or two cells vertically and one cells horizontally. Given two different cells of the chessboard, create a function that determines whether a knight can go from the first cell to the second in one move.
The function receives as input, four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The function should return `True` if a knight can go from the first cell to the second in one move, or `False` otherwise.

**Input Format:** A sequence of 4 integers, one per line, indicating the initial and final coordinates of the knight.

**Output Format:** `True` if the maneuver is possible or `False` otherwise.

## Sample Input
```
2
4
3
2
```
## Sample Output
```
True
```

# Solution
```python test.py  -r 'python test.py'
<prefix>
def knight_move(x1: int, y1: int, x2: int, y2: int) -> bool:
    '''
    Return True if the knight can move from
    the first to the second coordinate
    
    Otherwise return False
    '''
</prefix>
<template>
<sol>
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    if dx == 1 and dy == 2 or dx == 2 and dy == 1:
        return True
    else:
        return False
</sol>
</template>
<suffix>
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
print(knight_move(x1, y1, x2, y2))
</suffix>
```

# Public Test Cases

## Input 1

```
1
1
1
4
```

## Output 1

```
False
```


## Input 2

```
1
1
8
8
```

## Output 2

```
False
```


## Input 3

```
2
4
3
2
```

## Output 3

```
True
```


## Input 4

```
5
2
4
4
```

## Output 4

```
True
```


## Input 5

```
2
8
3
7
```

## Output 5

```
False
```


# Private Test Cases

## Input 1

```
2
8
3
5
```

## Output 1

```
False
```

## Input 2

```
5
5
3
7
```

## Output 2

```
False
```

## Input 3

```
2
4
2
5
```

## Output 3

```
False
```

## Input 4

```
4
7
6
6
```

## Output 4

```
True
```

## Input 5

```
4
5
2
4
```

## Output 5

```
True
```
