#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

"""
使用栈实现队列的下列操作：

push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。
示例:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false
"""


class MyQueue():
    def __init__(self):
        self.lst = []

    def push(self, x):
        self.lst.insert(0, x)
        print(self.lst)

    def pop(self):
        return self.lst.pop()

    def peek(self):
        return self.lst[-1]

    def empty(self):
        return len(self.lst) == 0


obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj)
print(obj.peek())
print(obj.pop())
print(obj.empty())
