"""
Created on 八月 03 2017
@author: dev.erxuan@gmail.com
@description: requests introduction
"""
# -*- coding: utf-8 -*-
import requests

"""
获取Github的公共时间线
r = requests.get('https://github.com/timeline.json')
<Response [410]>
"""

"""
payload = {'key1':'value1','key2':'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url)
http://httpbin.org/get?key1=value1&key2=value2

payload = {'key1':'value1','key2':['value2','value3']}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)
http://httpbin.org/get?key1=value1&key2=value2&key2=value3
"""

"""
r = requests.get('https://github.com/timeline.json')
print(r.text)
{"message":"Hello there, wayfaring stranger. If you’re reading this then you probably didn’t see our blog post a couple of years back announcing that this API would go away: http://git.io/17AROg Fear not, you should be able to get what you need from the shiny new Events API instead.","documentation_url":"https://developer.github.com/v3/activity/events/#list-public-events"}
"""

"""
二进制数据
r = requests.get('https://github.com/timeline.json')
print(r.content)
b'{"message":"Hello there, wayfaring stranger. If you\xe2\x80\x99re reading this then you probably didn\xe2\x80\x99t see our blog post a couple of years back announcing that this API would go away: http://git.io/17AROg Fear not, you should be able to get what you need from the shiny new Events API instead.","documentation_url":"https://developer.github.com/v3/activity/events/#list-public-events"}'
"""

"""
r = requests.get('https://github.com/timeline.json', stream=True)
print(r.raw)

filename = "test.txt"
with open(filename, 'wb') as fd:
    for chunk in r.iter_content(chunk_size=20):
        fd.write(chunk)
"""

"""
payload = {'key1':'value1','key2':'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "key1": "value1", 
    "key2": "value2"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Length": "23", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.18.1"
  }, 
  "json": null, 
  "origin": "120.42.88.74", 
  "url": "http://httpbin.org/post"
}
"""

import json

url = 'https://api.github.com/some/endpoint'
payload = {'some':'data'}

r = requests.post(url,data=json.dumps(payload))
print(r.text)