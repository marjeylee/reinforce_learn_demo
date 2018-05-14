# -*- coding: utf-8 -*-
__author__ = 'l'
__date__ = '2018/5/14'
"""
具体Sarsa类
"""

import numpy as np
import pandas as pd


class RL(object):
    def __init__(self, action_space, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        """
        初始化对象
        :param action_space:
        :param learning_rate:  学习率
        :param reward_decay:  奖励衰减
        :param e_greedy: 放飞自我概率
        """
        self.actions = action_space
        self.lr = learning_rate
        self.gamma = reward_decay
        self.epsilon = e_greedy
        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)

    def check_state_exist(self, state):
        """
        检查状态是否已知
        :param state:
        :return:
        """
        if state not in self.q_table.index:
            self.q_table = self.q_table.append(
                pd.Series(
                    [0] * len(self.actions),
                    index=self.q_table.columns,
                    name=state,
                )
            )

    def choose_action(self, observation):
        """
        进行行为选择
        :param observation:
        :return:
        """
        self.check_state_exist(observation)
        if np.random.rand() < self.epsilon:
            # 正常按照经验走
            state_action = self.q_table.loc[observation, :]
            state_action = state_action.reindex(
                np.random.permutation(state_action.index))
            action = state_action.idxmax()
        else:
            # 随机乱走
            action = np.random.choice(self.actions)
        return action

    def learn(self, *args):
        pass


class SarsaTable(RL):
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        super(SarsaTable, self).__init__(actions, learning_rate, reward_decay, e_greedy)

    def learn(self, s, a, r, s_, a_):
        """
        覆写学习方法
        :param s:观测到状态
        :param a:
        :param r:
        :param s_:
        :param a_:
        :return:
        """
        self.check_state_exist(s_)
        q_predict = self.q_table.loc[s, a]
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table.loc[s_, a_]  # 未结束
        else:
            q_target = r  #
        self.q_table.loc[s, a] += self.lr * (q_target - q_predict)  # update
