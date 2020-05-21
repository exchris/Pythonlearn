#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

class Solution:
    def preorderTraversal(self, root):
        if root is None:
            return []
        result = [root.val]
        left_val = self.preorderTraversal(root.left)
        right_val = self.preorderTraversal(root.right)
        return result + left_val + right_val