#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
@author dev.erxuan@gmail.com
@file flower.py.py
@software PyCharm
@date 2020/4/20 22:34
"""
import turtle
myPen = turtle.Pen()
myPen.speed(0)
myPen.pensize()
myPen.pencolor("red")
myPen.penup()
myPen.goto(-50, -50)
myPen.down()
for i in range(12):
    myPen.pencolor("red")
    myPen.circle(100, extent=30)
    myPen.fillcolor("yellow")
    myPen.begin_fill()
    myPen.pencolor("black")
    myPen.right(60)
    myPen.forward(80)
    myPen.right(60)
    myPen.forward(80)
    myPen.right(120)
    myPen.forward(80)
    myPen.right(60)
    myPen.forward(80)
    myPen.end_fill()
    myPen.right(60)
myPen.hideturtle()
turtle.done()

if __name__ == "__main__":
    pass
