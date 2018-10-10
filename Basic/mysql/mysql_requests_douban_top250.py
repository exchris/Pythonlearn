#!/usr/bin/python
# -*- coding:utf-8 -*-

# 爬虫存取豆瓣电影TOP250的部分数据
import pymysql
import requests
import re
from bs4 import BeautifulSoup

db = pymysql.connect("127.0.0.1","root","root","test")
cursor = db.cursor()

def getHTMLText(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Host': 'movie.douban.com'
    }
    try:
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    # 获取电影标题
    reTitle = r'<span class="title">(.[^&]*?)</span>'
    # 电影标题列表
    titleList = re.findall(reTitle, html)

    for i in titleList:
        print("第 %d " % titleList.index(i), ",名为 %s" % i)
        sql = "insert into film(name,rank) values('%s', '%d')" % \
              (i, titleList.index(i))
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

    # 获取电影评分
    # reStar = r'"v:average">(.*?)</span>'
    # starList = re.findall(reStar, html)
    # 获取电影排名
    # reRank = r'<em class="">(.*)</em>'
    # rankList = re.findall(reRank, html)

if __name__ == "__main__":
    page = 0
    base_url = 'https://movie.douban.com/top250?start='
    while page < 10:
        url = base_url + str(25 * page)
        html = getHTMLText(url)
        result = get_data(html)
        page += 1
    print("All Done!")


