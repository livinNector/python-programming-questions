---
title:Parking Bill Calculation System
Problem Statement
---
# Problem Statement
Write a program that calculates the parking bill based on the following factors:

Day Type:

0 for weekdays.
1 for weekends.
Vehicle Type:

0 for two-wheelers.
1 for four-wheelers.
Time of Day:

0 for non-peak hours.
1 for peak hours.
Number of Hours:

Parking duration in hours.
The charges are as follows:

Weekdays:
Two-wheeler: ₹20 per hour (Non-peak), ₹20/hour + ₹20 flat (Peak).
Four-wheeler: ₹40 per hour (Non-peak), ₹40/hour + ₹30 flat (Peak).
Weekends:
Two-wheeler: ₹40 per hour (Non-peak), ₹40/hour + ₹20 flat (Peak).
Four-wheeler: ₹60 per hour (Non-peak), ₹60/hour + ₹30 flat (Peak).
Your program should prompt the user to enter the day, vehicle type, time of day, and number of hours, and then calculate and print the parking bill.
**Sample Input**
```
Day: 0 (Weekday)
Vehicle Type: 0 (Two-wheeler)
Time: 1 (Peak Hour)
Hours: 2
```
**Sample Output**
```
The bill is: ₹60
```
# Solution
```py test.py -r 'python3 test.py'
<template>
def parking_bill():
    """
    Main function to calculate parking bill based on user inputs.
    Repeatedly prompts the user until they choose to exit.
    """
    # Ask user whether it's a weekday or weekend
    day = int(input("Enter 0 for weekday and 1 for weekend: "))
   
    while True:
        # Ask user for vehicle type (two-wheeler or four-wheeler)
        wheel = int(input("Enter 0 for two-wheeler and 1 for four-wheeler: "))
       
        # Ask user whether it's peak or non-peak hour
        peak = int(input("Enter 0 for non-peak hour and 1 for peak hour: "))
       
        # Ask user for the number of hours the vehicle is parked
        hrs = int(input("Enter number of hours: "))
       
        # Calculate bill based on the day type (weekday or weekend)
        if day == 0:
            weekday(wheel, peak, hrs)  # Weekday calculation
        else:
            weekend(wheel, peak, hrs)  # Weekend calculation
       
        # Prompt user if they want to calculate another bill
        con = input("Do you want to calculate another bill? (Y/N): ")
        if con.lower() == 'y':  # Continue if 'Y' or 'y'
            continue
        else:  # Exit the loop and terminate
            print("Exiting...")
            break

def weekday(vehicle_type, peak_hour, hours):
    """
    Function to calculate parking bill for weekdays.
   
    Arguments:
    vehicle_type: int - 0 for two-wheeler, 1 for four-wheeler.
    peak_hour: int - 0 for non-peak hour, 1 for peak hour.
    hours: int - number of hours parked.
    """
    if vehicle_type == 0:  # Two-wheeler
        if peak_hour == 0:  # Non-peak hour
            bill = 20 * hours
        else:  # Peak hour
            bill = 20 * hours + 20
    else:  # Four-wheeler
        if peak_hour == 0:  # Non-peak hour
            bill = 40 * hours
        else:  # Peak hour
            bill = 40 * hours + 30
   
    # Print the calculated bill
    print(f"The bill is: ₹{bill}")

def weekend(vehicle_type, peak_hour, hours):
    """
    Function to calculate parking bill for weekends.
   
    Arguments:
    vehicle_type: int - 0 for two-wheeler, 1 for four-wheeler.
    peak_hour: int - 0 for non-peak hour, 1 for peak hour.
    hours: int - number of hours parked.
    """
    if vehicle_type == 0:  # Two-wheeler
        if peak_hour == 0:  # Non-peak hour
            bill = 40 * hours
        else:  # Peak hour
            bill = 40 * hours + 20
    else:  # Four-wheeler
        if peak_hour == 0:  # Non-peak hour
            bill = 60 * hours
        else:  # Peak hour
            bill = 60 * hours + 30
   
    # Print the calculated bill
    print(f"The bill is: ₹{bill}")

# Call the function to start the program
parking_bill()
</template>
```
# Public Test Cases
## Input 1
```
Day: 0
Vehicle Type: 0
Time: 0
Hours: 5
```
## Output 1
```
The bill is: ₹100
```
## Input 2
```
Day: 1
Vehicle Type: 0
Time: 1
Hours: 2
```
## Output 2
```
The bill is: ₹100
```
## Input 3
```
Day: 1
Vehicle Type: 1
Time: 1
Hours: 1
```
## Output 3
```
The bill is: ₹90
```

# Private Test Cases
## Input 1
```
Day: 0
Vehicle Type: 1
Time: 1
Hours: 3
```
## Output 1
```
The bill is: ₹150
```