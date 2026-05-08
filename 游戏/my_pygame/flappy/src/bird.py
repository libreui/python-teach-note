from pygame.sprite import pygame
from pygame.sprite import Sprite
from resource import ResourceManager
from config import Config


class Bird(Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()

        self.config = Config()
        self.resource = ResourceManager()

        # 加载三种翅膀状态的图片
        self.bird_images = {
            'up': self.resource.get_bird_images()[f'{Config.BIRD_COLOR}_up'],
            'mid': self.resource.get_bird_images()[f'{Config.BIRD_COLOR}_mid'],
            'down': self.resource.get_bird_images()[f'{Config.BIRD_COLOR}_down']
        }
        
        # 当前帧索引和帧计数器
        self.frame_index = 0  # 初始帧索引为0（中状态）
        self.frame_counter = 0  # 帧计数器，用于控制翅膀煽动速度
        self.animation_speed = 100 * self.config.ANIM_SCROLL_FACTOR  # 控制翅膀煽动速度
        
        self.original_image = self.bird_images['mid']
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = 0
        self.angle = 0  # 初始角度为0度

    def jump(self):
        """小鸟跳跃"""
        self.velocity = -5
        self.angle = 45  # 跳跃时向上旋转45度

    def update(self):
        """更新小鸟位置和动画"""
        self.velocity += self.config.GRAVITY
        self.rect.y += self.velocity
        
        # 下落时向下旋转，最多旋转45度
        if self.velocity > 0:
            self.angle = max(-45, self.angle - 3)  # 逐渐向下旋转


    def animation(self):
        """更新翅膀煽动动画"""
        self.frame_counter += 1
        if self.frame_counter >= self.animation_speed:
            self.frame_counter = 0
            self.frame_index = (self.frame_index + 1) % 3
            # 根据帧索引选择对应的翅膀图片
            if self.frame_index == 0:
                self.original_image = self.bird_images['up']
            elif self.frame_index == 1:
                self.original_image = self.bird_images['mid']
            else:
                self.original_image = self.bird_images['down']

    def draw(self, surface):
        """绘制小鸟"""
        # 旋转图像
        rotated_image = pygame.transform.rotate(self.original_image, self.angle)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        surface.blit(rotated_image, rotated_rect)