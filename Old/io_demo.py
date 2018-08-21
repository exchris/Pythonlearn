"""
Created on 八月 03 2017
@author: dev.erxuan@gmail.com
"""
# -*- coding: utf-8 -*-

import os # 导入os模块

print(os.getcwd()) # 获得当前路径
print(os.listdir()) # 列出目录下所有文件和文件夹
print(os.mkdir('hahaha')) # 创建一个名为hahaha的目录
print(os.rmdir('c')) # 删除一个名为c的目录
print(os.rename('abc.txt', 'readme.txt')) # 重命名一个文件

