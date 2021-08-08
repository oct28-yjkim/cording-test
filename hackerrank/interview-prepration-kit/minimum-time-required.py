#!/bin/python3

import math
import os
import random
import re
import sys
from math import ceil
from collections import Counter

# Complete the minTime function below.
def minTime(machines, goal):
    c = Counter(machines)
    fastest = min(c)
    min_days = 1
    max_days = ceil((fastest*goal)/c[fastest])
    while max_days-min_days>1:
        mid = (min_days+max_days)//2
        output = sum((mid//x)*y for x,y in c.items())
        if output<goal:
            min_days = mid
        else:
            max_days = mid
    return max_days