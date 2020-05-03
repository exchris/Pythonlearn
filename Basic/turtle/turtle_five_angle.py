#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
绘制五角星
@author dev.erxuan@gmail.com
@file turtle_five_angle.py
@software PyCharm
@date 2020/4/23 22:29
"""

import turtle, time

# 绘制画布范围
turtle.setup(1500, 1200, 0, 0)
# 设置画笔大小
turtle.pensize(5)
# 设置画笔颜色
turtle.pencolor("pink")
# 设置画笔填充颜色
turtle.fillcolor("red")

# 准备开始填充图形
turtle.begin_fill()

for _ in range(5):
    # 向当前画笔方向移动50px
    turtle.forward(400)
    # 顺时针转动36°角
    turtle.right(44)

# 结束填充图形
turtle.end_fill()
# 延迟5s
time.sleep(5)

if __name__ == "__main__":
    pass
