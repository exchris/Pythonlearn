#!/usr/bin/python
# -*- coding:utf-8 -*-
import mysql.connector

mydb = mysql.connector.connect(
    host='127.0.0.1',  # 数据库主机地址
    user='root',  # 数据库用户名
    passwd='root'  # 数据库密码
)
print(mydb)
