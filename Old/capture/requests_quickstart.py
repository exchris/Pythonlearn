
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/27 0027 上午 10:00
# @Author  : Exchris Tsai
# @Site    : 
# @File    : requests_quickstart.py
# @Software: PyCharm

__author__ = 'Exchris Tsai'

# 发送请求
# 使用Requests发送网络请求非常简单
# 一开始到导入Requests模块
import requests
# 尝试获取某个网页。获取Github的公共时间线
r = requests.get(r'https://github.com/timeline.json')

# Requests简便的API意味着所有HTTP请求类型都是显而易见的。
# 例如,你可以这样发送一个HTTP POST请求
# r = requests.post("http://httpbin.org/post")
# r = requests.put("http://httpbin.org/put)
# r = requests.delete("http://httpbin.org/delete")
# r = requests.head("http://httpbin.org/get")
# r = requests.options("http://httpbin.org/get")

# 传递URL参数

# payload = {'key1':'value1', 'key2':'value2'}
# r = requests.get("http://httpbin.org/get", params=payload)
# print(r.url) http://httpbin.org/get?key2=value2&key1=value1

# payload = {'key1':'value1','key2':['value2','value3']}
# r = requests.get('http://httpbin.org/get', params=payload)
# print(r.url) http://httpbin.org/get?key1=value1&key2=value2&key2=value3

# 响应内容
print("Text:")
print(r.text)
print("Content:")
print(r.content)
print("Json():")
print(r.json())