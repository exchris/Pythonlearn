#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'


class Solution:
    def postorderTraversal(self, root):
        if root is None:
            return []
        result = [root.val]
        left_item = self.postorderTraversal(root.left)
        right_item = self.postorderTraversal(root.right)
        return left_item + right_item + result
