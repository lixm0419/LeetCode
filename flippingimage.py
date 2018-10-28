#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 10:30:55 2018

@author: xiaomengli
"""

def flipAndInvertImage(A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        a1=[list(reversed(x)) for x in A]
        a2=[[abs(x-1) for x in a] for a in a1]
        return(a2)