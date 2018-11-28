import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="runoob"
)
mycursor = mydb.cursor()

sql = "SELECT * FROM sites WHERE name ='RUNOOB'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

sql = "SELECT * FROM sites WHERE url LIKE '%oo%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# 为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义查询的条件：
sql = "SELECT * FROM sites WHERE name = %s"
na = ("RUNOOB",)

mycursor.execute(sql, na)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# order by
sql = "SELECT * FROM sites ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
