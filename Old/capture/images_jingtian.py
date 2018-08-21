#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/27 0027 上午 10:28
# @Author  : Exchris Tsai
# @Site    :
# @File    : images_tiba.py
# @Software: PyCharm

__author__ = 'Exchris Tsai'

import requests
from bs4 import BeautifulSoup as BS
import os
import sys
import re

print(u'把改py文件抓取的图片保存到本地D盘images目录下tieba文件夹中')
localpath = u'D:\\images\\tieba\\'
if not os.path.exists(localpath):
    os.makedirs(localpath)
    print('创建成功')
else:
    print('路径为', localpath)

# 抓取html内容
f= requests.get('http://tieba.baidu.com/p/5244924952').content

# BeautifulSoup 解析html内容
s = BS(f, 'html.parser')

# 设置抓取图片title为"景甜"
title = "景甜"
newpath = localpath+title
print('图片保存的新路径为:', newpath)

# 判断新路径是否存在
if not os.path.exists(newpath):
    os.makedirs(newpath)
    print('创建成功', newpath)
else:
    print('路径为', newpath)

# 查询该页面中的所有图片在div标签的img图片
s_imgs = s.find_all('img', class_='BDE_Image')

i = 0
for s_img in s_imgs:
    img_url = s_img['src']
    img_content = requests.get(img_url).content
    file_name = str(i) + '.jpg'
    with open(newpath+'/'+file_name, 'wb') as wf:
        wf.write(img_content)
        wf.close()
    i += 1


sys.exit()
