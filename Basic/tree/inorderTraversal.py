#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)

        if self.root is None:
            self.root = node
        else:
            q = [self.root]

            while True:
                pop_node = q.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

    def inorderTraversal(self, root):
        if root is None:
            return []
        result = [root.item]
        left_item = self.inorderTraversal(root.left)
        right_item = self.inorderTraversal(root.right)
        return left_item + result + right_item

if __name__ == "__main__":
    t = Solution()
    print(t)
