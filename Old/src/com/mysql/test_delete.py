# -*- coding:UTF-8 -*-
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost","root","root","ttpaobu" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL删除语句
sql = "DELETE FROM EMPLOYEE WHERE AGE > \
      '%d'" %(20)
    
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交修改
    db.commit()
    # 返回受影响行数
    print(cursor.rowcount)
except:
    # 发送错误时回滚
    db.rollback()
    print("删除失败")