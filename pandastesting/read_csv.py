#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
@description 导入.csv文件
@author dev.erxuan@gmail.com
@file read_csv.py
@software PyCharm
@date 2020/4/18 15:53
"""
import pandas as pd
"""
sep: 分隔符
nrows: 指明读取行数
encoding: 指定csv文件格式
"""
df = pd.read_csv(r"e:\git\pythonlearn\files\test.csv", sep=" ")
print(df)

if __name__ == "__main__":
    pass
