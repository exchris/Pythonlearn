# encoding:UTF-8
import urllib.request
import re
import os
import random
import time


def getHtml(url):
    data = urllib.request.urlopen(url).read()
    data = data.decode('UTF-8')
    return data


def getData(content):
    # 需要获取资源的正则
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, content)
    return imglist


def saveImg(imageURL, fileName):
    try:
        u = urllib.request.urlopen(imageURL)
        data = u.read()
        f = open(fileName, 'wb')
        f.write(data)
        print(u"save hers img", fileName)
        f.close()
    except urllib.request.HTTPError as e:
        print('1:', e)
        time.sleep(random.choice(range(5, 10)))

    except urllib.request.URLError as e:
        print('2:', e)
        time.sleep(random.choice(range(5, 10)))


def saveImgs(images, name):
    number = 1
    print(name)
    for imageURL in images:
        splitPath = imageURL.split('.')
        fTail = splitPath.pop()
        if len(fTail) > 3:
            fTail = "jpg"
        fileName = name + "/" + str(number) + "." + fTail
        saveImg(imageURL, fileName)
        number += 1


def mkdir(path):
    path = path.strip()
    # 判断路径是否存在 ture存在 false不存在
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print(u"creat", path, u'dir')
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(u"named", path, 'created')
        return False


url = "http://pic.91.com/play/1411/21760879.html#p=10"
data = getHtml(url)
imglist = getData(data)
# 创建目录
mkpath = mkdir('lcm/')
# 保存图片到指定目录
saveImgs(imglist, "img")
print(imglist)
