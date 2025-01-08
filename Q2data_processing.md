---
title: Determine Top Product by Sales
tags: ['sorting', 'data processing', 'sales']
---

# Problem Statement
Write a function `top_selling_product` that processes a list of tuples containing product names and their sales. The function should:

1. Sort the products by their sales in descending order.
2. In case of a tie, choose the product that comes first alphabetically.
3. Return the name of the top-selling product.

### Input
A list of tuples where each tuple contains:
- `product_name` (str): The name of the product.
- `sales` (int): The total sales of the product.

### Output
A string containing the name of the top-selling product.

# Solution
```python test.py -r 'python test.py'
<prefix>

</prefix>
<template>
def top_selling_product(sales_data):
    '''
    Determine the top-selling product based on sales data.
    
    Arguments:
    sales_data: list of tuples - [(product_name (str), sales (int))]
    
    Returns:
    str - The name of the top-selling product.
    '''
    <los>...</los>
    <sol>
    # Sort products by sales in descending order and by name alphabetically
    sorted_data = sorted(sales_data, key=lambda x: (-x[1], x[0]))
    return sorted_data[0][0]  # Return the product name with the highest sales
    </sol>
</template>
<suffix>
input_data = input().strip()
sales_data = eval(input_data)
result = top_selling_product(sales_data)
print(result)
</suffix>
<suffix_invisible>

</suffix_invisible>
```
# Public Test Cases

## Input 1

```
[('ProductA', 150), ('ProductB', 200), ('ProductC', 200)]
```

## Output 1

```
ProductB
```


## Input 2

```
[('Alpha', 300), ('Beta', 300), ('Gamma', 250)]
```

## Output 2

```
Alpha
```


## Input 3

```
[('WidgetX', 400), ('WidgetY', 100), ('WidgetZ', 400)]
```

## Output 3

```
WidgetX
```



# Private Test Cases

## Input 1

```
[('Item1', 50), ('Item2', 75), ('Item3', 75)]
```

## Output 1

```
Item2
```

## Input 2

```
[('Phone', 500), ('Laptop', 500), ('Tablet', 300)]
```

## Output 2

```
Laptop
```

## Input 3

```
[('Chair', 10), ('Table', 15), ('Desk', 15)]
```

## Output 3

```
Desk
```

