# -*- coding:utf-8 -*-
import requests

# 发送请求
r = requests.get('https://github.com/exchris')
# 返回码
print(r.status_code)  # 200

# 返回头部信息
print('>>>> Content-Type')
contentType = r.headers['content-type']
print(contentType) # 'text/html; charset=utf-8'


# 编码信息
print('>>>>encoding')
encoding = r.encoding 
print(encoding) # 'utf-8'

# 内容部分(PS:由于编码问题,建议这里使用r.content)
contents = r.text
print(contents)