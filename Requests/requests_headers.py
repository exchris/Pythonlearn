#!/usr/bin/python
# -*- coding:utf-8 -*-

# 定制请求头
import requests
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
    'Host': 'www.santostang.com'
}
r = requests.get('http://www.santostang.com', headers=headers)
print("响应体的状态码:", r.status_code)
