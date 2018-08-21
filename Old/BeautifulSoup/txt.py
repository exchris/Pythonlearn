# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import re

# 根据HTML网页字符串创建BeautifulSoup对象
soup = BeautifulSoup(
                    html_doc,                # HTML文档字符串
                    'html.parser',           # HTML解析器
                    from_encoding:'utf8'     # HTML文档的编码   
                    )

# 方法: find_all(name, attrs, string)

# 查找所有标签为a的节点
soup.find_all('a')

# 查找所有标签为a,链接符合/view/123.html形式的节点
soup.find_all('a', href='/view/123.html') 
soup.find_all('a', href=re.compile(r'/view/\d+\.html'))

# 查找所有标签为div,class为abc,文字为Python的节点
soup.find_all('div', class_='abc', string='Python')

# 得到节点: <a href='1.html'>Python</a>

# 获取查找到的节点的标签名称
node.name

# 获取查找到的a节点的href属性
node['href']

# 获取查找到的a节点的链接文字
node.get_text()
