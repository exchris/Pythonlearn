"""
Created on 七月 28 2017
@author: dev.erxuan@gmail.com
"""
# -*- coding: utf-8 -*-
# 通过一个Proxy去访问网站,我们需要利用ProxyHandler来处理

# with proxy and proxy auth:
from urllib import request
proxy_handler = request.ProxyHandler({'http','http://www.example.com:3128/'})
proxy_auth_handler = request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm','host','username','password')
opener = request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass


