#!/usr/bin/python
# -*- coding:utf-8 -*-

# Requests爬虫实践:TOP250电影数据
# 网页地址: https://movie.douban.com/top250

import requests
from bs4 import BeautifulSoup


def get_movies():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Host': 'movie.douban.com'
    }
    movie_list = []
    for i in range(0, 10):
        link = 'https://movie.douban.com/top250?start=' + str(i * 25)
        r = requests.get(link, headers=headers)
        print(str(i + 1), "页响应状态码:", r.status_code)
        soup = BeautifulSoup(r.text, "lxml")
        div_list = soup.find_all('div', class_='hd')
        for each in div_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)
    return movie_list


movies = get_movies()
print(movies)
# 存储数据
for i in movies:
    with open("movies.txt", "a+") as f:
        f.write(str(movies.index(i)) + " " + i + "\n")
        f.close()
