'''
Created on July 28th 2017

@author: dev.erxuan@gmail.com

'''
# -*- coding: utf-8 -*-
import urllib.request

url = 'http://www.python.org'
proxies = {'http':'http://127.0.0.1:8086/'}
r = urllib.request.urlopen(url)    # 选择不适应代理服务器打开
print("Info:")
print(r.info)

print("getcode():")
print(r.getcode())

print("geturl():")
print(r.geturl())

# 对豆瓣的一个URL https://api.douban.com/v2/book/2129650进行抓取,并返回响应

with urllib.request.urlopen("https://api.douban.com/v2/book/2129650") as wf:
    data = wf.read()    # 数据
    print("Status:")
    print("Status:", wf.status, wf.reason)

    for k, v in wf.getheaders():

        print('%s : %s' %(k, v))
    print("Data:")
    print('Data:', data.decode('utf-8'))