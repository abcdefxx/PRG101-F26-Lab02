#!/usr/bin/env python3
# Author: Aaradhya Shrestha
# Date: October 1, 2026
# Purpose: Create a variable, check its type and print the variable.
# Usage: ./lab2a.py

# TO DO 1:

x = input("Enter a number: ")
print(type(x))        
x = int(x)            
print(type(x))        

if x >= 6:
    print("x is greater then 6!")

if x >= 4 and x < 12:
    print("x is between 4 and 12!")