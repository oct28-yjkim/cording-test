#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    count = 0
    mid1 = d // 2
    mid2 = mid1 if d % 2 else mid1 - 1
 
    subexp = sorted(expenditure[:d])
    for i, exp in enumerate(expenditure[d:], d-1):
        x = expenditure[i-d]
        if i != d-1 and x != expenditure[i]:
            idx = bisect.bisect_left(subexp, x)
            subexp.pop(idx)
            bisect.insort(subexp, expenditure[i])

        if exp >= subexp[mid1] + subexp[mid2]:
            count += 1
    return count

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
