#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 0028 上午 10:56
# @Author  : Exchris Tsai
# @Site    : 
# @File    : fileopen.py
# @Software: PyCharm

__author__ = 'Exchris Tsai'

f = open('1.txt', 'w') # 写入方式,如果文件存在清空文件内容,不存在创建文件
f.write("test cxm")
f.close()

f = open('hello.py', 'a') # 追加和读写方式打开,如果不存在创建
f.write("\nprint('write test')")
f.close()

# 读写模式
f = open('hello.py', 'r+') # 读追加,在最前面
f.write("\nprint('rw mode'")
f.close()

f = open('hello.py', 'w+') # 读追加,清空所有内容然后新加
f.write("\nprint('wr, mode')")
f.close()


