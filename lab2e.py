#!/usr/bin/env python3
# Author: Aaradhya Shrestha
# Date: October 2, 2026
# Purpose: Check how many command line arguments were provided.
# Usage: python ./lab2e.py

# TO DO 1:

import sys

count = len(sys.argv) - 1
words = ["zero", "one", "two", "three", "four", "five"]

if count == 0:
    print("This script requires exactly two arguments. No arguments were provided!")
elif count == 2:
    print("Hello user, good job, your provided two arguments!")
else:
    print("This script requires exactly two arguments. You provided " + words[count] + " arguments.")