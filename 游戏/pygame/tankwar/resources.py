import os

import pygame.image

# /Users/libre1/Code/PythonJupyter/游戏/pygame/tankwar/resources/images/playerTank/tank_T1_0.png
root = os.path.dirname(__file__)
scene_path = f"{root}/resources/images/scene"
play_tank_path = f"{root}/resources/images/playerTank"
others_path = f"{root}/resources/images/others"
bullet_path = f"{root}/resources/images/bullet"


class Resources:
    def __init__(self):
        # 加载背景
        self.bg = pygame.image.load(f"{others_path}/background.png")

        # 加载砖块
        self.brick = pygame.image.load(f"{scene_path}/brick.png")
        # 加载金属
        self.iron = pygame.image.load(f"{scene_path}/iron.png")

        # 加载坦克
        self.tank_0 = pygame.image.load(f"{play_tank_path}/tank_T1_0.png")
        self.tank_1 = pygame.image.load(f"{play_tank_path}/tank_T1_1.png")
        self.tank_2 = pygame.image.load(f"{play_tank_path}/tank_T1_2.png")

        # 加载子弹
        self.bullet_up = pygame.image.load(f"{bullet_path}/bullet_up.png")
        self.bullet_down = pygame.image.load(f"{bullet_path}/bullet_down.png")
        self.bullet_left = pygame.image.load(f"{bullet_path}/bullet_left.png")
        self.bullet_right = pygame.image.load(f"{bullet_path}/bullet_right.png")
