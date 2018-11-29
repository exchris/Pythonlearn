#!/usr/bin/python
# -*- coding:utf-8 -*-

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="runoob"
)
mycursor = mydb.cursor()

sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = [
    ('Google', 'https://www.google.com'),
    ('Github', 'https://www.github.com'),
    ('Taobao', 'https://www.taobao.com'),
    ('stackoverflow', 'https://www.stackoverflow.com/')
]

mycursor.executemany(sql, val)

mydb.commit()  # 数据表内容有更新，必须使用到该语句

print(mycursor.rowcount, "记录插入成功。")
