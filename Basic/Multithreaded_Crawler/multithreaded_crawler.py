#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
多线程爬虫
@author dev.erxuan@gmail.com
@file multithreaded_crawler.py
@software PyCharm
@date 2020/5/3 12:58
"""
from multiprocessing.dummy import Pool


def calc_power2(num):
    return num * num


def calDigitSquare():
    """
    计算0~9的每个数的平方
    :return:
    """
    # 初始化一个有3个线程的线程池
    pool = Pool(3)
    orgin_num = [x for x in range(10)]
    result = pool.map(calc_power2, orgin_num)
    print(f'计算0-9的平放分别为:{result}')


if __name__ == "__main__":
    calDigitSquare()
    pass
