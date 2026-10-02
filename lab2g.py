#!/usr/bin/env python3
# Author: Aaradhya Shrestha
# Date: October 2, 2026
# Purpose: Calculate tax using nested if statements.
# Usage: python ./lab2g.py

# TO DO 1:

income = float(input("Enter your taxable income: "))
status = input("Enter your status (single/married): ").lower()

if status == "single":
    if income <= 32000:
        tax = income * 0.10
    else:
        tax = 3200 + (income - 32000) * 0.25
    print("Your tax is $" + str(tax))
elif status == "married":
    if income <= 64000:
        tax = income * 0.10
    else:
        tax = 6400 + (income - 64000) * 0.25
    print("Your tax is $" + str(tax))
else:
    print("Invalid status. Please enter single or married.")