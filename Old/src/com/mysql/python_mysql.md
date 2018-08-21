# DB API - 数据库连接对象connection

- 连接对象:建立Python客户端与数据库的网络连接
- 创建方法:MySQLdb.Connect(参数)

|   参数名   |  类型  | 说明          |
| :-----: | :--: | ----------- |
|  host   | 字符串  | MySQL服务器地址  |
|  port   |  数字  | MySQL服务器端口号 |
|  user   | 字符串  | 用户名         |
| passwd  | 字符串  | 密码          |
|   db    | 字符串  | 数据库名称       |
| charset | 字符串  | 连接编码        |

连接实例:

```
import MySQLdb

conn = MySQLdb.Connect(
	host = '127.0.0.1',
	port = 3306,
	user = 'root',
	passwd = 'root',
	db = 'learn',
	charset = 'utf8'
)

cursor = conn.cursor()

print(conn)
print(cursor)

cursor.close()
conn.close()
```

# DB API - 数据库游标对象cursor

- 游标对象
- cursor对象支持的方法

| 参数名                | 说明                       |
| ------------------ | ------------------------ |
| execute(op[,args]) | 执行一个数据库查询和命令             |
| fetchone()         | 取得结果集的下一行                |
| fetchmany(size)    | 获取结果集的下几行                |
| fetchall()         | 获取结果集中剩下的所有行             |
| rowcount           | 最近一次execute返回的数据的行数或影响行数 |
| close()            | 关闭游标对象                   |

- fetch*() 方法: 移动rownumber,返回数据

# 实例演示 - select查询数据
```
import MySQLdb

conn = MySQLdb.Connect(
	host = '127.0.0.1',
	port = 3306,
	user = 'root',
	passwd = 'root',
	db = 'learn',
	charset = 'utf8'
)

cursor = conn.cursor()

sql = "select * from user limit 10"
cursor.execute(sql)

rs = cursor.fetchall()
for row in rs:
	print "userid=%s,username=%s",%row
	
cursor.close()
conn.close()
```

# 实例演示 - insert/update/delete更新数据库

### 事务

- 事务:访问和更新数据库的一个程序执行单元
  - 原子性:事务中包括的诸操作要么都做,要么都不做
  - 一致性:事务必须使数据库从一致性状态变到另一个一致性状态
  - 隔离性:一个事务的执行不能被其他事务干扰
  - 持久性:事务一旦提交,它对数据库的改变就是永久性的
- 开发中怎样使用事务?
  - 关闭自动commit:设置conn.autocommit(False)
  - 正常结束事务 :conn.commit()
  - 异常结束事务:conn.rollback()


```
import MySQLdb

conn = MySQLdb.Connect(
	host = '127.0.0.1',
	port = 3306,
	user = 'root',
	passwd = 'root',
	db = 'learn',
	charset = 'utf8'
)

cursor = conn.cursor()

sql_insert = "insert into user(userid,username) values(10,'name10')"
sql_update = "update user set username='name91' where userid=9"
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
```

# 银行转账实例 - 账户A给账户B转账100元

