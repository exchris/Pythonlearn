#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
@author dev.erxuan@gmail.com
@file FileOperator.py
@software PyCharm
@date 2020/4/19 15:17
"""


def read_file(file):
    with open(file, encoding='utf-8') as f:
        """
        readlines()读取文本所有行并以列表形式返回结果
        """
        # content_list = f.readlines()
        # print(content_list)
        # print("\n\n")
        """
        直接把文件里面的全部内容用一个字符串返回
        """
        content_read_list = f.read()
        print(content_read_list)


def write_file(newFile):
    with open(newFile, 'w', encoding='utf-8') as f:
        f.write('您好')
        f.write('\n=============\n')
        f.writelines(['嘿嘿', '跟我学爬虫'])
        f.write('\n=============\n')
        f.writelines(['爬虫开发\n', '看这本书就够了!\n'])


if __name__ == "__main__":
    file = 'test.txt'
    newfile = 'new.txt'
    write_file(newfile)
    pass
