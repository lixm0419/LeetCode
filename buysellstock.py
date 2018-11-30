#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 18:42:26 2018

@author: xiaomengli
"""

prices=[8,3,6,2,8,8,8,4,2,0,7,2,9,4,9]

profit=0
valley=0
peak=0
n=len(prices)
if n!=0 and n!=1:
    if prices[0]<=prices[1]:
        valley=prices[0]
    for i in range(1,n-1):
        if prices[i-1]>=prices[i] & prices[i]<=prices[i+1]:
            valley=prices[i]
        if prices[i-1]<=prices[i] & prices[i]>=prices[i+1] and prices[i]!=peak:
            peak=prices[i]
            if peak> valley:
                profit+=peak-valley
    if prices[n-1]>prices[n-2]:
        peak=prices[n-1]
        if peak>valley:
            profit+=peak-valley
            
            
###better solution
def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum(max(prices[i+1]-prices[i],0) for i in range(0,len(prices)-1))