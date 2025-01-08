---
title: Decode Matrix Script
tags: ['matrix', 'decoding', 'regex', 'string manipulation']
---

# Problem Statement

Neo has a complex matrix script represented as a \( r x c \) grid of strings. The script contains alphanumeric characters, spaces, and symbols (!, @, #, $, %, &).  

To decode the script, Neo reads the matrix column-wise (top-to-bottom, left-to-right). Neo must connect the alphanumeric characters in the order they appear. If any symbols or spaces are present between two alphanumeric characters, they must be replaced with a single space `' '` to enhance readability.  
  

### Input Format
1. The first line contains two space-separated integers \( r \) (rows) and \( c \) (columns), respectively.
2. The next \( r \) lines each contain a string of length \( c \).

### Constraints
- \( 0 < r, c <= 100 \)  
- The matrix script contains only alphanumeric characters, spaces, and symbols (!, @, #, $, %, &).  

### Output Format
Print the decoded matrix script.

# Solution
```python test.py  -r 'python test.py'
<template>
def decode_matrix_script(r: int, c: int, matrix: list) -> str:
 '''
 Decodes the given matrix script by reading column-wise and replacing
 symbols or spaces between alphanumeric characters with a single space.

 Args:
 r: int - number of rows.
 c: int - number of columns.
 matrix: list - list of strings representing the matrix.

 Returns:
 str - the decoded matrix script.
 '''
<sol> transposed = ''.join([matrix[i][j] for j in range(c) for i in range(r)])
    
    # Step 2: Process the transposed string
    result = []
    last_char_alphanumeric = False
    
    for char in transposed:
        if char.isalnum():
            if not last_char_alphanumeric and result and result[-1] != ' ':
                result.append(' ')
            result.append(char)
            last_char_alphanumeric = True
        else:
            last_char_alphanumeric = False
    
    return ''.join(result).strip() </sol>
<suffix_invisible>
{% include './utils.py.jinja' %}
</suffix_invisible>
</template>
```

# Public Test Cases

## Input 1

```
7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!

```

## Output 1

```
This is Matrix#  %!

```


## Input 2

```
4 5
Neois
@Cool
$Cool
@@@@@

```

## Output 2

```
Neo is Cool Cool

```


# Private Test Cases

## Input 1

```
2 2
A@
!B

```

## Output 1

```
A B

```

## Input 2

```
3 6
Hello@
!#@%Co
Python

```

## Output 2

```
Hello Co Python

```

## Input 3

```
4 4
abcd
!!!! 
#### 
1234

```

## Output 3

```
a b c d 1 2 3 4

```

## Input 4

```
5 5
A   @
  B # 
C   ! 
  D $ 
E   % 

```

## Output 4

```
A B C D E

```

