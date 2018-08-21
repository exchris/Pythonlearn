# -*- coding:UTF-8 -*-

import json

# Python字典类型转换为JSON对象

data = {
    'no':1,
    'name':'Runoob',
    'url':'http://www.runoob.com'
}

# 对数据进行编码
json_str = json.dumps(data)

print("Python 原始数据:", repr(data))
print("JSON 对象:", json_str)
