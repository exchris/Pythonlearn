#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/26 0026 下午 5:06
# @Author  : Exchris Tsai
# @Site    : 
# @File    : urllibtest.py
# @Software: PyCharm

__author__ = 'Exchris Tsai'

import urllib
import urllib.request
import re

def download_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2)'
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}

    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    data = response.read()
    return data

def get_image(html):
    regx = r'http://[\S]*\.jpg'
    pattern = re.compile(regx)
    get_img = re.findall(pattern, repr(html)) # repr用来转换表达式类型字符串
    num = 0
    try:
        for img in get_img:
            image = download_page(img)  # 将每个img链接重新解析
            
            with open('%s.jpg' % num, 'wb') as fp:
                fp.write(image)
                num += 1
                print('正在下载第%s张图片' % num)
    except:
        print("链接错误")

    return

url = 'http://pic.yesky.com/451/106166451.shtml'
html = download_page(url)
get_image(html)