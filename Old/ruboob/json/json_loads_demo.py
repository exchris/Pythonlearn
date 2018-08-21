# -*- coding:utf-8 -*-



# Python 字典类型转换为JSON对象

data1 = {
    'no': 1,
    'name':'Runoob',
    'url':'http://www.runoob.com'
}

# 对数据进行编码

import json

json_str = json.dumps(data1)
print("Python原始数据:", repr(data1))
print("JSON对象:", json_str)

# 将JSON对象转换为Python字典

# 对数据进行解码
data2 = json.loads(json_str)

print("data2['name']:", data2['name'])
print("data2['url']:", data2['url'])