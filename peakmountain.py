#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 23:07:23 2018

@author: xiaomengli
"""

def peakIndexInMountainArray(A):
        """
        :type A: List[int]
        :rtype: int
        """
        lo,hi=0, len(A)-1
        while lo<hi:
            m=(lo+hi)//2
            if A[m]<A[m+1]:
                lo=m+1
            else:
                hi=m
        return lo