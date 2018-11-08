#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 23:07:33 2018

@author: xiaomengli
"""

def projectionArea(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        xy=0
        yz0=[]
        for i in range(len(grid[0])):
            a=grid[0][i]
            for j in range(len(grid)):
                if grid[j][i]>a:
                    a=grid[j][i]
                if grid[j][i]:
                    xy+=1
            yz0.append(a)
        yz=sum(yz0)
        xz0=[]
        for i in range(len(grid)):
                xz0.append(max(grid[i]))
        xz=sum(xz0)
        return (xy+yz+xz)
    
##better solution
def projectionArea(grid):
    ans=0
    for i in range(len(grid)):
        best_row=0
        best_col=0
        for j in range(len(grid)):
            if grid[i][j]:
                ans+=1
            best_row=max(best_row,grid[i][j])
            best_col=max(best_col,grid[j][i])
         ans=ans+best_row+best_col   
    
    return ans