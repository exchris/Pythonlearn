#!/usr/bin/python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup

html_doc = """
<html>
<body>
    <b class="boldest">Extremely bold</b>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, "lxml")

# 对象的种类归纳为:Tag,NavigableString,BeautifulSoup,Comment
tag = soup.b
print(type(tag))
print(tag)
# 每个tag都有自己的名字，通过.name来获取
print(tag.name)
tag.name = "blockquote"
print(tag)

# Attributes
print(type(tag['class']))  # <class:list>
print(tag['class'])  # ['boldest]
print(tag.attrs)  # {'class':['boldest']}

# tag的属性可以被添加，删除或修改
tag['class'] = 'verybold'
tag['id'] = 'verybold'

del tag['class']
del tag['id']
print(tag)
print(tag.get('class'))

css_soup = BeautifulSoup('<p class="body strikeout"></p>', "lxml")
print(css_soup.p['class'])  # ['body', 'strikeout']
css_soup1 = BeautifulSoup('<p class="body"></p>', 'lxml')
print(css_soup1.p['class'])  # ['body']

# 如果某个属性看起来好像有多个值,但在任何版本的HTML定义中都没有被定义为多值属性,那么Beautiful Soup会将这个属性作为字符串返回
id_soup = BeautifulSoup('<p id="my id"></p>', 'lxml')
print(id_soup.p['id'])  # my id

# 将tag转换成字符串时，多值属性将会合并成一个值
rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>', 'lxml')
print(rel_soup.a['rel'])
rel_soup.a['rel'] = ['index', 'contents']
print(rel_soup.p)

# 如果转换的文档是XML格式，那么tag中不包含多值属性
xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')
print(xml_soup.p['class'])