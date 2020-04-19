#! /usr/bin/python
# -*- coding:utf-8 -*-
# coding: utf-8

"""
第一步，获取页面
import requests
link = "http://www.santostang.com/"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
r = requests.get(link, headers=headers)
print(r.text)
print(r.status_code)
"""

"""
第二步：提取需要的数据
"""
# import requests
# # 从bs4这个库中导入BeautifulSoup
# from bs4 import BeautifulSoup
# link = "http://www.santostang.com/"
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
# r = requests.get(link, headers=headers)
# # 使用BeautifulSoup解析这段代码
# soup = BeautifulSoup(r.text, "lxml")
# print(soup)
# title = soup.find("h1", class_="post-title").a.text.strip()
# print(title)

"""
第三步：存储数据
"""
import requests
# 从bs4这个库中导入BeautifulSoup
from bs4 import BeautifulSoup
link = "http://www.santostang.com/"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}
r = requests.get(link, headers=headers)
print(r.text)
# 使用BeautifulSoup解析这段代码
soup = BeautifulSoup(r.text, "lxml")
title = soup.find("h1", class_="post-title").a.text.strip()
print(title)
# 存储数据
with open('title.txt', "a+") as f:
    f.write(title)
    f.close()


