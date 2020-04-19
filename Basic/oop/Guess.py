#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
@author dev.erxuan@gmail.com
@file Guess.py
@software PyCharm
@date 2020/4/19 10:33
"""
import random

"""
使用Python开发一个猜数小游戏。
1、再游戏中，程序每一轮会随机生成0~1024之间的数字，用户输入猜测的数字，程序告诉用户猜大了还是猜小了
再一定次数内猜对，则本轮用户获胜，否则本轮用户失败;
2、每一轮开始时，程序会要求用户输入用户名
3、程序会一直运行，直到用户输入"3"，停止游戏。每一轮游戏开始前，输入"1"可以查看用户的输入历史

知识点
(1)随机生成数字，涉及python的随机数模块
(2)用户输入数字，程序输出结果，涉及python的输入和输出模块
(3)程序会自动开始下一轮，涉及python的循环模块
(4)判断用户的输入，涉及python的条件判断
(5)查询用户的输入历史，涉及python的字典和列表
"""

history = dict()


def show_history():
    print('用户:{},记录如下:{}'.format(name, history[name]))


def start():
    global name
    name = input("请输入你的名字")
    history[name] = []
    answer = random.randint(0, 10)
    try_to_guess(name, answer)


def try_to_guess(name, answer):
    try_num = 0
    while try_num < 10:
        guess_answer = int(input('请输入一个数字: '))
        if guess_answer < answer:
            print('你输入的数字比正确答案小。')
        elif guess_answer == answer:
            print('回答正确')
            history[name].append('成功')
            break
        else:
            print('你输入的数字比正确答案大。')
            try_num += 1
    else:
        print('猜错次数太多，失败。')
        history[name].append('失败')


def default():
    pass


if __name__ == "__main__":
    select_dict = {'1': show_history, '2': start, '3': exit}
    while True:
        select = input('1.历史记录\n2.继续游戏\n3.退出游戏\n输入数字选择:')
        select_dict.get(select, default)()
