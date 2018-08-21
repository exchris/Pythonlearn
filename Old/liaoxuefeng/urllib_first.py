#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/26 0026 下午 3:49
# @Author  : Exchris Tsai
# @Site    : 
# @File    : urllib_first.py
# @Software: PyCharm

__author__ = 'Exchris Tsai'

from urllib import request, parse
from collections import deque
import re

"""
url = r"http://www.ifitshow.com"

data1 = request.urlopen(url).read()

a = request.urlopen(url)
type(a)
# <class 'http.client.HTTPResponse'>

a.geturl()
# 'http://www.baidu.com/s?word=Jecvay'

a.info()
# <http.client.HTTPMessage object at 0x03272250>

a.getcode()
# 200
"""

"""
# print(data.decode('utf-8'))

# Python 简单处理URL,抓取百度上面搜索关键词为Jecvay Notes的网页
data = {}
data['word'] = 'Jecvay Notes'

# 将data转换为'word=Jecvay+Notes',
url_values = parse.urlencode(data)
urls = "http://www.baidu.com/s?"
full_url = urls + url_values
# http://www.baidu.com/s?word=Jecvay+Notes

data = request.urlopen(full_url).read()
data = data.decode('utf-8')
# print(data)
"""

"""
# Python 的队列
queue = deque(["Eric", "John", "Michael"])
queue.append(["Terry"]) # Terry入队
queue.append(["Graham"]) # Graham入队
# 输出: "Eric"
# print(queue.popleft()) # 队首元素出队

# 输出 'John'
# print(queue.popleft()) # 队首元素出队

# deque(['Michael', ['Terry'], ['Graham']])
# print(queue) # 队列中剩下的元素

basket = {'apple','orange','apple','pear','orange','banana'}
# print(basket) # 这里演示的是去重功能
# {'orange','banana','pear','apple'}

# print('orange' in basket) # 快速判断元素是否在集合内
# True

# print('crabgrass' in basket)
# False
"""

"""
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # 集合a中包含元素
{'r', 'd', 'b'}
>>> a | b                              # 集合a或b中包含的所有元素
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # 集合a和b中都包含了的元素
{'a', 'c'}
>>> a ^ b                              # 不同时包含于a和b的元素
{'r', 'd', 'b', 'm', 'z', 'l'}
"""

queqe = deque()
visited = set()

url = 'http://news.dbanotes.net' # 入口页面,可以换成别的

queqe.append(url)
cnt = 0

while queqe:
    url = queqe.popleft() # 队首元素出队
    visited |= {url} # 标记为已访问

    print('已经抓取:' + str(cnt) + ' 正在抓取 < ---' + url)
    cnt += 1

    # 添加超时跳过功能
    urlop = request.urlopen(url, timeout=2)
    if 'html' not in urlop.getheader('Content-Type'):
        continue

    # 避免程序异常中止,用try...catch处理异常
    try:
        data = urlop.read().decode('utf-8')
    except:
        continue

    # 正则表达式提取页面中所有队列,并判断是否已经访问过,然后加入待爬队列
    linkre = re.compile('href=\"(.+?)\"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queqe.append(x)
            print('加入队列 ---> ' + x)
