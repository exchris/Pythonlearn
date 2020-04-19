#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
导入.xlsx文件
@author dev.erxuan@gmail.com
@file read_excel.py
@software PyCharm
@date 2020/4/18 15:31
"""
import pandas as pd

"""
路径前面加r;
sheet_name: 指定具体Sheet的名字，不指定默认导入的是第一个Sheet的文件
index_col: 指定行索引
header: 设置列索引
"""


def test_read_excel(file):
    # 使用第一行作为列索引
    df = pd.read_excel(file, sheet_name="Sheet1", index_col=0, header=0)
    print(df)

    # 使用第二行作为列索引
    df = pd.read_excel(file, sheet_name="Sheet1", index_col=0, header=1)
    print(df)

    # 使用默认从0开始的数作为列索引
    df = pd.read_excel(file, sheet_name="Sheet1", index_col=0, header=None)
    print(df)

    # 本地文件列数太多，通过设定usecols参数来指定要导入的列
    df = pd.read_excel(file, usecols=[0])
    print(df)
    # 给usecols参数具体的某个值，表示要导入第几列，同样是从0开始计数，也可以以列表的形式传入多个值，表示要传入某些列
    df = pd.read_excel(file, usecols=[0, 2])
    print(df)

    # head()方法控制要显示哪些行
    # 默认展示前5行
    print(df.head())
    # 只展示前2行
    print(df.head(2))


file = r"e:\git\pythonlearn\files\test.xlsx"
df = pd.read_excel(file)
# 利用shape获取数据表的大小
print(df.shape)
# 利用info获取数据类型
print(df.info())
# 利用describe获取数值分布情况
print(df.describe())

# 新建一个含有多列数值类型字段的DataFrame
df = pd.DataFrame([[20, 5000, 2], [25, 8000, 3], [30, 9000, 3], [28, 7000, 2]], columns=["年龄", "收入", "家庭"])
print(df)
print(df.describe())
