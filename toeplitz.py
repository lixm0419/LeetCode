#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 16:22:44 2018

@author: xiaomengli
"""

 def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        

        ncol=len(matrix[0])
        nrow=len(matrix)
        for i in range(nrow-1):
            for j in range(ncol-1):
                if matrix[i][j]!= matrix[i+1][j+1]:
                    return False
        return True
    
    
### better sulotion

def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        group={}
        
        for nrow, row in enumerate(matrix):
            for ncol,col in enumerate(row):
                if ncol-nrow not in group:
                    group[ncol-nrow]=col
                elif col != group[ncol-nrow]:
                    return False
        return True
    
## faster solution
