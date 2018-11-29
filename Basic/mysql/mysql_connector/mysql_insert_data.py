#!/usr/bin/python
# -*- coding:utf-8 -*-

import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="root",
    database="runoob"
)

mycursor = mydb.cursor()

sql = "INSERT INTO sites(name, url)VALUES(%s, %s)"
val = ("RUNOOB", "https://www.runoob.com")
mycursor.execute(sql, val)

mydb.commit()  # 数据表内容有更新，必须使用到该语句
print(mycursor.rowcount, "记录插入成功。")
print("1 条记录已插入, ID:", mycursor.lastrowid)
