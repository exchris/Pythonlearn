#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

# !/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'


# 831。隐藏个人信息

class Solution:

    def maskPII(self, S):
        rst = ''
        if S.find('@') != -1:  #邮箱格式
            name = S.split('@')[0].lower()
            name = name[0] + '*****' + name[-1]
            return name + '@' + S.split('@')[1].lower()
        else:
            n = []
            for c in S:
                if ord(c) >= 48 and ord(c) <= 57:
                    n.append(c)
            if len(n) == 10:
                # 本地号码
                return '***-***-' + ''.join(n[-4:])
            else:
                # 国际号码
                return '+**-***-***-' + ''.join(n[-4:])

if __name__ == "__main__":
    s = Solution()
    print(s.maskPII("86-(10)12345678"))
