#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 17:31:35 2018

@author: xiaomengli
"""

def findMaxConsecutiveOnes(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=[i for i,x in enumerate(nums) if x==0]
        if a==[]:
            return len(nums)
        else:
            
            a.append(len(nums))
            a=[-1]+a
            diff=0
            for j in range(len(a)-1):
                if diff<a[j+1]-a[j]-1:
                    diff=a[j+1]-a[j]-1
            return diff
        
        
###better solution
 def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt=0
        ans=0
        for i in nums:
            if i==1:
                cnt+=1
                ans=max(ans,cnt)
            else:
                cnt=0
        return ans
    
