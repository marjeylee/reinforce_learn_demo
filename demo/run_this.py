"""
主要app
"""

from demo.maze_env import Maze
from demo.RL_brain import SarsaTable


def update():
    for episode in range(100):
        observation = env.reset()  # 初始化可视化环境
        # 选择行动
        action = RL.choose_action(str(observation))

        while True:
            env.render()

            # 只要返回 目前状况、奖励、是否结束
            observation_, reward, done = env.step(action)

            # 基于目前情况选择下一操作
            action_ = RL.choose_action(str(observation_))

            RL.learn(str(observation), action, reward, str(observation_), action_)
            observation = observation_
            action = action_

            # 训练结束
            if done:
                break

    # end of game
    print('game over')
    env.destroy()


if __name__ == "__main__":
    env = Maze()
    RL = SarsaTable(actions=list(range(env.n_actions)))

    env.after(10, update)
    env.mainloop()
