#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

class Solution:
    def numUniqueEmails(self, emails):
        email_set = set()
        for email in emails:
            name, domain = email.split('@')
            name = name[:name.find('+')].replace('.', '')
            email_set.add(name + '@' + domain)
        return len(email_set)

s =Solution()
s.numUniqueEmails()


