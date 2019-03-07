#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql

# 打开数据库链接
db = pymysql.connect("127.0.0.1", "root", "root", "test")

# 使用cursor()方法操作游标
cursor = db.cursor()

html = urlopen("https://www.zhihu.com/explore")
bsObj = BeautifulSoup(html, 'lxml')
bsList = bsObj.findAll("", {"class": "explore-feed feed-item"})
for bsItem in bsList:
    qsLink = bsItem.find("a", {"class": "question_link"})
    author = bsItem.find("span", {"class": "author-link-line"})
    vote = bsItem.find("div", {"class": "zm-item-vote"})

    print(" 标题: %s\n 地址：%s\n 回答者：%s \n 点赞数：%s \n" % (
        qsLink.get_text().strip(), qsLink.attrs["href"], author.get_text().strip(), vote.get_text().strip()))

    # SQL插入语句
    title = qsLink.get_text().strip()
    href = qsLink.attrs["href"]
    answer = author.get_text().strip()
    vote = int(vote.get_text().strip())

    sql = "INSERT INTO zhihu_content(title, \
        href, answer, vote ) \
        VALUES('%s', '%s', '%s', '%d')" % \
          (title, href, answer, vote)

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

# 关闭数据库链接
db.close()
