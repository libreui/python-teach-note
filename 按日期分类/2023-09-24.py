import random

i = 0  # 计次
a = random.randint(1, 50)  # 随机数
# continue 放弃当前循环，执行下一次循环
while True:
    # 计次并询问部分
    if i > 2:
        n = input('您是否想继续玩：')
        if n == 'y' or n == 'Y':
            i = 0
        elif n == 'n' or n == 'N':
            break
        else:
            continue

    # 游戏部分
    t = int(input('请猜猜小明的年龄：'))
    if t > a:
        print('猜大了！')
    elif t < a:
        print('猜小了!')
    else:
        print('猜对了！')

    i += 1


