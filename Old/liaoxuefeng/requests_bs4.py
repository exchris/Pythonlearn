#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/26 0026 下午 5:23
# @Author  : Exchris Tsai
# @Site    : 
# @File    : requests_bs4.py
# @Software: PyCharm

__author__ = 'Exchris Tsai'

from bs4 import BeautifulSoup as BS
import  requests
import codecs

def get_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }
    date = requests.get(url).content
    return date

def get_text(html):
    soup = BS(html, 'html.parser')
    article = soup.find('div', attrs={'class':'article'}) # 定位文章
    title = article.find('h1', attrs={'class':'title'}).get_text() # 获取标题
    text = [] # 定义一个列表来存放文章
    for paragraph in article.find_all('p'):
        p_content = paragraph.get_text()
        text.append(p_content) # 将文章一段一段的添加入列表
        # print(p_content)
    return title, text

def save_text(title, text):
    file_name = title + '.txt' # 定义文件名
    with codecs.open(file_name, 'wb', encoding='utf-8') as fp:
        # codecs是文件操作模块
        try:
            for p in text:
                fp.write('\t%s\t\r\n'%p)
        except Exception:
            print('error!')
        print('文章读取完成!')
        return


if __name__ == '__main__':
    url = 'http://www.jianshu.com/p/4a349b5c16c7'
    html = get_page(url)
    title, text = get_text(html)
    save_text(title, text)