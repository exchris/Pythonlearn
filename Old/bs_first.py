# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

# 创建一个html文本
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
# 创建对象:soup = BeautifulSoup(html,'lxml')
soup = BeautifulSoup(html, 'lxml')
# Tag就是html中的一个标签,用BeautifulSoup就能解析出来Tag的具体内容
# 具体的个数为soup.name其中name是html下的标签
print(soup.title) # 输出title标签下的内容,
print(soup.head)