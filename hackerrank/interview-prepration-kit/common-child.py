#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    # Write your code here
    n = len(s1)
    lcs = [[0]*(n+1) for _ in range(2)]


    for i in range(1, n+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                lcs[1][j] = lcs[0][j-1] + 1
            else:
                if lcs[0][j] >= lcs[1][j-1]:
                    lcs[1][j] = lcs[0][j]
                else:
                    lcs[1][j] = lcs[1][j-1]

        lcs[0] = lcs[1][:]

    return lcs[0][n]
    