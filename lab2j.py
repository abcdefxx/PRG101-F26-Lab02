#!/usr/bin/env python3
# Author: Aaradhya Shrestha
# Date: October 2, 2026
# Purpose: Practice using break and continue in a loop.
# Usage: python ./lab2j.py

# TO DO 1:
# Follow the instructions given in the README.md file.

import math

while True:
    number = float(input("Please type in a number: "))

    if number < 0:
        print("Invalid number.")
        continue

    if number == 0:
        print("Exiting ...")
        break

    print(math.sqrt(number))