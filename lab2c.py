#!/usr/bin/env python3
# Author: Aaradhya Shrestha
# Date: October 2, 2026
# Purpose: Compare the length of two strings.
# Usage: ./lab2c.py

# TO DO 1:
# Follow the instructions given in the README.md file.

str1 = input("Enter a sentence: ")
str2 = input("Enter another sentence: ")

if len(str1) > len(str2):
    print(str1 + " is longer then " + str2 + "!")
elif len(str1) < len(str2):
    print(str2 + " is longer then " + str1 + "!")
else:
    print(str1 + " and " + str2 + " are of equal length!")