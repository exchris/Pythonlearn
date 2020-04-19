#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
读懂一个机器人类
@author dev.erxuan@gmail.com
@file Robot.py
@software PyCharm
@date 2020/4/19 10:14
"""


class Robot(object):
    def __init__(self, name):
        # 名字
        self.name = name
        # 身高30cm
        self.height = 30
        # 体重5kg
        self.weight = 5
        # 左脚距离地面0cm
        self.left_foot_from_earth = 0
        # 右脚距离地面0cm
        self.right_foot_from_earth = 0
        # 左手距离地面15cm
        self.left_hand_from_earth = 15
        # 右手距离地面15cm
        self.right_hand_from_earth = 15

    def _adjust_movement(self, part, current_value, displacement):
        """
        脚不能插到地底下，也不能离地高于15cm
        手不能低于身体的一半，也不能高于40cm
        :param part: foot或者hand
        :param current_value:int
        :param displacement:int
        :return:int
        """
        if part == 'foot':
            boundary = [0, 15]
        elif part == 'hand':
            boundary = [15, 40]
        else:
            print('未知的身体部位!')
            return
        new_value = current_value + displacement
        if new_value < boundary[0]:
            return boundary[0]
        elif new_value > boundary[1]:
            return boundary[1]
        else:
            return new_value

    def move_left_foot(self, displacement):
        """
        :param displacement:
        :return:
        """
        left_foot_from_earth = self.left_foot_from_earth + displacement
        if left_foot_from_earth > 0 and self.right_foot_from_earth > 0:
            print('不能双脚同时离地，放弃移动左脚！')
            return
        self.left_foot_from_earth = self._adjust_movement('foot', self.left_foot_from_earth, displacement)
        self.announce()

    def move_right_foot(self, displacement):
        right_foot_from_earth = self.right_foot_from_earth + displacement
        if right_foot_from_earth > 0 and self.left_foot_from_earth > 0:
            print('不能双脚同时离地，放弃移动右脚')
            return
        self.right_foot_from_earth = self._adjust_movement('foot', self.right_foot_from_earth, displacement)
        self.announce()

    def move_left_hand(self, displacement):
        self.left_hand_from_earth = self._adjust_movement('hand', self.left_hand_from_earth, displacement)
        self.announce()

    def move_right_hand(self, displacement):
        self.right_hand_from_earth = self._adjust_movement('hand', self.right_hand_from_earth, displacement)
        self.announce()

    def announce(self):
        print('\n*************************')
        print('左手距离地面:{} cm'.format(self.left_hand_from_earth))
        print('右手距离地面:{} cm'.format(self.right_hand_from_earth))
        print('左脚距离地面:{} cm'.format(self.left_foot_from_earth))
        print('右脚距离地面:{} cm'.format(self.right_foot_from_earth))
        print('**************************\n')

    def dance(self):
        self.move_left_foot(14)
        self.move_right_foot(4)
        self.move_left_hand(20)
        self.move_right_hand(100)
        self.move_right_hand(-5)
        self.move_left_foot(-2)


if __name__ == "__main__":
    robot = Robot('瓦力')
    robot.dance()
    pass
