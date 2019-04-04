# Given an array, , of  integers, print 's elements in
# reverse order as a single line of space-separated
# numbers.
# INPUT: 1 4 3 2
# OUTPUT: 2 3 4 1

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    # my code start from here
    new_arr = arr[::-1]

    print(' '.join(str(i) for i in new_arr))