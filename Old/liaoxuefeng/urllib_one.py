#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/26 0026 下午 4:54
# @Author  : Exchris Tsai
# @Site    : 
# @File    : urllib_one.py
# @Software: PyCharm

__author__ = 'Exchris Tsai'

import urllib
import urllib.request

def get_image(url):

    request = urllib.request.Request(url) #构建请求
    response = urllib.request.urlopen(request) # 获取服务器响应
    get_img = response.read() # 读取图片
    with open('001.jpg', 'wb') as fp:
        fp.write(get_img)
        print('图片下载完成')
        fp.close()
    return

url = 'http://p2.123.sogoucdn.com/imgu/2016/10/20161019124600_428.jpg'
get_image(url)