#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
@author dev.erxuan@gmail.com
@file operation-platform-test.py
@software PyCharm
@date 2020/4/18 15:13
"""
import requests
import random
from datetime import datetime, timedelta
import json

host_address = "http://127.0.0.1:3016/oper/"
headers = {"token": "", "Content-Type": "application/json"}


def test_add_brand():
    url_address = host_address + "brandManage/addBrand"
    data_param = {
        
        ""
    }
    data_value = json.dumps(data_param)
    date_result = requests.post(url=url_address, headers=headers, data=data_value)

if __name__ == "__main__":
    pass
