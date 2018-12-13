# In this challenge, we're going to use loops to help us do some simple math. Check out the Tutorial tab to learn more.
# Task
# Given an integer, n, print its first 10 multiples. Each multiple nxi (where 1 <i <10 ) should be printed on a new line in the form: n x i = result.

# Input Format

# A single integer, n.

# Constraints
# 2 <equal n <equal 20

# Output Format

# Print 10 lines of output; each line i (where 1 <i <10 ) contains the result of n x i in the form:
# n x i = result.

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    for i in range(1,11):
    print(str(n) + " x " + str(i) + " = " + str(n*i))
