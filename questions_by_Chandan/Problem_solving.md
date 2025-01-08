---
title: Order Management System
tags: [application, problem-solving, functions, dictionary, list]
---

# Problem Statement

---

You are tasked to develop an **Order Management System** for a small business. Implement the following functions:

1. **`add_order(order_list, order_id, product, quantity)`**  
    - Description: Adds a new order to the `order_list`.  
    - Arguments:  
      - `order_list` (list): A list where each order is a dictionary.  
      - `order_id` (int): Unique ID for the order.  
      - `product` (str): Name of the product ordered.  
      - `quantity` (int): Quantity of the product ordered.  
    - Returns: Updated `order_list`.  
    - Example:  
      ```python
      add_order([], 101, 'Apple', 5)
      # Output: [{'order_id': 101, 'product': 'Apple', 'quantity': 5}]
      ```

2. **`update_order(order_list, order_id, new_quantity)`**  
    - Description: Updates the quantity of an existing order. If the order ID is not found, return "Order not found".  
    - Arguments:  
      - `order_list` (list): List of orders.  
      - `order_id` (int): ID of the order to update.  
      - `new_quantity` (int): Updated quantity for the order.  
    - Returns: Updated `order_list` or an error message.  
    - Example:  
      ```python
      update_order([{'order_id': 101, 'product': 'Apple', 'quantity': 5}], 101, 10)
      # Output: [{'order_id': 101, 'product': 'Apple', 'quantity': 10}]
      ```

3. **`delete_order(order_list, order_id)`**  
    - Description: Deletes an order from the `order_list` based on the order ID. If the order ID is not found, return "Order not found".  
    - Arguments:  
      - `order_list` (list): List of orders.  
      - `order_id` (int): ID of the order to delete.  
    - Returns: Updated `order_list` or an error message.  
    - Example:  
      ```python
      delete_order([{'order_id': 101, 'product': 'Apple', 'quantity': 5}], 101)
      # Output: []
      ```

4. **`get_order_summary(order_list)`**  
    - Description: Returns a summary of all orders, grouped by product, showing the total quantity for each product.  
    - Arguments:  
      - `order_list` (list): List of orders.  
    - Returns: A dictionary where keys are product names, and values are the total quantities.  
    - Example:  
      ```python
      get_order_summary([{'order_id': 101, 'product': 'Apple', 'quantity': 5}, {'order_id': 102, 'product': 'Apple', 'quantity': 3}, {'order_id': 103, 'product': 'Banana', 'quantity': 2}])
      # Output: {'Apple': 8, 'Banana': 2}
      ```

---

# Solution

```python
def add_order(order_list, order_id, product, quantity):
    order_list.append({'order_id': order_id, 'product': product, 'quantity': quantity})
    return order_list

def update_order(order_list, order_id, new_quantity):
    for order in order_list:
        if order['order_id'] == order_id:
            order['quantity'] = new_quantity
            return order_list
    return "Order not found"

def delete_order(order_list, order_id):
    for order in order_list:
        if order['order_id'] == order_id:
            order_list.remove(order)
            return order_list
    return "Order not found"

def get_order_summary(order_list):
    summary = {}
    for order in order_list:
        product = order['product']
        quantity = order['quantity']
        if product in summary:
            summary[product] += quantity
        else:
            summary[product] = quantity
    return summary
```
# Public Test Cases

## Input 1

```
order_list = []
order_list = add_order(order_list, 101, 'Apple', 5)
order_list = add_order(order_list, 102, 'Banana', 2)
order_list = update_order(order_list, 101, 10)
order_list = delete_order(order_list, 102)
summary = get_order_summary(order_list)
print(order_list)
print(summary)
```
## Output 1

```
[{'order_id': 101, 'product': 'Apple', 'quantity': 10}]
{'Apple': 10}
```

## Input 2

```
order_list = []
order_list = add_order(order_list, 201, 'Orange', 6)
order_list = add_order(order_list, 202, 'Apple', 3)
order_list = add_order(order_list, 203, 'Banana', 5)
order_list = update_order(order_list, 202, 8)
order_list = delete_order(order_list, 204)  # Invalid ID
summary = get_order_summary(order_list)
print(order_list)
print(summary)
```
## Output 2
```
[{'order_id': 201, 'product': 'Orange', 'quantity': 6}, {'order_id': 202, 'product': 'Apple', 'quantity': 8}, {'order_id': 203, 'product': 'Banana', 'quantity': 5}]
{'Orange': 6, 'Apple': 8, 'Banana': 5}
```

# Private Test Cases

## Input 1
```
order_list = []
order_list = add_order(order_list, 301, 'Milk', 2)
order_list = add_order(order_list, 302, 'Bread', 4)
order_list = add_order(order_list, 303, 'Milk', 3)
order_list = update_order(order_list, 302, 6)
order_list = delete_order(order_list, 304)  # Invalid ID
summary = get_order_summary(order_list)
print(order_list)
print(summary)
```

## Output 1
```
[{'order_id': 301, 'product': 'Milk', 'quantity': 2}, {'order_id': 302, 'product': 'Bread', 'quantity': 6}, {'order_id': 303, 'product': 'Milk', 'quantity': 3}]
{'Milk': 5, 'Bread': 6}
```

## Input 2
```
order_list = []
order_list = add_order(order_list, 401, 'Pencil', 10)
order_list = add_order(order_list, 402, 'Notebook', 5)
order_list = add_order(order_list, 403, 'Notebook', 7)
order_list = update_order(order_list, 401, 15)
order_list = delete_order(order_list, 402)
summary = get_order_summary(order_list)
print(order_list)
print(summary)
```
## Output 2
```
[{'order_id': 401, 'product': 'Pencil', 'quantity': 15}, {'order_id': 403, 'product': 'Notebook', 'quantity': 7}]
{'Pencil': 15, 'Notebook': 7}
```
