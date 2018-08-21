# -*- coding:UTF-8 -*-

import json 

# json.dumps() 将Python对象编码成JSON字符串
# json.loads() 将已编码的JSON字符串解码为Python对象

data = [{'a':1,'b':2,'c':3,'d':4,'e':5}]

# 将Python对象编码成JSON字符串
json = json.dumps(data)
print(json)

