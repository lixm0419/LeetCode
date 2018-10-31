#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 20:59:58 2018

@author: xiaomengli
"""


def selfDividingNumbers(left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        output=[]
        for x in range(left,right+1):
            if x<10:
                output.append(x)
            else:
                a=len(str(x))-1
                b=[x//(10**a)]
                a1=x
                while(a>0):
                    a1=a1-b[-1]*10**a
                    a=a-1
                    b.append(a1//(10**a))
                b.append(a1%10)
                    
                if 0 not in b:
                    d=[x%c==0 for c in b]
                    if False not in d:
                        output.append(x)
        return output    
    
    
### better solution
def self_dividing(n):
            for d in str(n):
                if d=='0' or n%int(d)>0:
                    return False;
            return True
                
        ans=[]
        for n in range(left,right+1):
            if self_dividing(n):
                ans.append(n)
        return ans
        
    
###other option
  def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def self_dividing(n):
            x=n
            while(x>0):
                x,d=divmod(x,10)
                if d==0 or n%d>0 :
                    return False;
            return True
                
        ans=[]
        for n in range(left,right+1):
            if self_dividing(n):
                ans.append(n)
        return ans
        