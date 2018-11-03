#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 21:55:54 2018

@author: xiaomengli
"""

def numUniqueEmails(emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        uniemail=set()
        for x in emails:
            a,b = x.split('@')
            c=a.split('+')[0]
            c=c.replace('.','')
            uniemail.add(c+'@'+b)
            
        return len(uniemail)