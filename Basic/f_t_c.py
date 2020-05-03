#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
华氏温度转换为摄氏温度
@author dev.erxuan@gmail.com
@file f_t_c.py
@software PyCharm
@date 2020/4/24 21:47
"""
f = float(input('请输入华氏温度'))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' %(f, c))

if __name__ == "__main__":
    pass
