# python3.4 爬虫教程
# 爬取网站上的图片
# 林炳文Evankaka(博客：http://blog.csdn.net/evankaka/)
# -*- coding:utf-8 -*-
import urllib.request
import socket
import re
import sys
import os

targetDir = r"D:\images\girls"  # 文件保存路径


def destFile(path):
    if not os.path.isdir(targetDir):
        os.mkdir(targetDir)
    pos = path.rindex('/')
    t = os.path.join(targetDir, path[pos + 1:])
    return t


if __name__ == "__main__":  # 程序运行入口
    weburl = "http://images.baidu.com/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs1&word=%E6%80%A7%E6%84%9F90%20%E7%BE%8E%E5%A5%B3&oriquery=%E7%BE%8E%E5%A5%B3&ofr=%E7%BE%8E%E5%A5%B3"
    webheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    req = urllib.request.Request(url=weburl, headers=webheaders)  # 构造请求报头
    webpage = urllib.request.urlopen(req)  # 发送请求报头
    contentBytes = webpage.read()
    for link, t in set(re.findall(r'(http:[^\s]*?(jpg|png|gif))', str(contentBytes))):  # 正则表达式查找所有的图片
        print(link)
        try:
            urllib.request.urlretrieve(link, destFile(link))  # 下载图片
        except:
            print('失败')  # 异常抛出