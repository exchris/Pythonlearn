#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
@author dev.erxuan@gmail.com
@file read_sql.py
@software PyCharm
@date 2020/4/18 15:59
"""

# 导入pymysql模块
import pymysql
# 导入pandas模块
import pandas as pd

# 创建连接
# user: 用户名
# password: 密码
# host: 数据库地址/本地使用localhost
# db: 数据库名
# charset: 数据库编码，一般为UTF-8
eng = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='root',
    db='python_db',
    charset='utf8'
)
sql = "SELECT * FROM memberinfo"
df = pd.read_sql(sql, eng)
print(df)

if __name__ == "__main__":
    pass
