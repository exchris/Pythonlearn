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
import os
import psycopg2
import pytest

host_address = "http://127.0.0.1:3016/oper/"
headers = {"token": "", "Content-Type": "application/json;charset=UTF-8"}
host_md_address = "http://127.0.0.1:9876"

file_name = os.path.abspath(os.path.join(os.getcwd())) + '/device_id.txt'


# 获取信息
@pytest.fixture(scope='module')
def test_get_public_info():
    url_address = "http://30.23.78.173:3017/oper/test/getOrgTree"
    print(url_address)
    result_data = requests.get(url=url_address, headers=headers)
    result_value = json.loads(result_data.text, encoding='utf-8')
    print(result_value)
    data_result = result_value['data']['level1Node']
    manufacturers_info = data_result[10]
    weibao_info = data_result[9]
    print(weibao_info)
    manufacturers_info_id_list = []
    weibao_info_id_list = []
    manufacturers_info_id_list.append(manufacturers_info['data']['id'])
    weibao_info_id_list.append(weibao_info['data']['id'])
    for child_id in manufacturers_info['children']:
        manufacturers_info_id_list.append(child_id['data']['id'])
    for weibao_child_id in weibao_info['children']:
        weibao_info_id_list.append(weibao_child_id['data']['id'])
    print(manufacturers_info_id_list)
    print(weibao_info_id_list)
    return manufacturers_info_id_list, weibao_info_id_list


def test_get_classify_device():
    """
    获取分类
    :return:
    """
    url_address = host_address + "/objectType/objectTypeList"
    data_value = json.dumps({
        "current": 1,
        "name": "",
        "parentType": 1,
        "size": 1000
    })
    result_data = requests.post(url=url_address, headers=headers, data=data_value)
    result_value = json.loads(result_data.text, encoding='utf-8')
    print(result_value)
    list_object_type = []
    for single_index in result_value['data']['records']:
        list_object_type.append(single_index['objectType'])
    return list_object_type


def test_add_brand():
    """
    新增品牌
    :return:
    """
    list_model_name = []
    for model_index in range(0, 15):
        model_name = "测试型号" + str(model_index)
        list_model_name.append(model_name)

    url_address = host_address + "brandManage/add"
    # json.dumps将python对象转换为json字符串
    data_value = json.dumps({
        "colorAttrs": "红色,白色",
        "modelAttrs": ",".join(list_model_name),
        "name": "演示添加品牌",
        "sizeAttrs": "33"
    })
    # json.loads()将字符串转为字典,不仅可以把字符串转为字典，还可以转为任何Python对象
    print(json.loads(data_value))
    result_data = requests.post(url=url_address, headers=headers, data=data_value)
    result_value = json.loads(result_data.text)
    print(result_value)


def test_get_brand():
    """
    查询每个品牌
    :return:
    """
    url_address = host_address + 'brandManage/list'
    data_value = json.dumps({
        "current": 1,
        "name": "演示添加品牌",
        "size": 10
    })
    result_data = requests.post(url=url_address, headers=headers, data=data_value)
    result_value = json.loads(result_data.text)
    global brand_id
    brand_id = result_value['data']['records'][0]['id']
    result_model = result_value['data']['records'][0]['attrs']
    model = result_model.split(";")
    model_result_value = model[1].split(" ")
    del (model_result_value[0])
    return model_result_value


def test_add_devices():
    """
    添加设备
    :return:
    """
    approved_date = (datetime.now() - timedelta(days=random.randint(0, 60))).strftime('%Y-%m-%d %H:%M:%S')
    expired_date = (datetime.now() + timedelta(days=random.randint(0, 60))).strftime('%Y-%m-%d %H:%M:%S')
    last_maint_date = (datetime.now() - timedelta(days=random.randint(15, 30))).strftime('%Y-%m-%d %H:%M:%S')
    longitude = float("113.5" + str(random.randint(10000, 100000)))
    latitude = float("23.5" + str(random.randint(10000, 100000)))
    objecttype = random.choices(test_get_classify_device())[0]
    print(objecttype)
    print((datetime.now() - timedelta(days=random.randint(0, 60))).strftime('%Y-%m-%d %H:%M:%S'))
    url_address = host_address + "deviceManage/addDevice"
    data_value = json.dumps({
        "objectType": objecttype,
        "strategyId": "",  # 策略
        "name": "测试设备" + str(random.randint(1, 1000)),
        "code": str(random.randint(1000000000, 10000000000000)),  # 设备编号
        "approvedDate": approved_date,  # 验收时间
        # "squadron": random.choices(['46', '70', '113', '123', '125', '126', '128', '129', '2243', '2245'])[0]
        "squadron": random.choices([3, 4, 5]),  # 所属中队
        "ip": "30.23." + str(random.randint(0, 99)) + "." + str(random.randint(0, 254)),  # IP地址
        "status": random.choice([0, 1, 2, 3]),  # 设备状态
        "delFlag": 0,
        "location": "广东省广州市从化区职业技术学校",  # 安装位置
        "longitude": longitude,  # 经度
        "latitude": latitude,  # 纬度
        "brand": brand_id,  # 品牌
        "model": random.choices(test_get_brand())[0],  # 型号
        "description": "测试构造的数据设备" + str(random.randint(1, 1000)),  # 设备描述
        "tag": random.choice([0, 1]),  # 设备标签，内场，外场
        "relateKey": "",
        "serialNo": "serialno" + str(random.randint(1000000000, 10000000000000)),
        # "uuid": "uuid" + str(random.randint(1000000000, 10000000000000)),
        # "maintenanceUnit": random.choices(test_get_public_info[1])[0],  # 维保单位
        "maintenanceUnit": random.choice([10, 11, 19, 20, 21, 22, 23, 110, 112]),
        "maintenanceCycle": random.randint(15, 60),  # 维保间隔
        "last_maintDate": last_maint_date,  # 上次维保时间
        "expiredDate": expired_date,  # 有效时间
        "manufacturer": random.choice([13, 14, 24, 25, 26, 27, 28])  # 厂商
    })
    print(json.loads(data_value))
    print(data_value)
    result_data = requests.post(url=url_address, headers=headers, data=data_value)
    result_value = json.loads(result_data.text)
    print(result_value)


def pgyql_operation(sql):
    host = "10.25.76.84"
    port = 5432
    user = "postgres"
    pwd = ""
    dataBase = "conghua-oper-test"

    connect = psycopg2.connect(host=host, port=port, user=user, password=pwd, database=dataBase)
    cursor = connect.cursor()
    try:
        cursor.execute(sql)
        connect.commit()
        res = cursor.fetchall()
        connect.close()
        return res
    except Exception as e:
        print(e)
        connect.rollback()


def test_get_relate_key_1_lei():
    """
    :return:
    """
    sql = """
    select relate_key from ch_device where object_type in (
        select object_type from sys_object_type 
        where object_type_name like '电违不区%' or 
        object_type_name like '电子警察%' or 
        object_type_name like '%不礼让行人抓怕%' or
        object_type_name like '%测速设备%' or 
        object_type_name like '%违停抓怕%'
    )
    """
    relate_key = pgyql_operation(sql)
    list_relate_key = []
    for single_relate in relate_key:
        list_relate_key.append(single_relate[0])
    return list_relate_key


def test_send_tupiandaxiao():
    """
    构造图片大小不合适报警
    :return: 
    """
    group = "device"
    topic = "topicTest"
    url_address = host_address + "sys/sendMsgToMq?group=" + group + "&topic=" + topic
    print(url_address)
    data_value = json.dumps({
        "deviceId": random.choices(test_get_relate_key_1_lei())[0],
        "type": "avg",
        "data": random.randint(10, 20),  # 设置图片大小检查值时，设置550左右
    })
    print(json.loads(data_value))
    result_data = requests.post(url=url_address, headers=headers, data=data_value)
    result_value = json.loads(result_data.text)
    print(result_value)


def test_send_shuliangtongji():
    """
    一段时间内，检测的数量
    :return:
    """
    group = "device"
    topic = "topicTest"
    url_address = host_address + "sys/sendMsgToMq?group=" + group + "&topic=" + topic
    print(url_address)
    data_value = json.dumps({
        "deviceId": random.choices(test_get_relate_key_1_lei())[0],
        "type": "snap",
        "data": random.randint(10, 30),  # 设置检测量报警阈值，设置1000左右
    })
    print(json.loads(data_value))
    result_data = requests.post(url=url_address, headers=headers, data=data_value)
    print(datetime.now())
    result_value = json.loads(result_data.text)
    print(result_value)


def test_get_relate_key_2_xinhaokongzhi():
    """
    信号控制设备
    :return:
    """
    sql = """
    select relate_key from ch_device where object_type in (
        select object_type from sys_object_type where object_type_name like '信号控制%'
    )
    """
    relate_key = pgyql_operation(sql=sql)
    list_relate_key = []
    for single_relate_key in relate_key:
        list_relate_key.append(single_relate_key[0])
    print(list_relate_key)
    return list_relate_key


def test_send_xinhaokongzhi_1():
    """
    上传内容是否完整
    :return:
    """
    group, topic = "test", "signalDeviceStatus"
    url_address = host_address + "sys/sendMsgToMq?group=" + group + "&topic=" + topic
    print(url_address)
    data_value = json.dumps({
        "deviceId": random.choices(test_get_relate_key_2_xinhaokongzhi())[0],
        "status": 2
    })
    print(json.loads(data_value))
    result_data = requests.post(url=url_address, headers=headers, data=data_value)
    result_value = json.loads(result_data.text)
    print(result_value)


def test_get_relae_key_xinxifabu():
    """
    信息发布设备
    :return:
    """
    sql = """
        select relate_key from ch_device where object_type in (
            select object_type from sys_object_type where object_type_name like '信息发布%'
            or object_type_name like '信号控制%'
        )
        """
    relate_key = pgyql_operation(sql=sql)
    list_relate_key = []
    for single_relate_key in relate_key:
        list_relate_key.append(single_relate_key[0])
    print(list_relate_key)
    return list_relate_key


def test_get_relate_key_kakou():
    """
    获取第一类设备的relate_key
    :return:
    """
    sql = """
    select relate_key from ch_device where object_type in (
      select object_type from sys_object_type where object_type_name like '卡口设备%'
    )
    """
    relate_key = pgyql_operation(sql)
    list_relate_key = []
    for single_relate in relate_key:
        list_relate_key.append(single_relate[0])
    pgyql_operation(list_relate_key)
    return list_relate_key


def test_send_kakou_1():
    """
    卡口设备，检测视频信号
    :param test_get_relate_key_3_kakou:
    :return:
    """
    group, topic = "test", "topicTest"
    url_address = host_address + "sys/sendMsgToMq?group=" + group + "&topic=" + topic
    print(url_address)
    data_value = json.dumps({
        "deviceId": random.choices(test_get_relate_key_kakou())[0],
        "type": "qvd",
        "data": {
            "resolution": random.choice([1, 0, -1]),
            "inspectResult": random.randint(0, 6),
            "scChromaResult": random.choice([-1, 0, 1, 2]),
            "scSnowResult": random.choice([-1, 0, 1, 2]),
            "scDarkResult": random.choice([-1, 0, 1, 2]),
            "scLumaResult": random.choice([-1, 0, 1, 2]),
            "scFreezeResult": random.choice([-1, 0, 1, 2]),
            "scShakeResult": random.choice([-1, 0, 1, 2]),
            "scContrastResult": random.choice([-1, 0, 1, 2]),

            "scStreakResult": random.choice([-1, 0, 1, 2]),
            "scCoverResult": random.choice([-1, 0, 1, 2]),
            "scSignalResult": random.choice([-1, 0, 1, 2]),
            "scMonoResult": random.choice([-1, 0, 1, 2]),
            "scBlurResult": random.choice([-1, 0, 1, 2]),
            "scSceneResult": random.choice([-1, 0, 1, 2]),
            "scFlashResult": random.choice([-1, 0, 1, 2])
        }
    })
    print(json.loads(data_value))
    result_data = requests.post(url=url_address, headers=headers, data=data_value)
    result_value = json.loads(result_data.text)
    print(result_value)


def test_send_kakou_zhengchang():
    """
    卡口设备，检测视频信号
    :param test_get_relate_key_3_kakou:
    :return:
    """
    group = 'test'
    topic = 'topicTest'
    url_address = host_address + 'sys/sendMsgToMq?group=' + group + '&topic=' + topic
    print(url_address)
    data_value = json.dumps({
        "deviceId": random.choices(test_get_relate_key_kakou())[0],
        "type": "qvd",
        "data": {
            "resolution": random.choice([1, 0, -1]),
            "inspectResult": 1,
            "scChromaResult": 1,
            "scSnowResult": 1,
            "scDarkResult": 1,
            "scLumaResult": 1,
            "scFreezeResult": 1,
            "scShakeResult": 1,
            "scContrastResult": 1,

            "scStreakResult": 1,
            "scCoverResult": 1,
            "scSignalResult": 1,
            "scMonoResult": 1,
            "scBlurResult": 1,
            "scSceneResult": 1,
            "scFlashResult": 1
        }
    })
    print(json.loads(data_value))
    result_data = requests.post(url=url_address, headers=headers, data=data_value)
    result_value = json.loads(result_data.text)
    print(result_value)


if __name__ == "__main__":
    test_add_brand()
    test_get_brand()
    for i in range(0, 2):
        test_add_devices()
    test_send_tupiandaxiao()
    test_send_shuliangtongji()

    pass
