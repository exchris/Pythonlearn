#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'


class Node:
    def __init__(self, number):
        self.number = number
        self.rchild = None
        self.lchild = None


class Tree:
    lis = []

    def __init__(self):
        self.root = None

    def add(self, number):
        node = Node(number)

        if self.root is None:
            self.root = node
            Tree.lis.append(self.root)

        else:
            while True:
                point = Tree.lis[0]

                if point.lchild == None:
                    point.lchild = node
                    Tree.lis.append(point.lchild)
                    return
                elif point.rchild == None:
                    point.rchild = node
                    Tree.lis.append(point.rchild)
                    Tree.lis.pop(0)
                    return


if __name__ == '__main__':
    t = Tree()
    L = [1, 2, 3, 4, 5, 6, 7]
    for x in L:
        t.add(x)

    print(t)
