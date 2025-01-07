## Problem Statement

Write a function `Intro(F_name: str, L_name: str, height: float, weight: float) -> str` that:
1. Takes four parameters:
   - `F_name`: First name (string).
   - `L_name`: Last name (string).
   - `height`: Height in meters (float).
   - `weight`: Weight in kilograms (float).
   
2. Returns a string of the form: `"Hi, my name is XY and my BMI is __"` where:
   - `X` is the first character of `F_name`.
   - `Y` is the first character of `L_name`.
   - BMI is calculated using the formula: `BMI = weight / (height ** 2)`.

## Solution

```python
def Intro(F_name: str, L_name: str, height: float, weight: float) -> str:
    bmi = weight / (height ** 2)
    return f"Hi, my name is {F_name[0]}{L_name[0]} and my BMI is {bmi:.2f}"
```

## Public Test Cases

### Test Case 1:
**Input:**
```python
("John", "Doe", 1.75, 70)
```
**Expected Output:**
```
Hi, my name is JD and my BMI is 22.86
```

### Test Case 2:
**Input:**
```python
("Alice", "Smith", 1.60, 55)
```
**Expected Output:**
```
Hi, my name is AS and my BMI is 21.48
```

## Private Test Cases

### Test Case 1:
**Input:**
```python
("James", "Bond", 1.83, 80)
```
**Expected Output:**
```
Hi, my name is JB and my BMI is 23.88
```

### Test Case 2:
**Input:**
```python
("Mark", "Ruffalo", 1.73, 72)
```
**Expected Output:**
```
Hi, my name is MR and my BMI is 24.06
```

### Test Case 3:
**Input:**
```python
("Chris", "Evans", 1.80, 85)
```
**Expected Output:**
```
Hi, my name is CE and my BMI is 26.23
```

### Test Case 4:
**Input:**
```python
("Henry", "Cavill", 1.85, 92)
```
**Expected Output:**
```
Hi, my name is HC and my BMI is 26.88
```


