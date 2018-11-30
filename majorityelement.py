#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 23:54:34 2018

@author: xiaomengli
"""

def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        value={}
        for i in range(len(nums)):
            if nums[i] not in value:
                value[nums[i]]=1
            else:
                value[nums[i]]+=1
        return max(value,key=value.get)
    
###better solution
def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = collections.Counter(nums)
        return max(a.keys(),key=a.get)


###better solution
def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        candidate=None
        for num in nums:
            if count==0:
                candidate=num
            count+=(1 if num==candidate else -1)
        
        return candidate