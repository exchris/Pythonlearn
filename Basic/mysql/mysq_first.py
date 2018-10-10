#!/usr/bin/python
# -*- coding:utf-8 -*-

# 链接MySQL的TESTDB数据库

import pymysql

# 打开数据库连接
db = pymysql.connect("127.0.0.1", "root", "root", "test")

# 使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()

# 使用execute()方法执行SQL查询
cursor.execute("SELECT VERSION()")

# 使用fetchone()方法获取单条数据
data = cursor.fetchone()

print("Database Version : %s" % data)

# 关闭数据库连接
db.close()
