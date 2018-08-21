# -*- coding:utf-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "ttpaobu")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = """INSERT INTO employee(first_name,
        last_name,age,sex,income)
        values('Mac','Mohan',20,'M',2000)"""

"""
# SQL 插入语句
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('Mac', 'Mohan', 20, 'M', 2000)
"""

try:
    # 执行sql语句
    cursor.execute(sql)
    # 返回受影响行数
    print(db.affected_rows())
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# 关闭游标
cursor.close()

# 关闭数据库连接
db.close()