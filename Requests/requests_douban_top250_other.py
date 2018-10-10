#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

def getHTMLText(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Host': 'movie.douban.com'
    }
    try:
        r = requests.get(url,headers=headers,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    # 获取电影标题
    reTitle = r'<span class="title">(.[^&]*?)</span>'
    titleList = re.findall(reTitle, html)
    # 获取电影评分
    reStar = r'"v:average">(.*?)</span>'
    starList = re.findall(reStar, html)
    # 获取电影排名
    reRank = r'<em class="">(.*)</em>'
    rankList = re.findall(reRank, html)

    count = 0
    # 定义写入模板
    tplt = "{0:^10}\t{1:{3}<10}\t{2:^18}\n"
    with open('filmlist.txt', 'a') as f:
        # 输出每一页的结果
        while count < 25:
            f.write(tplt.format(rankList[count],titleList[count],starList[count],chr(12288)))
            count += 1


if __name__=="__main__":
    f = open('filmlist.txt', 'w')
    f.write('') # 清空源文件内容
    f.close()
    # 定义写入模板
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^18}\n"
    with open('filmlist.txt', 'a') as f:
        f.write(tplt.format("排名","电影","评分", chr(12288)))

    page = 0
    base_url = 'https://movie.douban.com/top250?start='
    while page < 10:
        url = base_url + str(25 * page)
        html = getHTMLText(url)
        result = get_data(html)
        page += 1
    print("All Done!!!")