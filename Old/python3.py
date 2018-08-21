 import urllib.request
 import re

 def downloadPage(url):
     h = urllib.request.urlopen(url)
     return h.read().decode('utf-8')

 def downloadImg(content):
     pattern = r'src="(.+?\.jpg)"pic_ext'
     m = re.compile(pattern)
     urls = re.findall(m, content)

 def downloadImg(content):
     pattern = r'src="(.+?\.jpg)"pic_ext'
     m = re.compile(pattern)
     urls = re.findall(m, content)
     for i, url in enumerate(urls):
         urllib.request.urlretrieve(url, "%s.jpg" %(i,))

 content = downloadPage("http://tieba.baidu.com/p/2460150866")
 downloadImg(content)