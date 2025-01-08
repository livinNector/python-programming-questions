---
title: Daily shop records
tags: [aggregation, filtering, I/O, definite input]
---

# Problem Statement
You are provided with a list of dictionaries where each dictionary contains information about a shopper, including their name, age, and a dictionary of items they have bought, with item names as keys and quantities as values.

Return a dictionary having the format: 
{
&emsp;"shoppers": list of names,
&emsp;"filtered_by_age": Shoppers above the given age filter,
&emsp;"average_age": Average age of shoppers,
&emsp;"sorted_shoppers": Shoppers sorted by age,
&emsp;"items_group": Group shopper names by items bought,
&emsp;"unique_items": Set of unique items bought from the shop
}

# Solution
```python test.py -r 'python test.py'
<prefix>
# some prefix   
</prefix>
<template>
def process_shoppers(shoppers: list[dict], age_filter: int) -> dict:
    '''
    Write a function process_shoppers(shoppers, age_filter) that takes the inputs 
    and returns a list of dictionaries containing records after performing basic aggregation 
    and filtering operations and result dictionary must be in the given format.

    Arguments:
    shoppers: list[dict]
    age_filter: int

    Return: a dictionary in the form {
                "shoppers": list of names,
                "filtered_by_age": Shoppers above the given age filter,
                "average_age": Average age of shoppers,
                "sorted_shoppers": Shoppers sorted by age,
                "items_group": Group shopper names by items bought,
                "unique_items": Set of unique items bought from the shop
            }
    '''
    
    <los>...</los>
    <sol>
    names = [shopper['name'] for shopper in shoppers]
    
    filtered_shoppers = [shopper['name'] for shopper in shoppers if shopper['age'] > age_filter]
    
    ages = [shopper['age'] for shopper in shoppers]
    average_age = sum(ages)/len(ages)
    
    sorted_shoppers = sorted(shoppers, key=lambda x: x['age'])
    
    items_group = dict()
    for shopper in shoppers:
        for item in shopper['items_bought']:
            if item not in items_group.keys():
                items_group[item] = []
            items_group[item].append(shopper['name'])
    
    unique_items = set()
    for shopper in shoppers:
        unique_items.update(shopper['items_bought'].keys())
    
    # Returning all results as a dictionary
    return {
        "shoppers": names,
        "filtered_by_age": filtered_shoppers,
        "average_age": average_age,
        "sorted_shoppers": sorted_shoppers,
        "items_group": dict(items_group),
        "unique_items": unique_items
    }
    </sol>
    test = <los>...</los><sol>'test'</sol> #tests
</template>
<suffix>
# some suffix
</suffix>
<suffix_invisible>
{% include '../function_type_and_modify_check_suffix.py.jinja' %}
</suffix_invisible>
```

# Public Test Cases

## Input 1
```
shoppers = [
    {"name": "Alice", "age": 25, "items_bought": {"Apples": 3, "Bananas": 5}},
    {"name": "Bob", "age": 35, "items_bought": {"Oranges": 2, "Milk": 1}},
    {"name": "Charlie", "age": 30, "items_bought": {"Apples": 1, "Bread": 2}},
    {"name": "David", "age": 22, "items_bought": {"Milk": 2, "Eggs": 12}},
    {"name": "Eve", "age": 28, "items_bought": {"Bananas": 4, "Oranges": 3}},
]
age_filter = 25
```

## Output 1
```
shoppers: ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
filtered_by_age: ['Bob', 'Charlie', 'Eve']
average_age: 28.0
sorted_shoppers: [{'name': 'David', 'age': 22, 'items_bought': {'Milk': 2, 'Eggs': 12}}, {'name': 'Alice', 'age': 25, 'items_bought': {'Apples': 3, 'Bananas': 5}}, {'name': 'Eve', 'age': 28, 'items_bought': {'Bananas': 4, 'Oranges': 3}}, {'name': 'Charlie', 'age': 30, 'items_bought': {'Apples': 1, 'Bread': 2}}, {'name': 'Bob', 'age': 35, 'items_bought': {'Oranges': 2, 'Milk': 1}}]
items_group: {'Apples': ['Alice', 'Charlie'], 'Bananas': ['Alice', 'Eve'], 'Oranges': ['Bob', 'Eve'], 'Milk': ['Bob', 'David'], 'Bread': ['Charlie'], 'Eggs': ['David']}
unique_items: {'Bananas', 'Oranges', 'Bread', 'Eggs', 'Milk', 'Apples'}
```

# Private Test Cases


## Input 1
```
shoppers = [
    {"name": "Alice", "age": 25, "items_bought": {"Apples": 3, "Bananas": 5, "Oranges": 2, "Milk": 1}},
    {"name": "Bob", "age": 35, "items_bought": {"Oranges": 2, "Milk": 1, "Cheese": 1, "Bread": 2}},
    {"name": "Charlie", "age": 30, "items_bought": {"Apples": 1, "Bread": 2, "Eggs": 6, "Butter": 1}},
    {"name": "David", "age": 22, "items_bought": {"Milk": 2, "Eggs": 12, "Bread": 3, "Cheese": 1}},
    {"name": "Eve", "age": 28, "items_bought": {"Bananas": 4, "Oranges": 3, "Tomatoes": 5, "Cucumbers": 2}},
    {"name": "Frank", "age": 40, "items_bought": {"Cheese": 2, "Wine": 1, "Apples": 3, "Bread": 4}},
    {"name": "Grace", "age": 27, "items_bought": {"Oranges": 5, "Apples": 3, "Bread": 2, "Butter": 1}},
    {"name": "Hank", "age": 32, "items_bought": {"Milk": 3, "Cereal": 2, "Eggs": 4, "Tomatoes": 6}},
    {"name": "Ivy", "age": 38, "items_bought": {"Eggs": 6, "Bread": 4, "Milk": 2, "Tomatoes": 3}},
    {"name": "Jack", "age": 29, "items_bought": {"Bananas": 5, "Tomatoes": 4, "Milk": 1, "Oranges": 2}},
    {"name": "Karen", "age": 33, "items_bought": {"Apples": 2, "Oranges": 4, "Bananas": 3, "Bread": 1}},
    {"name": "Louis", "age": 24, "items_bought": {"Milk": 1, "Cereal": 3, "Bread": 2, "Eggs": 5}},
]

```

## Output 1
```
shoppers: ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack', 'Karen', 'Louis']
filtered_by_age: ['Bob', 'Charlie', 'Eve', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack', 'Karen']
average_age: 30.25
sorted_shoppers: [{'name': 'David', 'age': 22, 'items_bought': {'Milk': 2, 'Eggs': 12, 'Bread': 3, 'Cheese': 1}}, {'name': 'Louis', 'age': 24, 'items_bought': {'Milk': 1, 'Cereal': 3, 'Bread': 2, 'Eggs': 5}}, {'name': 'Alice', 'age': 25, 'items_bought': {'Apples': 3, 'Bananas': 5, 'Oranges': 2, 'Milk': 1}}, {'name': 'Grace', 'age': 27, 'items_bought': {'Oranges': 5, 'Apples': 3, 'Bread': 2, 'Butter': 1}}, {'name': 'Eve', 'age': 28, 'items_bought': {'Bananas': 4, 'Oranges': 3, 'Tomatoes': 5, 'Cucumbers': 2}}, {'name': 'Jack', 'age': 29, 'items_bought': {'Bananas': 5, 'Tomatoes': 4, 'Milk': 1, 'Oranges': 2}}, {'name': 'Charlie', 'age': 30, 'items_bought': {'Apples': 1, 'Bread': 2, 'Eggs': 6, 'Butter': 1}}, {'name': 'Hank', 'age': 32, 'items_bought': {'Milk': 3, 'Cereal': 2, 'Eggs': 4, 'Tomatoes': 6}}, {'name': 'Karen', 'age': 33, 'items_bought': {'Apples': 2, 'Oranges': 4, 'Bananas': 3, 'Bread': 1}}, {'name': 'Bob', 'age': 35, 'items_bought': {'Oranges': 2, 'Milk': 1, 'Cheese': 1, 'Bread': 2}}, {'name': 'Ivy', 'age': 38, 'items_bought': {'Eggs': 6, 'Bread': 4, 'Milk': 2, 'Tomatoes': 3}}, {'name': 'Frank', 'age': 40, 'items_bought': {'Cheese': 2, 'Wine': 1, 'Apples': 3, 'Bread': 4}}]
items_group: {'Apples': ['Alice', 'Charlie', 'Frank', 'Grace', 'Karen'], 'Bananas': ['Alice', 'Eve', 'Jack', 'Karen'], 'Oranges': ['Alice', 'Bob', 'Eve', 'Grace', 'Jack', 'Karen'], 'Milk': ['Alice', 'Bob', 'David', 'Hank', 'Ivy', 'Jack', 'Louis'], 'Cheese': ['Bob', 'David', 'Frank'], 'Bread': ['Bob', 'Charlie', 'David', 'Frank', 'Grace', 'Ivy', 'Karen', 'Louis'], 'Eggs': ['Charlie', 'David', 'Hank', 'Ivy', 'Louis'], 'Butter': ['Charlie', 'Grace'], 'Tomatoes': ['Eve', 'Hank', 'Ivy', 'Jack'], 'Cucumbers': ['Eve'], 'Wine': ['Frank'], 'Cereal': ['Hank', 'Louis']}
unique_items: {'Bananas', 'Cucumbers', 'Cheese', 'Cereal', 'Tomatoes', 'Apples', 'Milk', 'Oranges', 'Butter', 'Eggs', 'Bread', 'Wine'}
```