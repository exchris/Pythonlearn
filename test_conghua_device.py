#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: liu li
@software: PyCharm
@file: test_conghua_device.py
@time: 2020-5-21 9:22
"""
import requests
import json
import random
from datetime import datetime, timedelta
import time

header = {'token': 'c6367e6ee1202a5f27c2b6f658a7b928', 'Content-Type': 'application/json;charset=UTF-8'}
host_address = "http://16.176.84.78:3016"
# host_address = 'http://30.23.78.173'
# host_md_address = "http://30.23.78.173:9876"
host_md_address = "http://16.176.84.81:9876"


def test_get_brand():
    '''
    查询每个品牌
    :return:
    '''
    url_address = host_address + '/oper/brandManage/list'
    data_value = json.dumps({
        "current": 1,
        "name": "sAAA",
        "size": 10,
    })
    result_data = requests.post(url=url_address, headers=header, data=data_value)
    result_value = json.loads(result_data.text)
    global brand_id
    brand_id = result_value['data']['records'][0]['id']
    result_model = result_value['data']['records'][0]['attrs']
    model = result_model.split(";")
    model_result_value = model[1].split("  ")
    del (model_result_value[0])
    # print("品牌型号"+ model_result_value)
    return (brand_id, model_result_value)


def test_get_classify_device():
    '''
    获取所有分类
    :return:
    '''
    url_address = host_address + '/oper/objectType/objectTypeList'
    data_value = json.dumps({
        "current": 1,
        "name": "",
        "parentType": 1,
        "size": 1000
    })
    result_data = requests.post(url=url_address, headers=header, data=data_value)
    result_value = json.loads(result_data.text)
    print(result_value)
    list_objectType = []
    for single_index in result_value['data']['records']:
        if single_index["objectType"] != "12":
            list_objectType.append(single_index['objectType'])
    print(list_objectType)
    return list_objectType


def test_add_devices():
    '''
    添加设备
    :return:
    '''
    approved_date = (datetime.now() - timedelta(days=random.randint(0, 60))).strftime('%Y-%m-%d %H:%M:%S')
    expired_date = (datetime.now() + timedelta(days=random.randint(0, 60))).strftime('%Y-%m-%d %H:%M:%S')
    last_maint_date = (datetime.now() - timedelta(days=random.randint(15, 30))).strftime('%Y-%m-%d %H:%M:%S')
    longitude = float("113.5" + str(random.randint(10000, 100000)))
    latitude = float("23.5" + str(random.randint(10000, 100000)))
    objectType = random.choices(test_get_classify_device())[0]
    print(objectType)
    # print((datetime.now()-timedelta(days=random.randint(060))).strftime('%Y-%m-%d %H:%M:%S'))
    url_address = host_address + '/oper/deviceManage/addDevice'
    data_value = json.dumps({
        "objectType": objectType,
        "strategyId": "",  # 策略
        "name": "测试设备" + str(random.randint(1, 1000)),
        # "code":str(random.randint(100000000010000000000000)) # 设备编号
        "approvedDate": approved_date,  # 验收时间
        "squadron": random.choice([3, 4, 10, 11, 12, 13, 14]),  # 所属中队
        "ip": "16.176.86." + str(random.randint(0, 254)),  # IP地址
        "status": random.choice([0, 1, 2, 3]),  # 设备状态
        "delFlag": 0,
        "location": "",  # 安装地址
        "longitude": longitude,  # 经度
        "latitude": latitude,  # 纬度
        "brand": test_get_brand()[0],  # 品牌
        "model": random.choices(test_get_brand()[1])[0],  # 型号
        "desc<x>ription": "测试构造的数据设备" + str(random.randint(1, 1000)),  # 设备描述
        "tag": random.choice([0, 1]),  # 设备标签 内场，外场
        "relateKey": "",
        "serialNo": "440117000513110" + str(random.randint(10000, 99999)),
        # "uuid": "uuid"+ str(random.randint(100000000010000000000000)) #
        # "maintenanceUnit": random.choices(test_get_public_info[1])[0] # 维保单位
        "maintenanceUnit": random.choice([2, 7]),
        "maintenanceCycle": random.randint(15, 60),  # 维保间隔
        "last_maintDate": last_maint_date,  # 上次维保时间
        "expiredDate": expired_date,  # 有效时间
        "manufacturer": random.choice([5, 6, 8, 9])  # 厂商
    })
    result_data = requests.post(url=url_address, headers=header, data=data_value)
    result_value = json.loads(result_data.text)
    print(result_value)


if __name__ == '__main__':
    print('starting')
    for _ in range(100):
        test_add_devices()
        time.sleep(1)
