#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/25 0025 下午 3:35
# @Author  : Exchris Tsai
# @Site    : 
# @File    : example58.py
# @Software: PyCharm

# 画图,学用rectangle画方形
# rectangle(int left, int top, int right, int bottom)
# 参数说明：(left ，top )为矩形的左上坐标，(right,bottom)为矩形的右下坐标，两者可确定一个矩形的大小

__author__ = 'Exchris Tsai'

if __name__ == '__main__':
    from tkinter import *
    root = Tk()
    root.title('Canvas')
    canvas = Canvas(root, width = 400, height = 400, bg = 'yellow')
    x0 = 263
    y0 = 263
    y1 = 275
    x1 = 275
    for i in range(19):
        canvas.create_rectangle(x0, y0, x1, y1)
        x0 -= 5
        y0 -= 5
        x1 += 5
        y1 += 5

    canvas.pack()
    root.mainloop()