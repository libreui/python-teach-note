import os

import pygame.image

# /Users/libre1/Code/PythonJupyter/游戏/pygame/tankwar/resources/images/playerTank/tank_T1_0.png
root = os.path.dirname(__file__)
scene_path = f"{root}/resources/images/scene"
play_tank_path = f"{root}/resources/images/playerTank"
others_path = f"{root}/resources/images/others"


class Resources:
    """资源类"""
    def __init__(self):
        self.bg = pygame.image.load(f"{others_path}/background.png")
        self.brick = pygame.image.load(f"{scene_path}/brick.png")
        self.tank_0 = pygame.image.load(f"{play_tank_path}/tank_T1_0.png")
        self.tank_1 = pygame.image.load(f"{play_tank_path}/tank_T1_1.png")
        self.tank_2 = pygame.image.load(f"{play_tank_path}/tank_T1_2.png")

