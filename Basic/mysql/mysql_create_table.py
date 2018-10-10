#!/usr/bin/python
# -*- coding:utf-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect("127.0.0.1", "root", "root", "test")

# 使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()

# 使用execute()方法执行SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
sql = """
    CREATE TABLE EMPLOYEE (
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1),
        INCOME FLOAT
    )
"""

# 使用execute()执行SQL语句
cursor.execute(sql)

# 关闭数据库连接
db.close()