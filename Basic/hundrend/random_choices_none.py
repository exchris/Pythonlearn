#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
求在一个包含9个数字的数列中产生一个随机的、包含3个数字的新数列
@author dev.erxuan@gmail.com
@file random_choices_none.py
@software PyCharm
@date 2020/4/20 23:00
"""
import random

list_1 = [2, 3, 4, 1, 5, 7, 6, 9, 8]
# 随机取列表中的一个数
print(random.choice(list_1))
a = random.choices(list_1, k=3)
print(a)
if __name__ == "__main__":
    pass
