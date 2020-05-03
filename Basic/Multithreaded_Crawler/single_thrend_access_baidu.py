#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
@author dev.erxuan@gmail.com
@file single_thrend_access_baidu.py
@software PyCharm
@date 2020/5/3 13:03
"""
import requests
import time
from multiprocessing.dummy import Pool


def query(url):
    requests.get(url)


def singleThrendBaidu():
    """
    单线程循环访问100次百度首页
    :return:
    """

    start = time.time()
    for i in range(100):
        query('https://baidu.com')
    end = time.time()
    print(f'单线程循环访问100次百度首页，耗时:{end - start}')


def fivePoolAccess_baidu():
    """
    使用5个线程访问100次百度首页，计算总时间
    :return:
    """
    start = time.time()
    url_list = []
    for i in range(100):
        url_list.append('https://baidu.com')
    pool = Pool(5)
    pool.map(query, url_list)
    end = time.time()
    print(f'5线程访问100次百度首页，耗时:{end - start}')


if __name__ == "__main__":
    singleThrendBaidu()
    fivePoolAccess_baidu()
    pass
