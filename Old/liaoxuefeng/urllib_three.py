#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/26 0026 下午 4:41
# @Author  : Exchris Tsai
# @Site    : 
# @File    : urllib_three.py
# @Software: PyCharm

__author__ = 'Exchris Tsai'

import requests
from bs4 import BeautifulSoup as BS

response = requests.get("http://jecvay.com")
soup = BS(response.text, "html5lib")
print(soup.title.text)
print(soup.body.text)

for x in soup.findAll("a"):
    print(x['href'])

soup1 = BS(requests.get("http://www.zhihu.com").text)
print(soup1.find("input",{"name":"_xsfr"})['value'])
