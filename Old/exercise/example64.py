#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/25 0025 下午 3:49
# @Author  : Exchris Tsai
# @Site    : 
# @File    : example64.py
# @Software: PyCharm

__author__ = 'Exchris Tsai'

# 利用ellipse和rectangle画图

if __name__ == '__main__':
    from tkinter import *
    canvas = Canvas(width = 400,height = 600,bg = 'white')
    left = 20
    right = 50
    top = 50
    num = 15
    for i in range(num):
        canvas.create_oval(250 - right,250 - left,250 + right,250 + left)
        canvas.create_oval(250 - 20,250 - top,250 + 20,250 + top)
        canvas.create_rectangle(20 - 2 * i,20 - 2 * i,10 * (i + 2),10 * ( i + 2))
        right += 5
        left += 5
        top += 10

    canvas.pack()
    mainloop()