#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
@author dev.erxuan@gmail.com
@file Tieba.py
@software PyCharm
@date 2020/4/19 16:50
"""
import re
import csv

with open('source.txt', 'r', encoding='utf-8') as f:
    source = f.read()

result_list = []
username_list = re.findall('username="(.*?)"', source, re.S)
print(username_list)
content_list = re.findall('j_d_post_content " style="display:;">(.*?)<', source, re.S)
print(content_list)
reply_time_list = re.findall('class="tail-info">(2017.*?)<', source, re.S)
print(reply_time_list)

for i in range(len(username_list)):
    result = {
        'username': username_list[i],
        'content': content_list[i],
        'reply_time': reply_time_list[i]
    }
    result_list.append(result)

with open('tieba.csv', 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['username', 'content', 'reply_time'])
    writer.writeheader()
    writer.writerows(result_list)

# 逻辑上更合理的代码
# 首先获得包含每一层楼所有信息的大文本块
every_reply = re.findall('l_post l_post_bright j_l_post clearfix "(.*?)p_props_tail props_appraise_wrap', source, re.S)
print(every_reply)

if __name__ == "__main__":
    pass
