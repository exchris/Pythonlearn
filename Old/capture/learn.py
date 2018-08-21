#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/28 0028 下午 2:34
# @Author  : Exchris Tsai
# @Site    : 
# @File    : learn.py
# @Software: PyCharm

__author__ = 'Exchris Tsai'

from bs4 import BeautifulSoup
with open("learn.html", "r") as ecological_pyramid:
    soup = BeautifulSoup(ecological_pyramid, "lxml")
    producer_entries = soup.find("ul")
    print(producer_entries.li.div.string)