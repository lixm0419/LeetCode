#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 23:29:27 2018

@author: xiaomengli
"""

def sortArrayByParityII(A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd=[]
        even=[]
        for x in A:
            if x%2==0:
                even.append(x)
            else:
                odd.append(x)
        
        for i in range(len(A)//2):
            A[2*i]=even[i]
            A[2*i+1]=odd[i]
        
        return A
    
    
##better solution

j=1
for i in xrange(0,len(A),2):
    if A[i]%2:
        while A[j]%2:
            j+=2
        A[i],A[j]=A[j],A[i]
