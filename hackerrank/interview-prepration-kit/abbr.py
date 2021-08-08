#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def isEqual(a, b):
    return a == b or a.upper() == b

def abbreviation(a, b):
    # Write your code here
    DP = []
    for i in range(len(a) + 1):
        DP.append([False] * (len(b) + 1))
    DP[0][0] = True
    
    for i in range(1, len(a) + 1):
        for j in range(0, len(b) + 1):
            if j > 0 and DP[i - 1][j - 1] and isEqual(a[i - 1], b[j - 1]):
                DP[i][j] = True
            if ord(a[i - 1]) >= 97 and DP[i - 1][j]:
                DP[i][j] = True

    return "YES" if DP[len(a)][len(b)] else "NO"