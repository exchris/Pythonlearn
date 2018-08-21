# -*- coding:UTF-8 -*-
# 场景1:找到imooc开头的
def find_start_imooc(fname):  
    f = open(fname)
    for line in f:
        if line.startswith('imooc'):
            print(line)
            
find_start_imooc('imooc.txt')

# 找到imooc开头和结尾的语句
def find_in_imooc(fname):
    f = open(fname)
    for line in f:
        if line.startswith('imooc')\
           and line[:-1].endswith('imooc'):
            print(line)
               
find_in_imooc('imooc.txt')

# 匹配一个下划线和字母开头的变量名 

    
