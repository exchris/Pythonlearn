#coding=utf8
import itchat
from itchat.content import *
import time
import requests

KEY = '8edce3ce905a4c1dbb965e6b35c3834d' #图灵机器人的key
 
# 向api发送请求
def get_response(msg):
  apiUrl = 'http://www.tuling123.com/openapi/api'
  data = {
    'key'  : KEY,
    'info'  : msg,
    'userid' : 'pth-robot',
  }
  try:
    r = requests.post(apiUrl, data=data).json()
    return r.get('text')
  except:
    return
# 自动回复
# 封装好的装饰器，当接收到的消息是Text，即文字消息
@itchat.msg_register(['Text'])
def text_reply(msg):
    #回复屏蔽自己还有蔷薇娜
    if not msg['FromUserName'] == nanaUserName and not msg['FromUserName'] == myUserName:
        # 发送一条提示给文件助手
        itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %
                        (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
                         msg['User']['NickName'],
                         msg['Text']), 'filehelper')
		# 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
        defaultReply = 'I received: ' + msg['Text']
        # 如果图灵Key出现问题，那么reply将会是None
        reply = get_response(msg['Text'])
        # 回复给好友
        return reply or defaultReply
		
@itchat.msg_register(['Picture'])
def picture_reply(msg):
    #图片消息，暂时没有想法要怎么做，还有别的消息，加好友，位置，分享等等
    if not msg['FromUserName'] == nanaUserName and not msg['FromUserName'] == myUserName:
        # msg['Text']是一个文件下载函数
		# 传入文件名，将文件下载下来
        msg['Text'](msg['FileName'])
        # 把下载好的文件再发回给发送者
        return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])

# 处理好友添加请求
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.add_friend(**msg['Text']) 
    # 加完好友后，给好友打个招呼
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])

# 处理群聊消息
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg['isAt']:
        itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])
if __name__ == '__main__':
    itchat.auto_login(hotReload=True,enableCmdQR=2)
	
	# 获取好友列表
    friends = itchat.get_friends(update=True)[0:]
    for friend in friends:
        if friend["RemarkName"] == "Nana":
            nanaUserName = friend["UserName"]
            print(friend)		
    # 获取自己的UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    itchat.run()