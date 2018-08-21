# !/usr/bin/python
# -*- coding:utf-8 -*-
import json

data = [{'a':1, 'b':2, 'c':3, 'd':4, 'e':5}]

json = json.dumps(data)

print(json)

# 使用参数让JSON数据格式化输出
import json
formatJSON = json.dumps({'a':'Runoob','b':7}, sort_keys=True, indent=4, separators=(',', ':'))
print(formatJSON)

# json.loads用于编码JSON数据。该函数返回Python字段的数据类型
import json
jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

text = json.loads(jsonData)
print(text)
