#!/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = 'exchris'

class Solution:

    def judgeCircle(self, moves):
        return moves.count("L") == moves.count("R") and moves.count("U") == moves.count("P")
