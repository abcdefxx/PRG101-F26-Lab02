#!/usr/bin/env python3
# Author: Aaradhya Shrestha
# Date: October 2, 2026
# Purpose: Keep asking for a PIN until the correct one is entered.
# Usage: python ./lab2i.py

# TO DO 1:
# Follow the instructions given in the README.md file.

pin = input("Please type in your PIN: ")

while pin != "1234":
    print("Incorrect...try again\n")
    pin = input("Please type in your PIN: ")

print("Correct PIN, You can enter!")