#!/usr/bin/python
# coding:utf-8
# 获取响应内容
import requests
r = requests.get('http://www.santostang.com/')

"""
1 r.text是服务器响应的内容，会自动根据响应头部的字符编码进行解码
2 r.encoding是服务器内容使用的文本编码
3 r.status_code用于检测响应的状态码，如果返回200，就表示请求成功了，如果返回的是4xx，就表示客户端错误，5xx则表示服务器错误响应
4 r.content是字节形式的响应体，会自动解码gzip和deflate编码的响应数据
5 r.json()是Requests中内置的JSON解析器
"""

print("文本编码:",r.encoding)
print("响应状态码:", r.status_code)
print("字符串方式的响应体:", r.text)