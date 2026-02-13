---
title: Problem-Solving: Expense Tracker
---

# Problem Statement

Design an expense tracker application that allows users to:

1. **Add an expense**: Record an expense with a category and amount.
2. **Remove an expense**: Remove a specific expense by its ID.
3. **Get total expenses**: Return the total amount of expenses.

You need to implement the following functions:

- `add_expense(expenses: list, category: str, amount: float) -> dict`: Adds a new expense with a unique ID.
- `remove_expense(expenses: list, expense_id: int) -> list`: Removes an expense by its ID.
- `total_expenses(expenses: list) -> float`: Returns the total amount of all expenses.

**Example**
```
expenses = []
expenses = add_expense(expenses, "Food", 50.0)
expenses = add_expense(expenses, "Transport", 30.0)
expenses = remove_expense(expenses, 1)
print(total_expenses(expenses))  # Output: 30.0
```

# Solution

```py3 test.py -r 'python test.py'
<template>
def add_expense(expenses: list, category: str, amount: float) -> dict:
    '''
    Add a new expense to the list with a unique ID.

    Arguments:
    expenses: list - List of existing expenses.
    category: str - Category of the expense.
    amount: float - Amount of the expense.

    Return: dict - Newly added expense.
    '''
    <los>...</los>
    <sol>
    expense_id = len(expenses) + 1
    expense = {"id": expense_id, "category": category, "amount": amount}
    expenses.append(expense)
    return expenses  </sol>

def remove_expense(expenses: list, expense_id: int) -> list:
    '''
    Remove an expense from the list by its ID.

    Arguments:
    expenses: list - List of existing expenses.
    expense_id: int - ID of the expense to remove.

    Return: list - Updated list of expenses.
    '''
    <los>...</los>
    <sol>
    expenses = [expense for expense in expenses if expense["id"] != expense_id]
    return expenses  </sol>

def total_expenses(expenses: list) -> float:
    '''
    Calculate the total amount of all expenses.

    Arguments:
    expenses: list - List of existing expenses.

    Return: float - Total expenses.
    '''
    <los>...</los>
    <sol>
    return sum(expense["amount"] for expense in expenses)  </sol>

</template>
<suffix_invisible>
{% include '../function_type_and_modify_check_suffix.py.jinja' %}
</suffix_invisible>
```

# Public Test Cases

## Input 1

```
expenses = []
expenses = add_expense(expenses, "Food", 50.0)
expenses = add_expense(expenses, "Travel", 100.0)
is_equal(
    total_expenses(expenses),
    150.0
)
expenses = remove_expense(expenses, 1)
is_equal(
    total_expenses(expenses),
    100.0
)
```

## Output 1

```
150.0
100.0
```

# Private Test Cases

## Input 1

```
expenses = []
expenses = add_expense(expenses, "Utilities", 80.0)
expenses = add_expense(expenses, "Groceries", 120.0)
expenses = add_expense(expenses, "Entertainment", 60.0)
is_equal(
    total_expenses(expenses),
    260.0
)
expenses = remove_expense(expenses, 2)
is_equal(
    total_expenses(expenses),
    140.0
)
```

## Output 1

```
260.0
140.0
```
