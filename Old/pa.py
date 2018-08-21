"""
Created on 八月 03 2017
@author: dev.erxuan@gmail.com
"""
# -*- coding: utf-8 -*-
import urllib.request
import re
import os
import random
import time
import sys

def getHtml(url):
    data = urllib.request.urlopen(url).read()
    data = data.decode('UTF-8')
    return data

def getData(content):
    # 需要获取资源的正则
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, content)
    return imglist

def saveImg(imageURL, fileName):
    try:
        u = urllib.request.urlopen(imageURL)
        data = u.read()
        f = open(fileName, 'wb')
        f.write(data)
        print(u"Save hers img", fileName)
        f.close()
    except urllib.request.HTTPError as e:
        print('1:', e)
        time.sleep(random.choice(range(5, 10)))
    except urllib.request.URLError as e:
        print('2:', e)
        time.sleep(random.choice(range(5, 10)))

def saveImgs(images):
    number = 1
    for imageURL in images:
        # 打印图片链接
        print(imageURL+"\n")
        splitPath = imageURL.split('.')
        fTail = splitPath.pop()
        if len(fTail) > 3:
            fTail = "jpg"
        fileName = "img"+"/"+str(number) + "." + fTail
        saveImg(imageURL, fileName)
        number += 1

def mkdir(path):
    path = path.strip()
    # 判断路径是否存在 True存在 False不存在
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在创建目录
        print(u"create",path,u'dir')
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录不存在则不创建,并提示目录已存在
        print(u"named",path,'already exists')
        return False

url = "http://pic.91.com/play/1411/21760879.html#p=10"
data = getHtml(url)
imglist = getData(data)

# 创建目录
mkpath = mkdir('img')
# 保存图片到指定目录
saveImgs(imglist)


