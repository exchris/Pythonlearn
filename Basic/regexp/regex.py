#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
@author dev.erxuan@gmail.com
@file regex.py
@software PyCharm
@date 2020/4/19 11:42
"""

import re

content = "我的微博密码:1234567,QQ密码是:33445566,银行卡密码是:888888,Github密码是:999abc999，帮我记住他们"

password_list = re.findall(':(.*?),', content)
name_list = re.findall('名字是(.*?),', content)
print('找到内容，返回:{}'.format(password_list))
print('找不到任何内容，返回:{}'.format(name_list))

account_content = "微博账号是:kingname,密码是:12345678,QQ账号是:99999,密码是:899abcd,银行卡账号是:00001,密码是:654321,Github账号是:999abc999,密码是:12345678"
account_password = re.findall('账号是:(.*?),密码是:(.*?),', account_content)
print('包含多个括号的情况下，返回:{}'.format(account_password))

big_string_mutil = """
我是kingname,我的微博密码是:123
45678,
"""
password_findall_no_flag = re.findall('密码是:(.*?),', big_string_mutil)
# 使用re.S作为flag来忽略换行符
password_findall_flag = re.findall('密码是:(.*?),', big_string_mutil, re.S)
print('不使用re.S的时候:{}'.format(password_findall_no_flag))
print('使用re.S的时候:{}'.format(password_findall_flag))

password_search = re.search('密码是:(.*?),', content)
password_search_not_find = re.search('xxx:(.*?),', content)
print(password_search)
print(password_search.group())
print(password_search.group(0))
print(password_search.group(1))
print(password_search_not_find)

account_password_search = re.search('账号是:(.*?),密码是:(.*?),', account_content)
print('读取第一个括号的内容:{}'.format(account_password_search.group(1)))
print('读取第二个括号的内容:{}'.format(account_password_search.group(2)))

if __name__ == "__main__":
    pass
