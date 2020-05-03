#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
@description csv操作示例
@author dev.erxuan@gmail.com
@file CsvOperator.py
@software PyCharm
@date 2020/4/19 15:29
"""
import csv


def csv_operator_read(file):
    """
    csv操作读取csv文件
    :param file:
    :return:
    """
    with open(file, encoding='utf-8') as f:
        # reader = csv.DictReader(f)
        reader = [x for x in csv.DictReader(f)]
        for row in reader:
            username = row['username']
            content = row['content']
            reply_time = row['reply_time']
            print('用户名:{},回复内容:{}'.format(username, content))


def csv_operator_write(data, file):
    """
    csv操作将字典内容写入到csv文件
    :param data
    :param file:
    :return:
    """
    with open(file, 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'age', 'salary'])
        writer.writeheader()
        writer.writerows(data)
        writer.writerow({'name': 'superman', 'age': 999, 'salary': 0})


if __name__ == "__main__":
    file = 'result.csv'
    csv_operator_read(file)
    data = [
        {'name': 'kingname', 'age': 24, 'salary': 99999},
        {'name': 'meiji', 'age': 34, 'salary': 1000000},
        {'name': 'zhangsan', 'age': 2, 'salary': 6000}
    ]
    csv_operator_write(data, 'new.csv')
    pass
