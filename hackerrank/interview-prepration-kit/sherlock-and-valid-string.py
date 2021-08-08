#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def isValid(s):
    # Write your code here
    c = Counter(Counter(s).values())
    if len(c)==1:
        return "YES"
    if len(c)>2:
        return "NO"
    if 1 in c.values() and (c[min(c.keys())]==1 or (max(c.keys()) - min(c.keys())==1)):
        return "YES"
    else:
        return "NO"