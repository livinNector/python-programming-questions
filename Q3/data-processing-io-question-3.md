---
title: Data Processing I/O Question
tags: ['csv', 'defaultdict','aggregation','stdin','stdout','max']
---

# Problem Statement
## StartDuck Coffee shop Sales Analysis

    StarDuck is a Coffee company and they are trying to expand their base in India.
    The CEO is confident but slightly confused and has some questions. 
    You as IITM BS student who has learnt python can help him answer some questions by uncovering some insights from the data they have shared with you.
    The data has the following attributes
    -- Date
    -- Day
    -- Product
    -- Quantity
    -- Price
    -- Total Sales
    -- Payment Method

    the data is in csv format read the data from stdin

    Answer the following questions by implementing the below functions

        1> What is the most profitable day of the week for StarDuck?
        2> Which product generates the highest revenue?
        3> Which payment method is used very frequently?
        4> What is the average daily revenue?

    Print the answers to the above question to stdout.
# Solution
```python test.py  -r 'python test.py'
<prefix>

</prefix>
<template>



    

def analyze_starduck_sales():
    <sol>
    import sys
    import csv
    from collections import defaultdict, Counter
    # Read CSV data from stdin
    csv_reader = csv.DictReader(sys.stdin)

    # Data structures to store required information
    day_sales = defaultdict(float)
    product_sales = defaultdict(float)
    payment_method_count = Counter()
    daily_revenue = defaultdict(float)

    # Process the CSV file row by row
    for row in csv_reader:
        day = row["Day"]
        product = row["Product"]
        payment_method = row["Payment Method"]
        date = row["Date"]
        total_sales = float(row["Total Sales"])

        # Aggregate data
        day_sales[day] += total_sales
        product_sales[product] += total_sales
        payment_method_count[payment_method] += 1
        daily_revenue[date] += total_sales

    # 1. Most profitable day and its revenue
    most_profitable_day = max(day_sales, key=day_sales.get)
    most_profitable_day_revenue = day_sales[most_profitable_day]

    # 2. Most profitable product and its revenue
    highest_revenue_product = max(product_sales, key=product_sales.get)
    highest_revenue_product_sales = product_sales[highest_revenue_product]

    # 3. Most frequently used payment method
    most_frequent_payment_method = max(payment_method_count, key=payment_method_count.get)

    # 4. Average daily revenue
    average_daily_revenue = sum(daily_revenue.values()) / len(daily_revenue)

    # Print results
    print(f"{most_profitable_day} {most_profitable_day_revenue:.2f}")
    print(f"{highest_revenue_product} {highest_revenue_product_sales:.2f}")
    print(f"{average_daily_revenue:.2f}")
    print(f"{most_frequent_payment_method}")
    </sol>


 


        
</template>

<suffix>
#driver code

analyze_starduck_sales()

</suffix>

```

# Public Test Cases

## Input 1

```
Date,Day,Product,Quantity,Price,Total Sales,Payment Method
2025-01-01,Monday,Coffee,120,3.50,420.00,Credit Card
2025-01-01,Monday,Tea,50,2.50,125.00,Cash
2025-01-01,Monday,Pastry,80,4.00,320.00,Credit Card
2025-01-02,Tuesday,Coffee,150,3.50,525.00,Debit Card
2025-01-02,Tuesday,Tea,60,2.50,150.00,Cash
2025-01-02,Tuesday,Pastry,90,4.00,360.00,Credit Card
2025-01-03,Wednesday,Coffee,130,3.50,455.00,Cash
2025-01-03,Wednesday,Tea,40,2.50,100.00,Credit Card
2025-01-03,Wednesday,Pastry,70,4.00,280.00,Debit Card
2025-01-04,Thursday,Coffee,160,3.50,560.00,Credit Card
2025-01-04,Thursday,Tea,70,2.50,175.00,Debit Card
2025-01-04,Thursday,Pastry,100,4.00,400.00,Cash
2025-01-05,Friday,Coffee,180,3.50,630.00,Cash
2025-01-05,Friday,Tea,90,2.50,225.00,Credit Card
2025-01-05,Friday,Pastry,110,4.00,440.00,Debit Card
2025-01-06,Saturday,Coffee,200,3.50,700.00,Debit Card
2025-01-06,Saturday,Tea,80,2.50,200.00,Cash
2025-01-06,Saturday,Pastry,120,4.00,480.00,Credit Card
2025-01-07,Sunday,Coffee,170,3.50,595.00,Credit Card
2025-01-07,Sunday,Tea,100,2.50,250.00,Debit Card
2025-01-07,Sunday,Pastry,130,4.00,520.00,Cash


```

## Output 1

```
Saturday 1380.00
Coffee 3885.00
1130.00
Credit Card

```
# Private Test Cases
## Input 1

```
Date,Day,Product,Quantity,Price,Total Sales,Payment Method
2024-01-01,Monday,Espresso,5,3.00,15.00,Credit Card
2024-01-01,Monday,Cappuccino,3,4.50,13.50,Cash
2024-01-01,Monday,Latte,7,5.00,35.00,UPI
2024-01-02,Tuesday,Espresso,6,3.00,18.00,UPI
2024-01-02,Tuesday,Americano,4,3.50,14.00,Credit Card
2024-01-02,Tuesday,Latte,5,5.00,25.00,Cash
2024-01-03,Wednesday,Mocha,8,5.50,44.00,Credit Card
2024-01-03,Wednesday,Latte,10,5.00,50.00,UPI
2024-01-04,Thursday,Cappuccino,4,4.50,18.00,Debit Card
2024-01-04,Thursday,Espresso,5,3.00,15.00,Credit Card
2024-01-05,Friday,Mocha,6,5.50,33.00,Cash
2024-01-05,Friday,Latte,8,5.00,40.00,UPI
2024-01-06,Saturday,Americano,9,3.50,31.50,Credit Card
2024-01-06,Saturday,Cappuccino,6,4.50,27.00,UPI
2024-01-07,Sunday,Mocha,10,5.50,55.00,Credit Card
2024-01-07,Sunday,Espresso,7,3.00,21.00,Cash




```

## Output 1

```
Wednesday 94.00
Latte 150.00
65.00
Credit Card
```
