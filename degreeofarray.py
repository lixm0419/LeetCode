#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 23:05:31 2018

@author: xiaomengli
"""

def findShortestSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left,right,count={},{},{}
        for i,x in enumerate(nums):
            if x not in left:
                left[x]=i
            right[x]=i
            count[x]=count.get(x,0)+1
        
        maxcon=max(count.values())
        ans=len(nums)
        for x in count:
            if count[x]==maxcon:
                ans= min(right[x]-left[x]+1,ans)
                
        return ans