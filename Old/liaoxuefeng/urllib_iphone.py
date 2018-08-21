#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/26 0026 下午 2:39
# @Author  : Exchris Tsai
# @Site    : 
# @File    : urllib_iphone.py
# @Software: PyCharm

__author__ = 'Exchris Tsai'

from urllib import request

req = request.Request(r'http://www.douban.com/')
req.add_header('User-Agent','Mozilla/6.0 (iPhone:CPU iPhone 0S 8_0 like Mac OS X)\
 AppleWebkit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' %(k, v))
    print('模拟iPhone6登录数据如下:')
    print('Data:', f.read().decode('utf-8'))