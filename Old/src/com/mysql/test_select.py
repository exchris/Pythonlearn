# coding:utf8
import MySQLdb

try:

	conn = MySQLdb.Connect(
		host = '127.0.0.1',
		port = 3306,
		user = 'root',
		passwd = 'root',
		db = 'ttpaobu',
		charset = 'utf8'
	)
	cursor = conn.cursor()

	sql = "select uid,username from user limit 10"
	cursor.execute(sql)
	
	print("记录条数有%d"%cursor.rowcount)
	
	rs = cursor.fetchone()
	print(rs)
	
	rs = cursor.fetchmany(3)
	print(rs)
	
	rs = cursor.fetchall()
	for row in rs:
		print("uid=%s,username=%s"%row)
		
	cursor.close()
	conn.close()
except Exception as e:
	print("数据库连接失败")




