# -*- coding:UTF-8 -*-
import re

# 在起始位置匹配
print(re.match('www', 'www.runoob.com').span())

# 不在起始位置匹配
print(re.match('com', 'www.runoob.com'))

line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*',line,re.M|re.I)

if matchObj:
    print("matchObj.group():", matchObj.group())
    print("matchObj.group(1):",matchObj.group(1))
    print("matchObj.group(2):",matchObj.group(2))
else:
    print("No match!!")
    
    
# 在起始位置匹配
print(re.search('www', 'www.runoob.com').span())
# 不在起始位置匹配
print(re.search('com', 'www.runoob.com').span())

searchObj = re.search(r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
    print("searchObj.group():",searchObj.group())
    print("searchObj.group(1):",searchObj.group(1))
    print("searchObj.group(2):",searchObj.group(2))
else:
    print("Nothing found!")