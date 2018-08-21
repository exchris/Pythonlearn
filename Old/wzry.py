# -*- coding:utf-8 -*-
import urllib.request
import json
import os
from builtins import str
from _ast import Str
from numpy import str0

response = urllib.request.urlopen("http://pvp.qq.com/web201605/js/herolist.json");

hero_json = json.loads(response.read())
hero_num = len(hero_json)

# print(hero_json)
# print("hero_num :", str(hero_num))
# 
# hero_name = hero_json[0]['cname']
# skin_names = hero_json[0]['skin_name'].split('|')
# skin_num = len(skin_names)
# 
# print('hero_name:', hero_name)
# print('skin_names:', skin_names)
# print('skin_num:', skin_num)

# 文件不存在则创建
save_dir = "D:\heroskin"
if not os.path.exists(save_dir):
    os.mkdir(save_dir)


for i in range(hero_num):
    # 获取皮肤名称列表
    skin_names = hero_json[i]['skin_name'].split('|')
    
#     for cnt in range(len(skin_names)):
#         
#         save_file_name = 'D:\\heroskin\\' + str(hero_json[i]['ename']) + '--' + str(hero_json[i]['cname']) + '--' + skin_names[cnt] + '.jpg'
#         
#         skin_url = 'http://game.gtimg.cn/images/yzzj/img/201606/skin/hero-info/' + str(hero_json[i]['ename']) + '/' +\
#         str(hero_json[i]['cname']) + '-bigskin' + str(cnt + 1) + '.jpg'
#         
#         urllib.request.urlretrieve(skin_url, save_file_name)
    print(skin_names);
    print();
    
    for cnt in range(len(skin_names)):
        
        # 保存文件名称
        save_file_name = save_dir + '\\' + str(hero_json[i]['ename']) + '-' + str(hero_json[i]['cname']) +\
            '-' + skin_names[cnt] + '.jpg'
        
        print(save_file_name)
#         print(cnt)
#         print(skin_names[cnt])
#         https://game.gtimg.cn/images/yxzj/img201606/heroimg/195/195-smallskin-2.jpg
        # 检测文件是否存在,如果存在则跳过下载
        if not os.path.exists(save_file_name):
            print("存在")
#             http://game.gtimg.cn/images/yxzj/img201606/heroimg/173/173-smallskin-3.jpg
            skin_url = "https://game.gtimg.cn/images/yxzj/img201606/heroimg/" + str(hero_json[i]['ename']) +\
                '/' + str(hero_json[i]['ename'])+'-'+'bigskin-' + str(cnt + 1) + '.jpg'
            urllib.request.urlretrieve(skin_url, save_file_name)
#             print(skin_url)
            
#             //game.gtimg.cn/images/yxzj/img201606/heroimg/195/195-smallskin-2.jpg
        
         