#!/usr/bin/env python3
# Author: Aaradhya Shrestha
# Date: October 2, 2026
# Purpose: Calculate the sum of all even numbers from 1 to 100.
# Usage: python ./lab2k.py

# TO DO 1:
# Follow the instructions given in the README.md file.

total = 0

for i in range(1, 101):
    if i % 2 == 0:
        total = total + i

print(total)