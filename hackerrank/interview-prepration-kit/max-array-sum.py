#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    if len(arr) == 1:
        return arr[0]
        
    dp = [arr[0], max(arr[:2])] + [0]*(len(arr)-2)
    for i in range(2, len(arr)):
        dp[i] = max(arr[i], dp[i-1], dp[i-2]+arr[i])
    
    return dp[-1]
