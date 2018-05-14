# -*- coding: utf-8 -*-
import time

__author__ = 'l'
__date__ = '2018/5/14'
"""
可视化
"""
import numpy as np


class Maze:
    def __init__(self):
        bg = np.zeros((10, 10))  # 背景
        # 定义初始化位置 1为动点位置
        # 定义坑的位置
        bg[2][2] = 2
        bg[2][3] = 2
        bg[2][4] = 2
        bg[3][1] = 2
        bg[3][1] = 2
        bg[6][4] = 2
        bg[6][6] = 2
        # 定义终点位置
        bg[5][5] = 3
        self.bg = bg
        self.actor_x = 0
        self.actor_y = 0
        """定义行为"""
        self.action_space = ['u', 'd', 'l', 'r']  # 行为

    def reset(self):
        """
        回到起点
        :return:
        """
        self.actor_x = 0
        self.actor_y = 0
        return '0_0'

    def step(self, action):
        if action == 0:  # 上
            if 0 < self.actor_x <= 9:
                self.actor_x = self.actor_x - 1
        elif action == 1:  # 下
            if 0 <= self.actor_x < 9:
                self.actor_x = self.actor_x + 1
        elif action == 2:  # 右
            if 0 <= self.actor_y < 9:
                self.actor_y = self.actor_y + 1
        elif action == 3:  # 左
            if 0 < self.actor_y <= 9:
                self.actor_y = self.actor_y - 1
        s_ = str(self.actor_x) + '_' + str(self.actor_y)
        # 奖励系统
        if self.bg[self.actor_x][self.actor_y] == 3:
            reward = 1000000
            done = True
            s_ = 'terminal'
        elif self.bg[self.actor_x][self.actor_y] == 2:
            reward = -1000
            done = True
            s_ = 'terminal'

        else:
            reward = -1
            done = False

        return s_, reward, done
