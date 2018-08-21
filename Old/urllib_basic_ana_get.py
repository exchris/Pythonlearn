"""
Created on 七月 28 2017
@author: dev.erxuan@gmail.com
"""
# -*- coding: utf-8 -*-

# 如果我们要想模拟浏览器发送GET请求,
# 就需要使用Request对象,通过往Request对象添加HTTP头,
# 我们就可以把请求伪装成浏览器。例如,模拟iPhone6去请求豆瓣首页

from urllib import request

req = request.Request('http://www.douban.com')
headers = "'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 " \
          "(KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25"

req.add_header("User-Agent", headers)

with request.urlopen(req) as f:
    print("Status:\n")
    print("Status:", f.status, f.reason)

    for k, v in f.getheaders():
        print("头部信息:\n")
        print("%s : %s" % (k, v))

    print("Data:\n")
    # 抓取的内容
    data = f.read().decode('utf-8')
    # 将抓取的内容写入到test.html文件中
    with open('test.html', 'w', encoding='utf-8') as wf:
        wf.write(data)
        wf.close()


