#!/usr/bin/python
# -*- coding:utf-8 -*-

# 超时

import requests

link = "http://www.santostang.com/"

# 把秒数设置为0.001秒，看看会抛出什么异常，这是为了让大家体验timeout异常的效果而设置的值，一般会把这个值设置为20秒
r = requests.get(link, timeout=0.001)
