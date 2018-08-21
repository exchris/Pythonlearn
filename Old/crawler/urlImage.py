"""
Created on 八月 03 2017
@author: dev.erxuan@gmail.com
"""
# -*- coding: utf-8 -*-
import os
import sys
import re
import urllib
import urllib.request

URL_REG = re.compile(r'(http://[^/\\]+)', re.I)
IMG_REG = re.compile(r'<img[^>]*?src=([\'"])([^\1]*?)\1', re.I)

def download(dir, url):
    ''' 下载网页中的图片

    :param dir: 保存到本地的路径
    :param url: 网页url
    :return: www.iplaypy.com
    '''
    global URL_REG, IMG_REG

    m = URL_REG.match(url)
    if not m:
        print('[Error]Invalid URL:', url)
        return
    host = m.group(1)

    if not os.path.isdir(dir):
        os.mkdir(dir)

    # 获取html,提取图片url
    html = urllib.request.urlopen(url).read()
    imgs = [item[1].lower() for item in IMG_REG.findall(html)]



