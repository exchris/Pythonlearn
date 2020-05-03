#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
@author dev.erxuan@gmail.com
@file urls.py
@software PyCharm
@date 2020/4/25 15:50
"""
from django.urls import path
from hrs import views


urlpatterns = [
    path('', views.index, name='index'),
    path('table', views.table, name='table'),
    path('helloworld', views.helloWorld, name='helloWorld'),
]