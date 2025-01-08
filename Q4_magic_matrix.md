---
title:Magic Matrix Finder
---

# Problem Statement
A magic matrix is a square matrix where the sum of every row, column, and both diagonals is the same. Your task is to write a program that determines if the given matrix is a magic matrix.

You need to implement the following functions:

# Functions to Implement

**is_square_matrix(matrix: List[List[int]]) -> bool**

Input: A list of lists matrix, where each sublist represents a row of the matrix.
Output: Returns True if the matrix is square (i.e., the number of rows equals the number of columns), otherwise False.

**is_magic_matrix(matrix: List[List[int]]) -> bool**

Input: A list of lists matrix, where each sublist represents a row of the matrix.
Output: Returns True if the matrix is a magic matrix, otherwise False. A magic matrix is a square matrix where the sum of each row, column, and both diagonals is the same.

**Example**
```
Input: matrix = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]


```
Output : True


# Solution

<template>
from typing import List

def is_square_matrix(matrix: List[List[int]]) -> bool:
    """
    Checks if the given matrix is square.
    """
    return len(matrix) == len(matrix[0])

def is_magic_matrix(matrix: List[List[int]]) -> bool:
    """
    Determines if the given matrix is a magic matrix.
    """
    if not is_square_matrix(matrix):
        return False
    
    n = len(matrix)
    
    # Calculate the sum of the first row (this will be the magic sum)
    magic_sum = sum(matrix[0])
    
    # Check sum of rows
    for row in matrix:
        if sum(row) != magic_sum:
            return False
    
    # Check sum of columns
    for col in range(n):
        col_sum = sum(matrix[row][col] for row in range(n))
        if col_sum != magic_sum:
            return False
    
    # Check sum of diagonals
    diag1_sum = sum(matrix[i][i] for i in range(n))
    diag2_sum = sum(matrix[i][n - 1 - i] for i in range(n))
    
    if diag1_sum != magic_sum or diag2_sum != magic_sum:
        return False
    
    return True

# Input handling (for testing purposes only)
if __name__ == "__main__":
    # Read the matrix input
    n = int(input("Enter the size of the matrix: "))
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    # Check if the matrix is magic
    if is_magic_matrix(matrix):
        print("True")
    else:
        print("False")
</template>


```

# Public Test Cases

## Input 1

```
matrix = [
    [8, 1, 6],
    [9, 5, 7],
    [4, 9, 2]
]


```

## Output 1

```
False

```

## Input 2

```
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

```

## Output 2

```
True

```

## Input 3

```
matrix = [
    [8, 1, 6],
    [3, 5, 7]
]


```

## Output 3

```
False

```

# Private Test Cases

## Input 1

```
matrix = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]
]


```

## Output 1

```
True

```
