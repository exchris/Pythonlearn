# -*- coding:utf-8 -*-
import requests 

payload = {'wd':'exchris', 'rn':'100'}
r = requests.get("http://www.baidu.com/s", params=payload)
print(r.url)
print()
print(r.encoding)

# json
r = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=122.88.60.28')
jsonone = r.json()['data']['country']
"""
print(r.json())
{u'code': 0, u'data': {u'ip': u'122.88.60.28', u'city': u'\u5357\u4eac\u5e02', u'area_id': u'300000', u'region_id': u'320000', u'area': u'\u534e\u4e1c', u'city_id': u'320100', u'country': u'\u4e2d\u56fd', u'region': u'\u6c5f\u82cf\u7701', u'isp': u'\u94c1\u901a', u'country_id': u'CN', u'county': u'', u'isp_id': u'100020', u'county_id': u'-1'}}
"""
print(jsonone)

# 网页状态码
r = requests.get('http://www.mengtiaokong.com')
print(r.status_code)
r = requests.get('http://www.baidu.com/link?url=QeTRFOS7TuUQRppa0wlTJJr6FfIYI1DJprJukx4Qy0XnsDO_s9baoO8u1wvjxgqN')
print(r.url)
print(r.history)


# 禁止跳转
r = requests.get('http://www.baidu.com/link?url=QeTRFOS7TuUQRppa0wlTJJr6FfIYI1DJprJukx4Qy0XnsDO_s9baoO8u1wvjxgqN', allow_redirects = False)
print(r.status_code)
