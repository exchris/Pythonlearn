#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
作用：
    下载王者荣耀官网图片壁纸
时间：
    2018-08-10
'''

# 导入模块
import requests
import json
import urllib

# 读取英雄信息 关键是数字名称
with open('.\\herolist.json', 'r', encoding='utf-8') as ff:
    jsonFile = json.load(ff)

# 批量提取数据

# 动态计算所有英雄个数
for m in range(len(jsonFile)):
    # 数字名称
    eName = jsonFile[m]['ename']
    # 中文名称
    cName = jsonFile[m]['cname']
    # 所有皮肤名称 列表
    skinName = jsonFile[m]['skin_name'].split('|')
    # 计算皮肤个数
    skinNumbers = len(skinName)
    # 下载皮肤
    for n in range(1, skinNumbers + 1):
        # 构造图片网址信息
        pictureUrl = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'\
                     + str(eName) + '/' + str(eName) + '-bigskin-' \
                     + str(n) + '.jpg'
        # 下载图片 requests.get(pictureUrl)
        # content 代表是以二进制格式表示
        picture = requests.request('get', pictureUrl).content
        # 保存图片 图片都是二进制 第一种方式
        with open('.\\pictures\\' + cName + skinName[n - 1] + '.jpg', 'wb') as ff:
            ff.write(picture)

        # 保存图片 图片都是以二进制 第二种方式
        # urllib.request.urlretrieve(pictureUrl, '.\\pictures\\' + cName + skinName[n - 1] + '.jpg')
