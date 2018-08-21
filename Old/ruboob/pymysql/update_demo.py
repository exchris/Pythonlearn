# -*- coding:utf-8 -*-
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","testuser","test123","TESTDB" )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL更新语句
sql = "UPDATE EMPLOYEE SET age = age + 1 \
      WHERE sex = '%c'" %('M')

try:
    # 执行SQL语句
    cursor.execute(sql)
    # 返回受影响的行数
    print(db.affected_rows())
    # 提交到数据库执行
    db.commit()
except:
    # 发送错误时回滚
    db.rollback()

# 关闭游标
cursor.close()
# 关闭数据库连接
db.close()