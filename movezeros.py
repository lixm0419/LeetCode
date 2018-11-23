#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 23:41:52 2018

@author: xiaomengli
"""


count=nums.count(0)
while count>=0:
    nums.remove(0)
    nums.append(0)
    count-=1
    
### better solution
def moveZeros(nums):
    z=0 
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[i],nums[z]=nums[z],nums[i]
            z+=1