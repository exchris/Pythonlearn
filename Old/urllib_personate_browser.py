'''
Created on July 31st 2017

@author: dev.erxuan@gmail.com

'''
# -*- coding:utf-8 -*-
# @description: 伪装成浏览器来爬网页

from urllib import request
weburl = r"http://www.douban.com/"
webheader = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}

response = request.Request(url=weburl, headers=webheader)
webPage = request.urlopen(response)
data = webPage.read().decode('utf-8')

print(data)

print(type(webPage))
print(webPage.geturl())
print(webPage.info())
print(webPage.getcode())