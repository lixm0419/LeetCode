#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 19:53:21 2018

@author: xiaomengli
"""

def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        trans=list()
        letters='abcdefghijklmnopqrstuvwxyz'
        for i in words:
            string=str()
            for j in i:
                string=string+code[letters.find(j)]
            trans.append(string)
        
        unique_list=[]
        
        for x in trans:
            if x not in unique_list:
                unique_list.append(x)
        
        return(len(unique_list))