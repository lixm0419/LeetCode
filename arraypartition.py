#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 00:05:01 2018

@author: xiaomengli
"""

def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()    
        return sum(nums[2*i] for i in range(len(nums)//2))
        ##better way return(sum(nums[::2]))