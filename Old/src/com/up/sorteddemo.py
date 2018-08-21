# -*- coding:UTF-8 -*-
def cmp_ignore_case(s1, s2):
    if s1.lower() > s2.lower():
        return 1
    if s1.lower() < s2.lower():
        return -1
    return 0

L = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(L,key=lambda x:x.upper()))