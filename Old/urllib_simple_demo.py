'''
Created on July 31st 2017

@author: dev.erxuan@gmail.com

'''
# -*- coding:utf-8 -*-
# @description: 一个简单的示例爬虫

from urllib import request
url = r"http://www.douban.com"
webPage = request.urlopen(url)
data = webPage.read().decode('utf-8')

print(data)

print("type:\n")
print(type(webPage))

print("info:\n")
print(webPage.info)

print("url地址:\n")
print(webPage.geturl())

print("code码\n")
print(webPage.getcode())
