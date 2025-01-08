---
title: Problem Solving Question
tags: ['tic-tac-toe', 'file-handling','tsv','logic-building','loops']
---

# Problem Statement
## Tic-Tac-Toe Winner
    Two players `A` and `B` wanted to decide who is cooking tonight's dinner.So they played 80 tic-tac-toe games to decide it. 
    You are given a file with records of past games, now it is time to decide the winner. Consider the rules below.

        > X was chosen by player A
        > O was chosen by player B
        > - represents an empty cell
        
    the file `tic-tac-toe.tsv` has a record of 80 games played between A and B.The format is tab seperated values.
    Each row in the file represents a tic-tac-toe board.
    

    find the overall winner and the number of times he/she has won, return this in a tuple.if there is a draw between players return both the players and their corresponding win count.

**example**

```XXXOOX---  represents a board```   
``` 
    |X X X|
    |O O X|
    |- - -|
```                          
# Solution
```python test.py  -r 'python test.py'

<template>
#implement the function determine_overall_winner in the code below
<sol>
import csv

def check_winner(board):
    """Check who won in a given tic-tac-toe board."""
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)              
    ]
    
    for i, j, k in win_conditions:
        if board[i] == board[j] == board[k] and board[i] in ("X", "O"):
            return board[i]  
    
    return None  

def determine_overall_winner(filename="C:\\Users\\vinee\\OneDrive\\Documents\\GitHub\\python-programming-questions\\Q4\\tic-tac-toe.tsv"):

    
    wins_A = 0
    wins_B = 0
    
    with open(filename, "r") as file:
        reader = csv.reader(file, delimiter="\t")
          
        
        for row in reader:
            winner = check_winner(row)
            if winner == "X":
                wins_A += 1
            elif winner == "O":
                wins_B += 1
    
   
    if wins_A > wins_B:
        return ("A", wins_A)
    elif wins_B > wins_A:
        return ("B", wins_B)
    else:
        return ("A", wins_A, "B", wins_B)  







</sol>
</template>
<suffix>
#driver code

print(determine_overall_winner())

</suffix>

```
# Public Test Cases

## Input 1

```

```

## Output 1

```
('A', 73)
```

# Private Test Cases

## Input 1

```

```

## Output 1

```
('A', 73)
```


