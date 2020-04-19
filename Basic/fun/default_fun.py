#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
@description: 接收由用户输入的通过逗号分隔的两个非零整数
计算两个数字的和、差、积、商
并将结果返回给用户

@author dev.erxuan@gmail.com
@file default_fun.py
@software PyCharm
@date 2020/4/19 9:49
"""


def get_input(split_char = ','):
    """
    接收用户输入的两个非零整数
    :return:
    """
    input_string = input("请输入由逗号分隔的两个非零整数".format(split_char))
    # 将字符串10,5变为列表['10','5'],并分别赋值给a_string,b_string，使得a_string的值为"10",b_string的值为"5"
    a_string, b_string = input_string.split(split_char)
    return int(a_string), int(b_string)


def calc(a, b):
    """
    只负责计算，计算a,b的和、差、积、商，并将结果保存为一个字典返回
    :param a:
    :param b:
    :return:
    """
    sum_a_b = a + b
    difference_a_b = a - b
    product_a_b = a * b
    quotiend = a / b

    return {
        'sum': sum_a_b,
        'diff': difference_a_b,
        'pro': product_a_b,
        'quo': quotiend
    }


def output(result):
    """
    输出，将result这个字典的值打印到屏幕上
    :param result:
    :return:
    """
    print("两个数的和为: {}".format(result['sum']))
    print("两个数的差为: {}".format(result['diff']))
    print("两个数的积为: {}".format(result['pro']))
    print("两个数的商为: {}".format(result['quo']))


if __name__ == "__main__":
    a_int, b_int = get_input()
    result_dict = calc(a_int, b_int)
    output(result_dict)
    pass
