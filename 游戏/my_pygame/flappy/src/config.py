import pygame


class Config:
    WIDTH = 288  # 游戏窗口宽度
    HEIGHT = 512  # 游戏窗口高度
    TITLE = 'Flappy Bird'  # 游戏窗口标题
    FPS = 60
    GRAVITY = 0.3  # 重力加速度
    SPEED = 1  # 基础速度

    # 滚动速率系数（基于基础速度计算）
    BG_SCROLL_FACTOR = 0.5  # 背景滚动系数（远景较慢）
    GROUND_SCROLL_FACTOR = 0.75  # 地面滚动系数（近景较快）

    # 游戏颜色
    BG_COLOR = (0, 0, 0)

    # 小鸟颜色
    BIRD_COLOR = 'blue'  # 小鸟颜色 blue red yellow

    ANIM_SCROLL_FACTOR = 0.06  # 动画滚动系数（越小越快 0.01 ~ 1）

    # 管道颜色
    PIPE_COLOR = 'green'  # 管道颜色 green red
    PIPE_WIDTH = 52  # 管道宽度
    PIPE_HEIGHT = 320  # 管道高度
    PIPE_GAP = 120  # 管道间距
    PIPE_SPACING = 150  # 管道间距

