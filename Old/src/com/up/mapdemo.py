# -*- coding:UTF-8 -*-
#map()是python内置的高阶函数,它接收一个函数f和一个list,并通过把函数f依次作用在list的每个元素上,
# 得到一个新的list并返回
# map()函数不改变原有的list，而是返回一个新的list
def f(x):
	return x*x

print(list(map(f,[1,2,3,4,5,6,7,8,9])))
# [1,4,9,....,81]

'''
任务:
假设用户输入的英文名字不规范,没有按照首字母大写,后续字母小写的规则,请利用map()函数,
把一个list(包含若干不规范的英文名字)变成一个包含规范英文名字的list
例如:
输入:['adam','LISA','barT']
输出:['Adam','Lisa','Bart']
'''
def format_name(s):
	return s[0].upper()+s[1:].lower()

print(list(map(format_name,['adam','LISA','barT'])))