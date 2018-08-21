"""
Created on 七月 31 2017
@author: dev.erxuan@gmail.com
"""
# -*- coding: utf-8 -*-
# @description: 抓取景甜吧的图片

from bs4 import BeautifulSoup
import re
import requests
import os, sys

print('把该py文件抓取的图片保存至D盘images目录下tieba文件夹jingtian目录下')
localpath = "D:\\images\\tieba\jingtian"

print("判断本地文件中是否有该文件夹")
if not os.path.exists(localpath):
    os.makedirs(localpath)
    print("创建成功")
else:
    print("目录已存在为", localpath)

# 抓取html内容
weburl = "http://tieba.baidu.com/photo/p?kw=%E6%99%AF%E7%94%9C&tid=2068732255&pic_id=b77b7ef40ad162d9c8dd655e11dfa9ec8a13cd30";
response = requests.get(weburl).content

# BeautifulSoup解析html内容
soup = BeautifulSoup(response, 'lxml')



