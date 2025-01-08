---
title: Organize the Shipment Inventory
---

# Problem Statement

You are managing a shipment inventory for a logistics company. The inventory is represented as a dictionary where each key is a product name (string), and the value is another dictionary containing the following details:
- **Quantity**: An integer representing the number of items available.
- **Price**: An integer representing the price per item.

Your task is to write a function `organize_inventory` that processes this dictionary and organizes it as a list of tuples, each containing:
- Product name (string)
- Quantity (integer)
- Price (integer)
- Total value (integer)

The returned list must meet the following criteria:
- Sorted in descending order of total value, calculated as `Quantity * Price`.
- If two products have the same total value, sorted alphabetically by their product names in ascending order.

The inventory may also contain products with missing or invalid data. The function should:
- Exclude any products with missing `Quantity` or `Price` values.
- Treat invalid (negative or zero) `Quantity` or `Price` values as zero and exclude those products from the result.

### Function Signature
```python
def organize_inventory(inventory: dict) -> list:
    pass
```

### Input
- `inventory`: A dictionary where keys are product names (strings) and values are dictionaries with `Quantity` and `Price` as keys.

### Output
- A list of tuples, where each tuple contains the product name, its quantity, price, and total value.

### Example Input
```python
inventory = {
    "Widget": {"Quantity": 10, "Price": 15},
    "Gadget": {"Quantity": 5, "Price": 30},
    "Tool": {"Quantity": 20, "Price": 10},
    "Faulty": {"Quantity": 0, "Price": 50},
    "Device": {"Quantity": -5, "Price": 30},
    "Incomplete": {"Price": 20}
}
```

### Example Output
```python
[
    ("Tool", 20, 10, 200),
    ("Gadget", 5, 30, 150),
    ("Widget", 10, 15, 150)
]
```

# Solution

```py3 solution.py -r 'python solution.py'
<template>
def organize_inventory(inventory: dict) -> list:
    '''
    Organize the shipment inventory by total value and product name.

    Arguments:
    inventory: dict - A dictionary where keys are product names and values are dictionaries containing Quantity and Price.

    Returns:
    A list of tuples sorted by total value (descending) and product name (ascending).
    '''
    inventory_list = []

    for product in inventory:
        details = inventory[product]
        quantity = details.get("Quantity", 0)
        price = details.get("Price", 0)

        if quantity <= 0 or price <= 0:
            continue

        total_value = quantity * price
        inventory_list.append((product, quantity, price, total_value))

    for i in range(len(inventory_list) - 1):
        for j in range(len(inventory_list) - i - 1):
            if (inventory_list[j][3] < inventory_list[j + 1][3]) or (
                inventory_list[j][3] == inventory_list[j + 1][3] and inventory_list[j][0] > inventory_list[j + 1][0]
            ):
                inventory_list[j], inventory_list[j + 1] = inventory_list[j + 1], inventory_list[j]

    return inventory_list
</template>
```

# Public Test Cases

## Input 1
```
inventory = {
    "Widget": {"Quantity": 10, "Price": 15},
    "Gadget": {"Quantity": 5, "Price": 30},
    "Tool": {"Quantity": 20, "Price": 10},
    "Faulty": {"Quantity": 0, "Price": 50},
    "Device": {"Quantity": -5, "Price": 30},
    "Incomplete": {"Price": 20}
}
organize_inventory(inventory)
```

## Output 1
```
[
    ("Tool", 20, 10, 200),
    ("Gadget", 5, 30, 150),
    ("Widget", 10, 15, 150)
]
```

## Input 2
```
inventory = {
    "Chair": {"Quantity": 15, "Price": 20},
    "Table": {"Quantity": 10, "Price": 25},
    "Desk": {"Quantity": 8, "Price": 50},
    "Broken": {"Quantity": -3, "Price": 50},
    "Missing": {"Quantity": 10}
}
organize_inventory(inventory)
```

## Output 2
```
[
    ("Desk", 8, 50, 400),
    ("Table", 10, 25, 250),
    ("Chair", 15, 20, 300)
]
```

# Private Test Cases

## Input 1
```
inventory = {
    "Box": {"Quantity": 10, "Price": 10},
    "Crate": {"Quantity": 20, "Price": 5},
    "Bag": {"Quantity": 15, "Price": 8},
    "Damaged": {"Quantity": 0, "Price": 10}
}
organize_inventory(inventory)
```

## Output 1
```
[
    ("Bag", 15, 8, 120),
    ("Box", 10, 10, 100),
    ("Crate", 20, 5, 100)
]
```

## Input 2
```
inventory = {
    "Bolt": {"Quantity": 25, "Price": 4},
    "Nut": {"Quantity": 50, "Price": 2},
    "Screw": {"Quantity": 30, "Price": 3},
    "Invalid": {"Quantity": -10, "Price": 5}
}
organize_inventory(inventory)
```

## Output 2
```
[
    ("Bolt", 25, 4, 100),
    ("Nut", 50, 2, 100),
    ("Screw", 30, 3, 90)
]
```
