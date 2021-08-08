#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def candies(n, arr):
    c = [1]*n
    for i in range(n-1):
        if arr[i] < arr[i+1]:
            c[i+1] = c[i] + 1
    for j in range(n-1, 0, -1):
        if arr[j] < arr[j-1] and c[j] >= c[j-1]:
            c[j-1] = c[j] + 1
    return sum(c)
