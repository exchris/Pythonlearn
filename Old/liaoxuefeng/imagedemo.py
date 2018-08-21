#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/26 0026 下午 5:54
# @Author  : Exchris Tsai
# @Site    : 
# @File    : imagedemo.py
# @Software: PyCharm

__author__ = 'Exchris Tsai'

import requests
import os
import urllib
import urllib.request
from bs4 import BeautifulSoup as BS

path = 'd:/images' #
title = 'girls'
new_path = os.path.join(path, title)
if not os.path.isdir(new_path):
    os.makedirs(new_path)

url = "http://lusparkle0420.lofter.com/"
r = requests.get(url)
soup = BS(r.text, 'html.parser')

n = 0
for link in soup.find_all('a'):
    if n > 100:
        break
    n = n + 1
    print(link.get('href'))
    urllib.request.urlretrieve(link)

print("----------------")
print('link sums:',n)

