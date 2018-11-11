#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 12:47:02 2018

@author: xiaomengli
"""


 def transpose(self, a):
     ans=[]

    for j in range(len(a[0])):
        ans0=[]
        for i in range(len(a)):
            ans0.append(a[i][j])
        ans.append(ans0)
    return ans

### better solution

    

 def transpose(self, A):
        R, C = len(A), len(A[0])
        ans = [[None] * R for _ in xrange(C)]
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                ans[c][r] = val
        return ans