#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
print(queue)
queue.append("Graham")
print(queue)
print(queue.popleft())
print(queue.popleft())
print(list(queue))
