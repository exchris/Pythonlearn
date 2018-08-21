#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/25 0025 上午 11:59
# @Author  : Exchris Tsai
# @Site    : 
# @File    : example57.py
# @Software: PyCharm

# 题目:学用line画直线

__author__ = 'Exchris Tsai'

if __name__ == "__main__":
    from tkinter import *

    canvas = Canvas(width=300, height=300, bg='red')
    canvas.pack(expand=YES, fill=BOTH)
    x0 = 263
    y0 = 263
    y1 = 275
    x1 = 275
    for i in range(19):
        canvas.create_line(x0, y0, x0, y1, width=1, fill='green')
        x0 = x0 - 5
        y0 = y0 - 5
        x1 = x1 + 5
        y1 = y1 + 5

    x0 = 263
    y1 = 275
    y0 = 263
    for i in range(21):
        canvas.create_line(x0, y0, x0, y1, fill='yellow')
        x0 += 5
        y0 += 5
        y1 += 5

    mainloop()