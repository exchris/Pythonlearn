# -*- coding:UTF-8 -*-
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost","root","root","ttpaobu" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 \
      WHERE SEX='%c'"%('M')

try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
    # 返回受影响行数
    print(cursor.rowcount)
except:
    # 发送错误时回滚
    db.rollback()

# 关闭游标
cursor.close()
# 关闭数据库连接
db.close()