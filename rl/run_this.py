# -*- coding: utf-8 -*-
from rl.visualization import Maze

__author__ = 'l'
__date__ = '2018/5/14'
"""
运行文件
"""
from rl.Sarsar import SarsaTable


def train(RL, env):
    """
    进行训练
    :return:
    """
    for episode in range(1000):
        observation = env.reset()  # 初始化可视化环境
        # 选择行动
        action = RL.choose_action(observation)

        while True:
            # 只要返回 目前状况、奖励、是否结束
            observation_, reward, done = env.step(action)
            if observation_ == 'terminal':
                print('(' + str(env.actor_x) + ',' + str(env.actor_y) + ')')
                print()
                observation_ = env.reset()

            # 基于目前情况选择下一操作
            print('(' + str(env.actor_x) + ',' + str(env.actor_y) + ')', end=',')
            action_ = RL.choose_action(str(observation_))
            RL.learn(str(observation), action, reward, str(observation_), action_)
            observation = observation_
            action = action_

            # 训练结束
            if done:
                break

    # end of game
    print('game over')


if __name__ == "__main__":
    env = Maze()
    RL = SarsaTable(actions=list(range(4)))
    train(RL, env)
