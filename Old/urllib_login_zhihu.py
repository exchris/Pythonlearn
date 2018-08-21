"""
Created on 七月 31 2017
@author: dev.erxuan@gmail.com
"""
# -*- coding: utf-8 -*-
# @description: 登录知乎

# 抓取知乎首页
"""
简单的写一个GET程序,把知乎首页GET下来,然后decode()一下解码,结果报错。
仔细一看,发现知乎网传给我们的是经过gzip压缩之后的数据。
我们需要先对数据解压,python进行gzip解压很方便
"""
"""
import gzip
def ungzip(data):
    try:    # 尝试解压
        print('正在解压......')
        data = gzip.decompress(data)
        print('解压完毕!')
    except:
        print('未经压缩,无需解压')
        return data

# 通过opener.read()读取回来的数据,经过ungzip自动处理后，再来一遍decode()就可以得到解码后的str了。

_xsrf 这个键的值在茫茫无际的互联网沙漠之中指引我们用正确的姿势来登录知乎, 
所以 _xsrf 可谓沙漠之舟. 如果没有 _xsrf, 
我们或许有用户名和密码也无法登录知乎(
我没试过, 不过我们学校的教务系统确实如此) 
如上文所说, 我们在第一遍 GET 的时候可以从响应报文中的 HTML 代码
里面得到这个沙漠之舟. 
如下函数实现了这个功能, 返回的 str 就是 _xsrf 的值.

import re
def getXSRF(data):
    cer = re.compile('name=\"_xsrf\" value=\"(.*)\"', flags = 0)
    strlist = cer.findall(data)
    return strlist[0]


2.3 发射Post

集齐 _xsrf, id, password 三大法宝, 我们可以发射 POST 了. 
这个 POST 一旦发射过去, 我们就登陆上了服务器, 
服务器就会发给我们 Cookies. 本来处理 Cookies 是个麻烦的事情, 
不过 Python 的 http.cookiejar 库给了我们很方便的解决方案, 
只要在创建 opener 的时候将一个 HTTPCookieProcessor 放进去, 
Cookies 的事情就不用我们管了. 下面的代码体现了这一点.

import http.cookiejar
import urllib.request
def getOpener(data):
    # deal with the Cookies

    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in header.items():
        elem = (key, value)
        header.append(elem)

    opener.addheaders = header
    return opener

"""

"""
登录

对于需要用户登录的网站信息的爬取

"""

import urllib.request,gzip,http.cookiejar,urllib.parse,re
import sys

# 解压缩函数
def ungzip(data):
    try:
        print("正在解压缩...")
        data = gzip.decompress(data)
        print("解压完毕...")
    except:
        print("未经压缩,无需解压...")
    return data

# 构造文件头
def getOpener(header):
    # 设置一个cookie处理器,它负责从服务器下载cookie到本地,并且在发送请求时带上本地的cookie
    cookiejar = http.cookiejar.CookieJar()
    cp = urllib.request.HTTPCookieProcessor(cookiejar)
    opener = urllib.request.build_opener(cp)
    headers = []
    for key, value in header.items():
        elem = (key, value)
        headers.append(elem)
    opener.addheaders = headers
    return opener

# 获取_xsrf
def getXsrf(data):
    cer = re.compile('name=\"_xsrf\" value=\"(.*)\"', flags = 0)
    strlist = cer.findall(data)
    return strlist[0]

# 根据网站报头信息设置headers
headers = {
    'Connection':'Keep-Alive',
    'Accept':'*/*',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36',
    'Accept-Encoding':'gzip,deflate,br',
    'Host':'www.zhihu.com',
    'DNT':'1'
}

url = "https://www.zhihu.com/"
req=urllib.request.Request(url,headers=headers)
res=urllib.request.urlopen(req)

#读取知乎首页内容，获得_xsrf
data = res.read()
data = ungzip(data)
_xsrf = getXsrf(data.decode('utf-8'))

opener = getOpener(headers)
#post数据接收和处理的页面（我们要向这个页面发送我们构造的Post数据）
url+='login/email'
name='2687547643@qq.com'
passwd='zero920410cai'

#分析构造post数据
postDict={
    '_xsrf':_xsrf,
    'email':name,
    'password':passwd,
    'remember_me':'true'
}
#给post数据编码
postData=urllib.parse.urlencode(postDict).encode()

#构造请求
res=opener.open(url,postData)
data = res.read()
#解压缩
data = ungzip(data)
print(data.decode())
