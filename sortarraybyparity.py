#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 21:59:58 2018

@author: xiaomengli
"""


def sortArrayByParity(A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        idx=0
        for i in range(len(A)):
            if A[i]%2==0:
                A[idx],A[i]=A[i],A[idx]
                idx+=1
        return(A)
    
