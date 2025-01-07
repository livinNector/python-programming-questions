## Problem Statement

You are required to implement a simple banking system. The bank details are stored in a **dictionary** named **BANK**, where the keys are `account number` and values are corresponding `account balance`. The banking system should consist of the following functions:
1. `create_account(acc_num)`: Creates a new account with the given acc_num and initializes the balance to 0. Returns "Account created successfully" if the account was created, or "Account Number already exists" if the account already exists
2. `check_balance(acc_num)`: Takes the `account number` as argument and returns the balance in that account.
3. `deposit(acc_num, amount)`: Takes `account number` and `amount` to be deposited as arguments and deposite the specified `amount` in the given `account number`. Return "Deposited Amount: ____, New Balance: ____" 
4. `withdraw(acc_num, amount)`: Takes `account number` and amount to be withdrawn as arguments and withdraws the specified `amount` from the given `account_number`. Returns "Withdrew Amount: ____, New balance: ____" or "Insufficient Balance" if the withdrawal amount exceeds the balance.
5. `Transaction(from_acc, to_acc, amount)`: Takes 3 arguments. First two are `account numbers` and third is the `amount`. The function transfers the amount specified from `from_acc` to `to_acc`. Returns "Transaction successfull" or "Insufficient Balance" if the `from_acc` does not have enough funds.

### Additional Instructions:
- For all functions, if the `acc_num` does not exist in the system, return "Account does not exist".
- If there is an invalid entry for `account number` or `amount`, return "Invalid Input".*

*The system must keep track of accounts in a dictionary where keys are account numbers and values are account balances. Each function must handle input validation.*

### Constraints:
- Account number will always be a positive integer greater than or equal to 10000.
- Amount to be deposited or withdrawn will always greater than or equal to 0.
- Balance will be a floating-poin number.
- The account number will be unique.

## Solution

```python
BANK = {}

def create_account(acc_num):
    if acc_num in BANK:
        return "Account Number already exists"
    BANK[acc_num] = 0.0
    return "Account created successfully"

def check_balance(acc_num):
    if acc_num not in BANK:
        return "Account does not exist"
    return BANK[acc_num]

def deposit(acc_num, amount):
    if acc_num not in BANK:
        return "Account does not exist"
    if amount <= 0:
        return "Invalid Input"
    BANK[acc_num] += amount
    return f"Deposited Amount: {amount}, New Balance: {BANK[acc_num]}"

def withdraw(acc_num, amount):
    if acc_num not in BANK:
        return "Account does not exist"
    if amount <= 0:
        return "Invalid Input"
    if BANK[acc_num] < amount:
        return "Insufficient Balance"
    BANK[acc_num] -= amount
    return f"Withdrew Amount: {amount}, New Balance: {BANK[acc_num]}"

def transaction(from_acc, to_acc, amount):
    if from_acc not in BANK or to_acc not in BANK:
        return "Account does not exist"
    if amount <= 0:
        return "Invalid Input"
    if BANK[from_acc] < amount:
        return "Insufficient Balance"
    BANK[from_acc] -= amount
    BANK[to_acc] += amount
    return f"Transaction successfull"
```

## Public Test Cases

### Test Case 1:
**Input:**
```
print(create_account(10001))
print(check_balance(10001))
print(deposit(10001, 500.0))
print(withdraw(10001, 200.0))
print(withdraw(10001, 400.0))
```
**Expected Output:**
```
Account created successfully
0.0
Deposited Amount: 500.0, New Balance: 500.0
Withdrew Amount: 200.0, New Balance: 300.0
Insufficient Balance
```

### Test Case 2:
**Input:**
```
print(create_account(10002))
print(deposit(10002, 1000.0))
print(withdraw(10002, 500.0))
print(transaction(10002, 10001, 200.0))
print(check_balance(10002))
print(check_balance(10001))
```
**Expected Output:**
```
Account created successfully
Deposited Amount: 1000.0, New Balance: 1000.0
Withdrew Amount: 500.0, New Balance: 500.0
Transaction successfull
300.0
500.0
```

## Private Test Cases

### Test Case 1:
**Input:**
```
print(create_account(10003))
print(deposit(10003, 1500.0))
print(withdraw(10003, 300.0))
print(transaction(10003, 10001, 200.0))
print(transaction(10001, 10003, 200.0))
print(check_balance(10003))
```
**Expected Output:**
```
Account created successfully
Deposited Amount: 1500.0, New Balance: 1500.0
Withdrew Amount: 300.0, New Balance: 1200.0
Transaction successfull
Transaction successfull
1200.0
```

### Test Case 2:
**Input:**
```
print(create_account(10004))
print(deposit(10004, 800.0))
print(withdraw(10004, 500.0))
print(withdraw(10004, 400.0))
print(transaction(10001, 10004, 200.0))
print(check_balance(10004))
```
**Expected Output:**
```
Account created successfully
Deposited Amount: 800.0, New Balance: 800.0
Withdrew Amount: 500.0, New Balance: 300.0
Insufficient Balance
Transaction successfull
500.0
```

### Test Case 3:
**Input:**
```
print(create_account(10005))
print(deposit(10005, 2000.0))
print(withdraw(10005, 300.0))
print(transaction(10005, 10001, 1800.0))
print(transaction(10001, 10005, 100.0))
print(check_balance(10005))
```
**Expected Output:**
```
Account created successfully
Deposited Amount: 2000.0, New Balance: 2000.0
Withdrew Amount: 300.0, New Balance: 1700.0
Insufficient balance
Transaction successfull
1800.0
```