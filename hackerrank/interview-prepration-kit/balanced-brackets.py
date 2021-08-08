#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    stack = []
    bracketDict = {
        "}" : "{",
        "]" : "[",
        ")" : "("
    }
    for b in s:
        if b in bracketDict and stack and bracketDict[b] == stack[-1]:
            stack.pop()
        else:
            stack.append(b)

    if stack:
        return("NO")
    else:
        return("YES")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    values_count = int(input())

    values = []

    for _ in range(values_count):
        values_item = input()
        values.append(values_item)

    res = isBalanced(values)

    fptr.write('\n'.join(res))
    fptr.write('\n')

    fptr.close()