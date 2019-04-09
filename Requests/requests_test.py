#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

# 最基本的抓取
import requests

response = requests.get("http://www.baidu.com/")
content = response.content
print("response headers:", response.headers)
print("content:", content.decode("utf-8"))