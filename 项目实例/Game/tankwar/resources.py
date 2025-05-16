import os

import pygame.image

# /Users/libre1/Code/PythonJupyter/游戏/pygame/tankwar/resources/images/playerTank/tank_T1_0.png
root = os.path.dirname(__file__)
scene_path = f"{root}/resources/images/scene"
play_tank_path = f"{root}/resources/images/playerTank"
others_path = f"{root}/resources/images/others"
bullet_path = f"{root}/resources/images/bullet"
home_path = f"{root}/resources/images/home"
enemy_tank_path = f"{root}/resources/images/enemyTank"


class Resources:
    def __init__(self):
        # 加载背景图片
        self.bg = pygame.image.load(f"{others_path}/background.png")

        # 加载地图元素图片
        self.brick = pygame.image.load(f"{scene_path}/brick.png")
        self.iron = pygame.image.load(f"{scene_path}/iron.png")
        self.ice = pygame.image.load(f"{scene_path}/ice.png")

        # 加载家
        self.home_1 = pygame.image.load(f"{home_path}/home1.png")
        self.home_2 = pygame.image.load(f"{home_path}/home2.png")
        self.home_destroyed = pygame.image.load(f"{home_path}/home_destroyed.png")

        # 加载坦克图片
        self.tank_0 = pygame.image.load(f"{play_tank_path}/tank_T1_0.png")
        self.tank_1 = pygame.image.load(f"{play_tank_path}/tank_T1_1.png")
        self.tank_2 = pygame.image.load(f"{play_tank_path}/tank_T1_2.png")
        # 加载子弹
        self.bullet_up = pygame.image.load(f"{bullet_path}/bullet_up.png")
        self.bullet_down = pygame.image.load(f"{bullet_path}/bullet_down.png")
        self.bullet_right = pygame.image.load(f"{bullet_path}/bullet_right.png")
        self.bullet_left = pygame.image.load(f"{bullet_path}/bullet_left.png")

        # 敌人坦克
        self.enemy_tank = [
            [
                pygame.image.load(f"{enemy_tank_path}/enemy_1_0.png"),
                pygame.image.load(f"{enemy_tank_path}/enemy_1_1.png"),
                pygame.image.load(f"{enemy_tank_path}/enemy_1_2.png"),
                pygame.image.load(f"{enemy_tank_path}/enemy_1_3.png")
            ],
            [
                pygame.image.load(f"{enemy_tank_path}/enemy_2_0.png"),
                pygame.image.load(f"{enemy_tank_path}/enemy_2_1.png"),
                pygame.image.load(f"{enemy_tank_path}/enemy_2_2.png")
            ],
            [
                pygame.image.load(f"{enemy_tank_path}/enemy_3_0.png"),
                pygame.image.load(f"{enemy_tank_path}/enemy_3_1.png"),
                pygame.image.load(f"{enemy_tank_path}/enemy_3_2.png"),
                pygame.image.load(f"{enemy_tank_path}/enemy_3_3.png")
            ],
            [
                pygame.image.load(f"{enemy_tank_path}/enemy_4_0.png"),
                pygame.image.load(f"{enemy_tank_path}/enemy_4_1.png"),
                pygame.image.load(f"{enemy_tank_path}/enemy_4_2.png"),
                pygame.image.load(f"{enemy_tank_path}/enemy_4_3.png")
            ]
        ]
