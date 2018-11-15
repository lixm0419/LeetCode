#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 17:31:35 2018

@author: xiaomengli
"""

 def matrixReshape(nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
       
        a=[x for y in nums for x in y]
        
        if r*c != len(a):
            return nums
        else:
            ans=[a[i:i+c] for i in range(0,len(a),c)]
            return ans
        