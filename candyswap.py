#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 23:33:59 2018

@author: xiaomengli
"""

 def fairCandySwap(A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        dif=sum(B)-sum(A)
        b=set(B)
        for i in A:
            if (dif+2*i)//2 in b:
                return[i,(dif+2*i)//2]