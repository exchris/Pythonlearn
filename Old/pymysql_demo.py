"""
Created on 八月 01 2017
@author: dev.erxuan@gmail.com
"""
# -*- coding: utf-8 -*-
import pymysql

# 连接数据库
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='root',db='leetcode',charset='utf8')

# 获取游标
cursor = conn.cursor()

# 插入数据
insert_sql = "INSERT INTO trade(name, account, saving) VALUES ('%s', '%s', '%.2f')"
data = ('雷军', '13516243895', 10000)
cursor.execute(insert_sql % data)
conn.commit()
print('成功插入',cursor.rowcount,'条数据')

# 修改数据
update_sql = "UPDATE trade SET saving = '%.2f' WHERE account = '%s'"
data = (8888, '13516243895')
cursor.execute(update_sql % data)
conn.commit()
print('成功修改',cursor.rowcount,'条数据')

# 查询数据
select_sql = "SELECT name,saving FROM trade WHERE account = '%s'"
data = ('13516243895',)
cursor.execute(select_sql % data)
for row in cursor.fetchall():
    print("Name:%s\tSaving:%.2f" %row)
print('共查找出',cursor.rowcount,'条数据')

# 删除数据
delete_sql = "DELETE FROM trade WHERE account = '%s' LIMIT %d"
data = ('13516243895', 1)
cursor.execute(delete_sql % data)
conn.commit()
print('成功删除',cursor.rowcount,'条数据')

# 事务处理
sql_1 = "UPDATE trade SET saving = saving + 1000 WHERE account = '18012345678' "
sql_2 = "UPDATE trade SET expend = expend + 1000 WHERE account = '18012345678' "
sql_3 = "UPDATE trade SET income = income + 2000 WHERE account = '18012345678' "

try:
    cursor.execute(sql_1)  # 储蓄增加1000
    cursor.execute(sql_2)  # 支出增加1000
    cursor.execute(sql_3)  # 收入增加2000
except Exception as e:
    conn.rollback()  # 事务回滚
    print('事务处理失败', e)
else:
    conn.commit()  # 事务提交
    print('事务处理成功', cursor.rowcount)

# 关闭连接
cursor.close()
conn.close()


