---
title: Calculate Total Billing Amount
---

# Problem Statement

You are given a dictionary `price_list` where the keys are product IDs (strings) and the values are the prices of the corresponding products (integers). You are also given a dictionary `order` where the keys are product IDs (strings) and the values are the quantities of the corresponding products (integers).

Write a function `calculate_total` that takes these two dictionaries as input and returns the total bill amount by summing up the product of the price and quantity for all items in the order.

If a product ID in `order` is not found in `price_list`, its price should be considered as 0.

**Example**
```python
price_list = {'p1': 100, 'p2': 200, 'p3': 150} order = {'p1': 2, 'p3': 1, 'p4': 3} calculate_total(price_list, order)
# Output:
# 350
In this example, `p1` contributes 200 (2 x 100), `p3` contributes 150 (1 x 150), and `p4` contributes 0 (not in price_list).

```


# Solution
```py3 test.py -r 'python test.py'
<template>
def calculate_total(price_list: dict, order: dict) -> int:
    '''
    Given the price list and order details, calculate the total billing amount.

    Arguments:
    price_list: dict - A dictionary where keys are product IDs and values are prices.
    order: dict - A dictionary where keys are product IDs and values are quantities.

    Return: int - Total bill amount.
    '''
    <sol>
    total = 0
    for product_id, quantity in order.items():
        price = price_list.get(product_id, 0)
        total += price * quantity
    return total
    </sol>
</template>
<suffix_invisible>
{% include '../function_type_and_modify_check_suffix.py.jinja' %}
</suffix_invisible>
```

# Public Test Cases

## Input 1

```
price_list = {'p1': 50, 'p2': 30, 'p3': 20}
order = {'p1': 3, 'p2': 4}
is_equal(
    calculate_total(price_list, order),
    290
)

```

## Output 1

```
290

```


## Input 2

```
price_list = {'a': 10, 'b': 20}
order = {'a': 1, 'c': 2}
is_equal(
    calculate_total(price_list, order),
    10
)

```

## Output 2

```
10

```


# Private Test Cases

## Input 1

```
price_list = {'x': 100, 'y': 200, 'z': 300}
order = {'x': 1, 'y': 2, 'z': 1}
is_equal(
    calculate_total(price_list, order),
    800
)

price_list = {'p1': 45, 'p2': 60, 'p3': 70}
order = {'p2': 5, 'p3': 2}
is_equal(
    calculate_total(price_list, order),
    430
)

price_list = {'a': 10}
order = {'b': 3}
is_equal(
    calculate_total(price_list, order),
    0
)

```

## Output 1

```
800
430
0

```
