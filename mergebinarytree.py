#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 11:19:16 2018

@author: xiaomengli
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            t3=TreeNode(t1.val+t2.val)
            t3.left=self.mergeTrees(t1.left,t2.left)
            t3.right=self.mergeTrees(t1.right,t2.right)
            return t3
        else:
            return t1 or t2
        