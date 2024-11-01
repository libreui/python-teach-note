import gym_gomoku
import numpy as np

# 创建游戏环境
env = gym_gomoku.make('Gomoku-v0')
env.reset()


# 定义玩家下棋函数（这里简单地通过输入获取坐标）
def player_move():
    move_str = input("请输入你要下棋的坐标（格式：x,y）：")
    x, y = map(int, move_str.split(","))
    return [x, y]


# 进行人机对战循环
while True:
    # 玩家下棋
    player_action = player_move()
    observation, reward, done, info = env.step(player_action)
    env.render()
    if done:
        if info['winner'] == 'player':
            print("恭喜你，你赢了！")
        elif info['winner'] == 'opponent':
            print("很遗憾，你输了！")
        else:
            print("平局！")
        break

    # 假设对手（这里简单模拟一个随机下棋的对手）
    opponent_action = [np.random.randint(env.action_space.low[0], env.action_space.high[0]),
                       np.random.randint(env.action_space.low[1], env.action_space.high[1])]
    observation, reward, done, info = env.step(opponent_action)
    env.render()
    if done:
        if info['winner'] == 'player':
            print("恭喜你，你赢了！")
        elif info['winner'] == 'opponent':
            print("很遗憾，你输了！")
        else:
            print("平局！")
        break
