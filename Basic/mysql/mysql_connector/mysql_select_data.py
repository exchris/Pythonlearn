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

mycursor.execute("SELECT * FROM sites")

myresult = mycursor.fetchall()  # fetchall() 获取所有记录

for x in myresult:
    print(x)
