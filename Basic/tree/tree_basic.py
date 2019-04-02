#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Function:simulate the binary tree in python
# __author__ :exchris
#

# Definition for a binary tree node.

myTree = [
    "a",  # root
    ["b",  # left subtree
     ["d", [], []], ["e", [], []]],
    ["c",  # right subtree
     ["f", [], []], []]
]

print(myTree)
print('left subtree = ', myTree[1])
print('root = ', myTree[0])
print('right subtree = ', myTree[2])
