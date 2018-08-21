# -*- coding:utf-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "ttpaobu")

# 使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()

# 使用execute() 方法执行SQL查询
cursor.execute("select version()")

# 使用fetchone()方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s" % data)

# 关闭游标
cursor.close()

# 关闭数据库连接
db.close()