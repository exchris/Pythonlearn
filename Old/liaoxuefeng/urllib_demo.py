#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/26 0026 下午 2:12
# @Author  : Exchris Tsai
# @Site    :
# @File    : urllib.py
# @Software: PyCharm

__author__ = 'Exchris Tsai'

"""
Get
urllib的request模块可以非常方便地抓取URL内容,也就是发送一个GET请求到指定的页面,然后返回HTTP的响应:
例如,对豆瓣的一个URL https://api.douban.com/v2/book/2129650 进行抓取,并返回响应:
"""

from urllib import request

"""
注意:仿坑处:使用urllib时文件名不能是urllib
"""

with request.urlopen(r'https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' %(k, v))

    print()
    print('Data', data.decode('utf-8'))