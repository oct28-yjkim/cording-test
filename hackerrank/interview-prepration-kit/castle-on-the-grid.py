#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#
def helper(grid,n,i,j,direction,stack,des):
    grid[i][j]='*'
    if direction==0:
        y=j
        while y>=1 and grid[i][y-1]!='X' and grid[i][y-1]!='*':
            y-=1
            if (i,y)==des:
                return True
            stack.append((i,y,direction))
        return False
    if direction==3:
        y=j
        while y<n-1 and grid[i][y+1]!='X' and grid[i][y+1]!='*':
            y+=1
            if (i,y)==des:
                return True
            stack.append((i,y,direction))
        return False
    if direction==1:
        x=i
        while x>=1 and grid[x-1][j]!='X' and grid[x-1][j]!='*':
            x-=1
            if (x,j)==des:
                return True
            stack.append((x,j,direction))
        return False
    if direction==2:
        x=i
        while x<n-1 and grid[x+1][j]!='X' and grid[x+1][j]!='*':
            x+=1
            if (x,j)==des:
                return True
            stack.append((x,j,direction))
        return False
        
def minimumMoves(grid, startX, startY, goalX, goalY):
    # Write your code here
    n=len(grid)
    grid=[list(item) for item in grid]
    stack=[]
    des=(goalX,goalY)
    if (startX,startY)==des:
        return 0
    # left,right,up,down=(0,3,1,2)
    for direction in range(4):
        if helper(grid,n,startX,startY,direction,stack,des):
            return 1
    count=1
    while stack:
        m=len(stack)
        count+=1
        while m>0:
            m-=1
            i,j,k=stack.pop(0)
            for direction in range(4):
                if helper(grid,n,i,j,direction,stack,des):
                    return count
    return count
