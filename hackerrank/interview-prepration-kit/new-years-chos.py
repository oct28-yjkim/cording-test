#!/bin/python3

import math 
import os 
import random
import re
import sys

def minimumBribes(q):
    bribes = 0 
    for i in range(len(q)-1,-1,-1):
        if q[i] - (i + 1) > 2:
            print("too chaotic")
            return 
        for j in range(max(0,q[i] -2), i):
            if q[j] > q[i]:
                bribes+=1
    print(bribes)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)