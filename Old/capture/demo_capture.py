# -*- coding:utf-8 -*-
import urllib
import urllib.request

url = r"http://www.douban.com/"
response = urllib.request.Request(url)
webPage = urllib.request.urlopen(response)
data = webPage.read()

# 将data文件写入到douban.txt中
with open('douban.txt', 'wb') as fb:
	fb.write(data)
	fb.close()

print(type(webPage))
print(webPage.geturl())
print(webPage.info())
print(webPage.getcode())