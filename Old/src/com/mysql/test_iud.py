import MySQLdb

conn = MySQLdb.Connect(
	host = '127.0.0.1',
	port = 3306,
	user = 'root',
	passwd = 'root',
	db = 'ttpaobu',
	charset = 'utf8'
)

cursor = conn.cursor()

sql_insert = "insert into user(uid,username) values(10,'name10')"
sql_update = "update user set username='name91' where uid=9"
sql_delete = "delete from user where userd<3"

try :
	cursor.execute(sql_insert)
	print(cursor.rowcount)

	cursor.execute(sql_update)
	print(cursor.rowcount)

	cursor.execute(sql_delete)
	print(cursor.rowcount)

	conn.commit()
except Exception as e:
	print(e)
	conn.rowback()
	
cursor.close()
conn.close()


