#!/usr/bin/env python3
# Author: Aaradhya Shrestha
# Date: October 2, 2026
# Purpose: Use command line arguments to print a message.
# Usage: python ./lab2f.py

# TO DO 1:

import sys

if len(sys.argv) < 3:
    print("The script requires at least 2 arguments.")
elif len(sys.argv) >= 3:
    name = sys.argv[1]
    age = sys.argv[2]
    print("Hi " + name + ", you are " + age + " years old and the script received " + str(len(sys.argv) - 1) + " arguments.")