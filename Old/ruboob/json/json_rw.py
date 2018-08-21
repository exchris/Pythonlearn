# -*- coding:utf-8 -*-
import json
# 写入JSON数据
data = {"app":"fitshow","author":"exchirs"}
with open('data.json', 'w') as f:
    json.dump(data, f)

# 读取数据
with open('data.json', 'r') as f:
    data = json.load(f)