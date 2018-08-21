#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/27 0027 下午 1:49
# @Author  : Exchris Tsai
# @Site    : 
# @File    : first.py
# @Software: PyCharm

__author__ = 'Exchris Tsai'

import requests ## 导入requests
from bs4 import BeautifulSoup ## 导入bs4中的BeautifulSoup
import os

## 浏览器请求头(大部分网站没有这个请求头会报错、请务必加上)
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/59.0.3071.115 Safari/537.36"}

all_url = 'http://www.mzitu.com/all' ## 开始的URL地址

## 使用requests中的get方法来获取all_url的内容headers为上面设置的请求头
start_html = requests.get(all_url, headers=headers)

## 打印出start_html,content是二进制的数据,一般用于下载图片、视频、音频、等多媒体内容,对于打印网页内容请使用text

## 使用BeautifulSoup来解析我们获取到的网页('lxml'是指定的解析器)
Soup = BeautifulSoup(start_html.text, 'lxml')

# 使用BeautifulSoup解析网页过后就可以找标签呐!(find_all是查找指定网页内的所有标签的意思,find_all返回的是一个列表)
# li_list = Soup.find_all('li')
# for li in li_list:
#    print(li)

## 意思是先查找class为div标签,然后查找所有的<a>标签
## 'find'是查找给定的标签一次,就算后面还有一样的标签也不会提取出来哦
## 而'find_all'是在页面中找出所有给定的标签!有10个给定的标签就返回10个
all_a = Soup.find('div', class_='all').find_all('a')
for a in all_a:
    # print(a)
    title = a.get_text() # 取出a标签的文本
    path = str(title).strip() ## 去掉空格
    os.makedirs(os.path.join("D:\mzitu", path)) ## 创建一个存放套图的文件夹
    os.chdir("D:\mzitu\\"+path) ## 切换到上面创建的文件夹

    href = a['href'] # 取出a标签的href属性
    # print(title, href)
    html = requests.get(href, headers=headers)
    html_Soup = BeautifulSoup(html.text, 'lxml')
    # 查找所有的<span>标签,获取第十个的<span>标签中的文本也就是最后一个页面了
    max_span = html_Soup.find('div',class_='pagenavi').find_all('span')[-2].get_text()
    print(max_span)
    for page in range(1, int(max_span)+1):
        page_url = href + '/' + str(page)
        # print(page_url)
        img_html = requests.get(page_url, headers=headers)
        img_soup = BeautifulSoup(img_html.text, 'lxml')
        # 查找标签
        img_url = img_soup.find('div',class_='main-image').find('img')['src']
        # print(img_url)
        ## 取URL 倒数第四至第九位 做图片的名字
        name = img_url[-9:-4]
        img = requests.get(img_url, headers=headers)
        # 路径
        f = open(name+".jpg",'ab')
        f.write(img.content)
        f.close()