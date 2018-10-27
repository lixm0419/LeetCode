#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 23:32:39 2018

@author: xiaomengli
"""

def hammingDistance(x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a="{0:032b}".format(x)
        b="{0:032b}".format(y)
        c=0
        
        for i in range(len(a)):
            if a[i]!=b[i]:
                c+=1
        
        return c