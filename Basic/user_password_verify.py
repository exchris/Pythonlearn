#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
@author dev.erxuan@gmail.com
@file user_password_verify.py
@software PyCharm
@date 2020/4/24 21:57
"""
import getpass

username = input('请输入用户名:')
password = input('请输入口令:')
# 如果希望输入口令时 终端中没有回显 可以使用getpass模块的getpass函数
password1 = getpass.getpass('请输入口令:')
if username == 'admin' and password == '123456':
    print('身份验证成功!')
else:
    print('身份验证失败!')
if __name__ == "__main__":
    pass
