# -*- coding:UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost","root","root","ttpaobu")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 创建数据表SQL语句
try:
    sql = """
    # 如果数据库已经存在使用execute()方法删除表。
    drop table if exists EMPLOYEE;
    CREATE TABLE EMPLOYEE(
       FIRST_NAME CHAR(20) NOT NULL,
       LAST_NAME CHAR(20),
       AGE INT,
       SEX CHAR(1),
       INCOME FLOAT(5)
    );
    """
    cursor.execute(sql)
    print("创建成功")
    cursor.close()
    db.close()
except Exception as e:
    print("创建失败")