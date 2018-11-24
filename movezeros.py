#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 23:41:52 2018

@author: xiaomengli
"""


def findDisappearedNumbers(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            index = abs(nums[i])-1
            nums[index]=-abs(nums[index])
            
        return [i+1 for i in range(len(nums)) if nums[i]>0]
    
nums=[4,3,2,7,8,2,3,1]
###Better solution
def findDisappearedNumbers(nums):
    return list(set(range(1,len(nums)+1))-set(nums))