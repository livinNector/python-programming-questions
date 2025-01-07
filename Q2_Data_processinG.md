---
title:  Data Processing in Python
tags: ['data processing', 'functional programming', 'filtering', 'mapping', 'aggregation', 'sorting', 'grouping', 'dictionary operations', 'list comprehensions', 'collections', 'functions', 'intermediate']

---

# Problem Statement

You are tasked with processing a list of products sold in a store. Each product is represented as a dictionary with the following keys: 

- `id` (int): A unique identifier for the product.
- `name` (str): The name of the product.
- `category` (str): The category of the product (e.g., "electronics", "furniture").
- `price` (float): The price of the product.
- `quantity_sold` (int): The total number of units sold.

Implement the following functions to process this data:

1. **`filter_by_price_range(products, min_price, max_price)`**  
   - Filters the products whose prices fall within the specified range `[min_price, max_price]`.  
   - Returns a list of matching product dictionaries.

2. **`map_to_names(products)`**  
   - Maps the list of products to a list of product names (`name` values).  
   - Returns a list of strings.

3. **`total_revenue(products)`**  
   - Calculates the total revenue for all products.  
   - Revenue is defined as `price * quantity_sold`.  
   - Returns a float representing the total revenue.

4. **`sort_by_quantity_sold(products, descending=False)`**  
   - Sorts the products by `quantity_sold` in ascending order by default. If `descending=True`, sorts them in descending order.  
   - Returns a list of sorted product dictionaries.

5. **`group_by_category(products)`**  
   - Groups the products by their `category`.  
   - Returns a dictionary where the keys are category names, and the values are lists of product dictionaries belonging to that category.

6. **`unique_categories(products)`**  
   - Extracts all unique categories present in the products list.  
   - Returns a set of unique category names.

7. **`average_price_by_category(products)`**  
   - Calculates the average price of products for each category.  
   - Returns a dictionary where the keys are category names, and the values are the average prices of products in that category.

---

# Solution
```python test.py  -r 'python test.py'
<template>
def filter_by_price_range(products, min_price, max_price):
    """
    Filters products based on a given price range.
    """
    <los>...</los>
<sol> 
    return [product for product in products if min_price <= product['price'] <= max_price]</sol>
def map_to_names(products):
    """
    Maps products to a list of their names.
    """
    <los>...</los>
    <sol>
    return [product['name'] for product in products]</sol>
def total_revenue(products):
    """
    Calculates the total revenue for all products.
    """
    <los>...</los>
    <sol>
    return sum(product['price'] * product['quantity_sold'] for product in products)</sol>
def sort_by_quantity_sold(products, descending=False):
    """
    Sorts products by the quantity sold.
    """     
    <los>...</los>  
<sol>
    return sorted(products, key=lambda product: product['quantity_sold'], reverse=descending) </sol>
def unique_categories(products):
    """
    Extracts unique categories from the list of products.
    """
    <los>...</los>
 <sol>
    return set({product['category'] for product in products})</sol>
def group_by_category(products):
    """
    Groups products by their category.
    """
    <los>...</los>
    <sol>
    from collections import defaultdict
    grouped = defaultdict(list)
    for product in products:
        grouped[product['category']].append(product)
    return dict(grouped) </sol>
def unique_categories(products):
    """
    Extracts unique categories from the list of products.
    """
    <los>...</los>
    <sol> 
    return set({product['category'] for product in products}) </sol>


def average_price_by_category(products):
    """
    Calculates the average price of products for each category.
    """
    <los>...</los>
    <sol>
    from collections import defaultdict
    category_totals = defaultdict(lambda: {'total_price': 0, 'count': 0})
    
    for product in products:
        category = product['category']
        category_totals[category]['total_price'] += product['price']
        category_totals[category]['count'] += 1
    
    return {category: totals['total_price'] / totals['count'] for category, totals in category_totals.items()} </sol>
</template>
<suffix_invisible>
{% include './utils.py.jinja' %}
</suffix_invisible>
```

# Public Test Cases

## Input 1

```
products = [
    {'id': 1, 'name': 'Laptop', 'category': 'electronics', 'price': 1000.0, 'quantity_sold': 5},
    {'id': 2, 'name': 'Chair', 'category': 'furniture', 'price': 150.0, 'quantity_sold': 10},
    {'id': 3, 'name': 'Headphones', 'category': 'electronics', 'price': 50.0, 'quantity_sold': 15},
    {'id': 4, 'name': 'Table', 'category': 'furniture', 'price': 300.0, 'quantity_sold': 3},
    {'id': 5, 'name': 'Smartphone', 'category': 'electronics', 'price': 700.0, 'quantity_sold': 8},
]

is_equal(
    map_to_names(products),
    ['Laptop', 'Chair', 'Headphones', 'Table', 'Smartphone']
)
is_equal(
    unique_categories(products),
    {'electronics', 'furniture'}
)

```

## Output 1

```
['Laptop', 'Chair', 'Headphones', 'Table', 'Smartphone']
{'electronics', 'furniture'}
```

## Input 2

```
products = [
    {'id': 101, 'name': 'Refrigerator', 'category': 'appliances', 'price': 1200.0, 'quantity_sold': 7},
    {'id': 102, 'name': 'Desk', 'category': 'furniture', 'price': 200.0, 'quantity_sold': 5},
    {'id': 103, 'name': 'Microwave', 'category': 'appliances', 'price': 300.0, 'quantity_sold': 12},
    {'id': 104, 'name': 'Sofa', 'category': 'furniture', 'price': 600.0, 'quantity_sold': 3},
    {'id': 105, 'name': 'Vacuum Cleaner', 'category': 'appliances', 'price': 400.0, 'quantity_sold': 9},
]

filtered_products = filter_by_price_range(products, 200, 600)
total = total_revenue(filtered_products)
is_equal(
    filtered_products,
    [{'id': 102, 'name': 'Desk', 'category': 'furniture', 'price': 200.0, 'quantity_sold': 5}, {'id': 103, 'name': 'Microwave', 'category': 'appliances', 'price': 300.0, 'quantity_sold': 12}, {'id': 104, 'name': 'Sofa', 'category': 'furniture', 'price': 600.0, 'quantity_sold': 3}, {'id': 105, 'name': 'Vacuum Cleaner', 'category': 'appliances', 'price': 400.0, 'quantity_sold': 9}]
)
is_equal(
    total,
    10000.0
)
```

## Output 2

```
[{'id': 102, 'name': 'Desk', 'category': 'furniture', 'price': 200.0, 'quantity_sold': 5}, {'id': 103, 'name': 'Microwave', 'category': 'appliances', 'price': 300.0, 'quantity_sold': 12}, {'id': 104, 'name': 'Sofa', 'category': 'furniture', 'price': 600.0, 'quantity_sold': 3}, {'id': 105, 'name': 'Vacuum Cleaner', 'category': 'appliances', 'price': 400.0, 'quantity_sold': 9}]
10000.0
```

## Input 3

```
products = [
    {'id': 101, 'name': 'Refrigerator', 'category': 'appliances', 'price': 1200.0, 'quantity_sold': 7},
    {'id': 102, 'name': 'Desk', 'category': 'furniture', 'price': 200.0, 'quantity_sold': 5},
    {'id': 103, 'name': 'Microwave', 'category': 'appliances', 'price': 300.0, 'quantity_sold': 12},
    {'id': 104, 'name': 'Sofa', 'category': 'furniture', 'price': 600.0, 'quantity_sold': 3},
    {'id': 105, 'name': 'Vacuum Cleaner', 'category': 'appliances', 'price': 400.0, 'quantity_sold': 9},
]

grouped = group_by_category(products)
averages = average_price_by_category(products)
is_equal(
    grouped,
    {'appliances': [{'id': 101, 'name': 'Refrigerator', 'category': 'appliances', 'price': 1200.0, 'quantity_sold': 7}, {'id': 103, 'name': 'Microwave', 'category': 'appliances', 'price': 300.0, 'quantity_sold': 12}, {'id': 105, 'name': 'Vacuum Cleaner', 'category': 'appliances', 'price': 400.0, 'quantity_sold': 9}], 'furniture': [{'id': 102, 'name': 'Desk', 'category': 'furniture', 'price': 200.0, 'quantity_sold': 5}, {'id': 104, 'name': 'Sofa', 'category': 'furniture', 'price': 600.0, 'quantity_sold': 3}]}

)
is_equal(
    averages,
    {'appliances': 633.3333333333334, 'furniture': 400.0}
)
```
## Output 3

```
{'appliances': [{'id': 101, 'name': 'Refrigerator', 'category': 'appliances', 'price': 1200.0, 'quantity_sold': 7}, {'id': 103, 'name': 'Microwave', 'category': 'appliances', 'price': 300.0, 'quantity_sold': 12}, {'id': 105, 'name': 'Vacuum Cleaner', 'category': 'appliances', 'price': 400.0, 'quantity_sold': 9}], 'furniture': [{'id': 102, 'name': 'Desk', 'category': 'furniture', 'price': 200.0, 'quantity_sold': 5}, {'id': 104, 'name': 'Sofa', 'category': 'furniture', 'price': 600.0, 'quantity_sold': 3}]}
{'appliances': 633.3333333333334, 'furniture': 400.0}
```

# Private Test Cases

## Input 1

```
products = [
    {'id': 1, 'name': 'Laptop', 'category': 'electronics', 'price': 1000.0, 'quantity_sold': 5},
    {'id': 2, 'name': 'Chair', 'category': 'furniture', 'price': 150.0, 'quantity_sold': 10},
    {'id': 3, 'name': 'Headphones', 'category': 'electronics', 'price': 50.0, 'quantity_sold': 15},
    {'id': 4, 'name': 'Table', 'category': 'furniture', 'price': 300.0, 'quantity_sold': 3},
    {'id': 5, 'name': 'Smartphone', 'category': 'electronics', 'price': 700.0, 'quantity_sold': 8},
]

is_equal(
    filter_by_price_range(products, 100, 500),
    [{'id': 2, 'name': 'Chair', 'category': 'furniture', 'price': 150.0, 'quantity_sold': 10}, {'id': 4, 'name': 'Table', 'category': 'furniture', 'price': 300.0, 'quantity_sold': 3}]
)
```

## Output 1

```
[{'id': 2, 'name': 'Chair', 'category': 'furniture', 'price': 150.0, 'quantity_sold': 10}, {'id': 4, 'name': 'Table', 'category': 'furniture', 'price': 300.0, 'quantity_sold': 3}]
```

## Input 2

```
products = [
    {'id': 101, 'name': 'Refrigerator', 'category': 'appliances', 'price': 1200.0, 'quantity_sold': 7},
    {'id': 102, 'name': 'Desk', 'category': 'furniture', 'price': 200.0, 'quantity_sold': 5},
    {'id': 103, 'name': 'Microwave', 'category': 'appliances', 'price': 300.0, 'quantity_sold': 12},
    {'id': 104, 'name': 'Sofa', 'category': 'furniture', 'price': 600.0, 'quantity_sold': 3},
    {'id': 105, 'name': 'Vacuum Cleaner', 'category': 'appliances', 'price': 400.0, 'quantity_sold': 9},
]

grouped = group_by_category(products)

is_equal(
    grouped,
    {'appliances': [{'id': 101, 'name': 'Refrigerator', 'category': 'appliances', 'price': 1200.0, 'quantity_sold': 7}, {'id': 103, 'name': 'Microwave', 'category': 'appliances', 'price': 300.0, 'quantity_sold': 12}, {'id': 105, 'name': 'Vacuum Cleaner', 'category': 'appliances', 'price': 400.0, 'quantity_sold': 9}], 'furniture': [{'id': 102, 'name': 'Desk', 'category': 'furniture', 'price': 200.0, 'quantity_sold': 5}, {'id': 104, 'name': 'Sofa', 'category': 'furniture', 'price': 600.0, 'quantity_sold': 3}]}
)
```

## Output 2

```
    {'appliances': [{'id': 101, 'name': 'Refrigerator', 'category': 'appliances', 'price': 1200.0, 'quantity_sold': 7}, {'id': 103, 'name': 'Microwave', 'category': 'appliances', 'price': 300.0, 'quantity_sold': 12}, {'id': 105, 'name': 'Vacuum Cleaner', 'category': 'appliances', 'price': 400.0, 'quantity_sold': 9}], 'furniture': [{'id': 102, 'name': 'Desk', 'category': 'furniture', 'price': 200.0, 'quantity_sold': 5}, {'id': 104, 'name': 'Sofa', 'category': 'furniture', 'price': 600.0, 'quantity_sold': 3}]}
```

## Input 3

```
products = [
    {'id': 101, 'name': 'Smartphone', 'category': 'electronics', 'price': 800.0, 'quantity_sold': 100},
    {'id': 102, 'name': 'Laptop', 'category': 'electronics', 'price': 1200.0, 'quantity_sold': 50},
    {'id': 103, 'name': 'Chair', 'category': 'furniture', 'price': 150.0, 'quantity_sold': 200},
    {'id': 104, 'name': 'Desk', 'category': 'furniture', 'price': 250.0, 'quantity_sold': 150}
]

# Mapping product names
names = map_to_names(products)

# Grouping products by category
grouped = group_by_category(products)

# Calculating total revenue
revenue = total_revenue(products)

is_equal(
    names,
    ['Smartphone', 'Laptop', 'Chair', 'Desk']
)

is_equal(
    grouped,
    {'electronics': [{'id': 101, 'name': 'Smartphone', 'category': 'electronics', 'price': 800.0, 'quantity_sold': 100}, {'id': 102, 'name': 'Laptop', 'category': 'electronics', 'price': 1200.0, 'quantity_sold': 50}], 'furniture': [{'id': 103, 'name': 'Chair', 'category': 'furniture', 'price': 150.0, 'quantity_sold': 200}, {'id': 104, 'name': 'Desk', 'category': 'furniture', 'price': 250.0, 'quantity_sold': 150}]}
)

is_equal(
    revenue,
    207500.0
)
```

## Output 3

```
['Smartphone', 'Laptop', 'Chair', 'Desk']
{'electronics': [{'id': 101, 'name': 'Smartphone', 'category': 'electronics', 'price': 800.0, 'quantity_sold': 100}, {'id': 102, 'name': 'Laptop', 'category': 'electronics', 'price': 1200.0, 'quantity_sold': 50}], 'furniture': [{'id': 103, 'name': 'Chair', 'category': 'furniture', 'price': 150.0, 'quantity_sold': 200}, {'id': 104, 'name': 'Desk', 'category': 'furniture', 'price': 250.0, 'quantity_sold': 150}]}
207500.0
```

## Input 4

```
products = [
    {'id': 101, 'name': 'Smartphone', 'category': 'electronics', 'price': 800.0, 'quantity_sold': 100},
    {'id': 102, 'name': 'Laptop', 'category': 'electronics', 'price': 1200.0, 'quantity_sold': 50},
    {'id': 103, 'name': 'Chair', 'category': 'furniture', 'price': 150.0, 'quantity_sold': 200},
    {'id': 104, 'name': 'Desk', 'category': 'furniture', 'price': 250.0, 'quantity_sold': 150}
]

# Sort products by quantity sold (descending)
sorted_by_quantity = sort_by_quantity_sold(products, descending=True)

# Calculate average price by category
avg_price = average_price_by_category(products)

is_equal(
    sorted_by_quantity,
    [{'id': 103, 'name': 'Chair', 'category': 'furniture', 'price': 150.0, 'quantity_sold': 200}, {'id': 104, 'name': 'Desk', 'category': 'furniture', 'price': 250.0, 'quantity_sold': 150}, {'id': 101, 'name': 'Smartphone', 'category': 'electronics', 'price': 800.0, 'quantity_sold': 100}, {'id': 102, 'name': 'Laptop', 'category': 'electronics', 'price': 1200.0, 'quantity_sold': 50}]

)

is_equal(
    avg_price,
    {'electronics': 1000.0, 'furniture': 200.0}
)
```

## Output 4

```
[{'id': 103, 'name': 'Chair', 'category': 'furniture', 'price': 150.0, 'quantity_sold': 200}, {'id': 104, 'name': 'Desk', 'category': 'furniture', 'price': 250.0, 'quantity_sold': 150}, {'id': 101, 'name': 'Smartphone', 'category': 'electronics', 'price': 800.0, 'quantity_sold': 100}, {'id': 102, 'name': 'Laptop', 'category': 'electronics', 'price': 1200.0, 'quantity_sold': 50}]
{'electronics': 1000.0, 'furniture': 200.0}
```