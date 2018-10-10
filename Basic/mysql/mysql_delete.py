#!/usr/bin/python
# -*- coding:utf-8 -*-

# 删除操作用于删除数据表中的数据
import pymysql

# 打开数据库连接
db = pymysql.connect("127.0.0.1", "root", "root", "test")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 删除语句
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" %(20)

try:
    # 执行SQL语句
    affected_rows = cursor.execute(sql)
    # 提交修改
    db.commit()
    print("返回受影响的行数为 %d" % affected_rows)
except:
    # 发生错误时回滚
    db.rollback()
# 关闭连接
db.close()