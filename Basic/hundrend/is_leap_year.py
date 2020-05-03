#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
@author dev.erxuan@gmail.com
@file is_leap_year.py
@software PyCharm
@date 2020/4/23 20:41
"""


def is_leap_year(year):
    """
    四年一闰，百年不闰，四百年再闰
    :param year:
    :return:
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("{}年是闰年".format(year))
    else:
        print("{}年是平年".format(year))


if __name__ == "__main__":
    year = int(input("year=?"))
    is_leap_year(year)
    pass
