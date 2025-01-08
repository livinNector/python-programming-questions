---
title: Simple Product Sales Analysis
tags: ['python', 'data-types', 'strings', 'int', 'dictionaries', 'stdin']
---
# Problem Statement
Given a list of product sales, calculate:
1. The total quantity sold for each product (in alphabetical order)
2. The product that sold the most units (best seller)

**Input Format:** First line contains N (number of sales). Next N lines contain space-separated product_name and quantity.

**Output Format:** Print each product's total quantity in alphabetical order, followed by the best seller.

**Note:** Product names contain only lowercase letters.

**Sample Input**
```
5
apple 10
banana 5
apple 3
orange 8
banana 7
```

**Sample Output**
```
apple: 13
banana: 12
orange: 8
best_seller: apple
```

**Explanation**  
Apple sold 10+3=13 units, banana sold 5+7=12 units, and orange sold 8 units. Apple has the highest total sales (13), making it the best seller.

# Solution
```py test.py -r 'python3 test.py'
<prefix>
def analyze_sales(n: int) -> str:
    '''
    Process n product sales and return formatted string
    containing total sales per product and best seller.
    '''
</prefix>
<template>
    <sol>
    # Initialize dictionary for product quantities
    product_sales = {}
    # Process each sale
    for i in range(n):
        product, quantity = input().split()
        quantity = int(quantity)
        if product not in product_sales:
            product_sales[product] = quantity
        else:
            product_sales[product]+= quantity
    result = []
    # Add product totals in alphabetical order
    for product in sorted(product_sales.keys()):
        result.append(f"{product}: {product_sales[product]}")
    # Add best seller
    best_seller = max(product_sales.items(), key=lambda x: x[1])[0]
    result.append(f"best_seller: {best_seller}")
    return "\n".join(result)
    </sol>
    <los>pass</los>
</template>
<suffix>
n = int(input())
print(analyze_sales(n))
</suffix>
```

# Public Test Cases
## Input 1
```
5
apple 10
banana 5
apple 3
orange 8
banana 7
```
## Output 1
```
apple: 13
banana: 12
orange: 8
best_seller: apple
```
## Input 2
```
3
milk 3
bread 2
milk 4
```
## Output 2
```
bread: 2
milk: 7
best_seller: milk
```
## Input 3
```
4
tea 5
coffee 5
juice 5
tea 1
```
## Output 3
```
coffee: 5
juice: 5
tea: 6
best_seller: tea
```

# Private Test Cases
## Input 1
```
2
book 1
pen 1
```
## Output 1
```
book: 1
pen: 1
best_seller: book
```
## Input 2
```
1
apple 10
```
## Output 2
```
apple: 10
best_seller: apple
```
## Input 3
```
6
water 2
soda 3
water 4
juice 1
soda 2
water 1
```
## Output 3
```
juice: 1
soda: 5
water: 7
best_seller: water
```
