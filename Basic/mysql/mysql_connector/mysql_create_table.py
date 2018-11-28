#!/usr/bin/python
# -*- coding:utf-8 -*-

import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="root",
    database="runoob"
)

mycursor = db.cursor()
mycursor.execute("use runoob")
mycursor.execute("CREATE TABLE IF NOT EXISTS sites(name varchar(255), url varchar(255))")
# 主键设置
mycursor.execute("ALTER TABLE sites ADD COLUMN id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY")

mycursor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")