#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

"""
'r' 读模式
'w' 写模式
'a' 追加模式
'b' 二进制模式
'+' 读/写模式
'rb' 读取二进制文件
"""

"""
f = open(r'qiye.txt')
print(f.read())
# 关闭对文件的引用。文件完毕后必须关闭，因为文件对象会占用操作系统资源，影响系统的IO操作
f.close()
"""

try:
    f = open(r'qiye.txt')
    print(f.read)
finally:
    if f:
        f.close()

with open(r'qiye.txt') as fileReader:
    for line in fileReader.readline():
        print(line.strip())

# 写入文件
f = open(r'qiye.txt', 'w')
f.write('qiye')
f.close()

with open(r'qiye.txt', 'w') as fileWriter:
    fileWriter.write('qiye')
