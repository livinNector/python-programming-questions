---
title: Basic Data Type Question
tags: ['array','int','float','dict','type-conversion','rounding-float','truncate']
---

# Problem Statement
## Implement the below function and do not use loops in the solution
**1. Find presence of allergen in a list of ingredients:**

    Given a list of Ingredients of a food product and an allergen. 
    Find out if the list of ingredients contains the allergen or not. 
    If the list contains the allergen return `True` else return `False`.
    

**Example**
```py3
Ingredients = ['Water','Soyabeans','Vitamin B12','Sugar']
Allergen = 'Soyabeans'
#returns True
```
```py3
Ingredients = ['mushroom','vinegar','soup thickener','sugar']
Allergen = 'peanuts'
#returns False
```
**2. Inches to Centimeter Calculator**
    Convert the length of a room measured in inches to centimeter and then truncate the decimal value.
    --| 1 inch = 2.54 centimeters |--
**Example**
```py3
inches_to_centi(1) #return 2
inches_to_centi(10) #return 20
inches_to_centi(-10) #return 0
```
**3. Min-Max-Avg of list of numbers**
    Find the `Minimum`,`Maximum` and `Avergae` of the list of numbers given and return a dictionary with the above as keys and their respected values.
    Note:- Round off the decimal to 2 places if necessary.
**Example**
```py3
stats([12, 45, 78, 23, 56, 89]) #returns "{'Average': 50.5, 'Maximum': 89 , 'Minimum': 12}"
stats([1.5, 2.5, 3.5, 4.5, 5.5]) #returns "{'Average': 3.5 , 'Maximum': 5.5, 'Minimum': 1.5}"
stats([100]) #returns "{'Average': 100, 'Maximum': 100, 'Minimum': 100}"
```
# Solution
```python test.py  -r 'python test.py'
<prefix>
# do not use loops for this problem.
</prefix>
<template>
def find_allergen_presence(ingredients:list,allergen:str)->bool:
    <los>...</los>
    <sol>return (allergen in ingredients)</sol>
def inches_to_centi(inches:float)->int:
    <los>...</los>
    <sol>
    if inches<=0:
        return 0

    return int(inches*2.54)
    </sol>
def stats(numbers: list) -> dict:
    <los>...</los>
    <sol>
    if not numbers:  
        return {"Minimum": None, "Maximum": None, "Average": None}
    
    return {
        "Minimum": min(numbers),
        "Maximum": max(numbers),
        "Average": round(sum(numbers) / len(numbers), 2)  
    }
    </sol>

</template>

<suffix_invisible>
{% include '../util.py.jinja' %}
</suffix_invisible>
```

# Public Test Cases

## Input 1

```
ingredients_list = ['milk', 'eggs', 'fish', 'Crustacean shellfish']
allergen = 'milk'
is_equal(find_allergen_presence(ingredients_list,allergen),True)

inches = 1
is_equal(inches_to_centi(inches),2)

numbers = [12, 45, 78, 23, 56, 89]
is_equal(order_repr(stats(numbers)),"{'Average': 50.5, 'Maximum': 89, 'Minimum': 12}")


check_for_loops_in_solution(inches_to_centi,find_allergen_presence,stats)
```

## Output 1

```
True
2
"{'Average': 50.5, 'Maximum': 89, 'Minimum': 12}"
```


## Input 2

```
ingredients_list = ['tree nuts', 'peanuts', 'wheat','soybeans']
allergen = 'Alcohol'
is_equal(find_allergen_presence(ingredients_list,allergen),False)

inches = 10
is_equal(inches_to_centi(inches),25)

numbers = [1.5, 2.5, 3.5, 4.5, 5.5]
is_equal(order_repr(stats(numbers)),"{'Average': 3.5, 'Maximum': 5.5, 'Minimum': 1.5}")

check_for_loops_in_solution(inches_to_centi,find_allergen_presence,stats)
```

## Output 2

```
False
25
"{'Average': 3.5, 'Maximum': 5.5, 'Minimum': 1.5}"
```


## Input 3

```
ingredients_list = ["Sugar", "Salt", "Butter", "Almond"]
allergen = "Almond"
is_equal(find_allergen_presence(ingredients_list,allergen),True)

inches = -10
is_equal(inches_to_centi(inches),0)

numbers = [100]
is_equal(order_repr(stats(numbers)),"{'Average': 100.0, 'Maximum': 100, 'Minimum': 100}")

check_for_loops_in_solution(inches_to_centi,find_allergen_presence,stats)
```

## Output 3

```
True
0
"{'Average': 100.0, 'Maximum': 100, 'Minimum': 100}"

```





# Private Test Cases

## Input 1

```
ingredients_list = ["Milk", "Eggs", "Peanuts", "Soy", "Wheat"]
allergen = "Peanuts"
is_equal(find_allergen_presence(ingredients_list,allergen),True)

inches = 45.8
is_equal(inches_to_centi(inches),116)


numbers = [-5, -10, 0, 5, 10]
is_equal(order_repr(stats(numbers)),"{'Average': 0.0, 'Maximum': 10, 'Minimum': -10}")

check_for_loops_in_solution(inches_to_centi,find_allergen_presence,stats)
```

## Output 1

```
True
116
"{'Average': 0.0, 'Maximum': 10, 'Minimum': -10}"

```

## Input 2

```
ingredients_list = []
allergen = "Milk"
is_equal(find_allergen_presence(ingredients_list,allergen),False)

inches = 100
is_equal(inches_to_centi(inches),254)

numbers = []
is_equal(order_repr(stats(numbers)),"{'Average': None, 'Maximum': None, 'Minimum': None}")

check_for_loops_in_solution(inches_to_centi,find_allergen_presence,stats)

```

## Output 2

```
False
254
"{'Average': None, 'Maximum': None, 'Minimum': None}"

```


