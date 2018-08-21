#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/26 0026 下午 4:29
# @Author  : Exchris Tsai
# @Site    : 
# @File    : urllib_two.py
# @Software: PyCharm

__author__ = 'Exchris Tsai'

from urllib import request
from http import cookiejar

"""
url = 'http://www.baidu.com/'
req = request.Request(url,headers= {
'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
})
oper = request.urlopen(req)
data = oper.read()
print(data.decode('utf-8'))
"""

def saveFile(data):
    save_path = 'baidu.txt'
    f_obj = open(save_path, 'wb') # wb表示打开方式
    f_obj.write(data)
    f_obj.close()

# head: dict of header
def makeMyOpener(head={
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}):
    cj = cookiejar.CookieJar()
    opener = request.build_opener(request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener


oper = makeMyOpener()
uop = oper.open('http://www.baidu.com/', timeout=1000)
data = uop.read()

saveFile(data)
