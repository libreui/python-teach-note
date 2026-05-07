import pygame
import os
from typing import Dict


class ResourceManager:
    """资源管理类，负责统一加载和管理游戏资源"""

    def __init__(self):
        """初始化资源管理器"""
        # 背景图片资源
        self.background_images: Dict[str, pygame.Surface] = {}
        # 小鸟图片资源
        self.bird_images: Dict[str, pygame.Surface] = {}
        # 管道图片资源
        self.pipe_images: Dict[str, pygame.Surface] = {}
        # 其他图片资源
        self.other_images: Dict[str, pygame.Surface] = {}
        # 资源加载标志
        self.images_loaded = False

    def load_images(self):
        """加载所有游戏图片资源"""
        if not self.images_loaded:
            try:
                # 获取当前脚本所在目录的绝对路径
                script_dir = os.path.dirname(os.path.abspath(__file__))
                # 构建sprites目录的绝对路径
                sprites_dir = os.path.join(os.path.dirname(script_dir), "sprites")

                # 加载背景图片
                self.background_images = {
                    "day": pygame.image.load(os.path.join(sprites_dir, "background-day.png")).convert(),
                    "night": pygame.image.load(os.path.join(sprites_dir, "background-night.png")).convert(),
                }

                # 加载小鸟图片（蓝色鸟）
                self.bird_images = {
                    "blue_down": pygame.image.load(os.path.join(sprites_dir, "bluebird-downflap.png")).convert_alpha(),
                    "blue_mid": pygame.image.load(os.path.join(sprites_dir, "bluebird-midflap.png")).convert_alpha(),
                    "blue_up": pygame.image.load(os.path.join(sprites_dir, "bluebird-upflap.png")).convert_alpha(),
                    "red_down": pygame.image.load(os.path.join(sprites_dir, "redbird-downflap.png")).convert_alpha(),
                    "red_mid": pygame.image.load(os.path.join(sprites_dir, "redbird-midflap.png")).convert_alpha(),
                    "red_up": pygame.image.load(os.path.join(sprites_dir, "redbird-upflap.png")).convert_alpha(),
                    "yellow_down": pygame.image.load(os.path.join(sprites_dir, "yellowbird-downflap.png")).convert_alpha(),
                    "yellow_mid": pygame.image.load(os.path.join(sprites_dir, "yellowbird-midflap.png")).convert_alpha(),
                    "yellow_up": pygame.image.load(os.path.join(sprites_dir, "yellowbird-upflap.png")).convert_alpha(),
                }

                # 加载管道图片
                self.pipe_images = {
                    "green": pygame.image.load(os.path.join(sprites_dir, "pipe-green.png")).convert_alpha(),
                    "red": pygame.image.load(os.path.join(sprites_dir, "pipe-red.png")).convert_alpha(),
                }

                # 加载其他图片
                self.other_images = {
                    "base": pygame.image.load(os.path.join(sprites_dir, "base.png")).convert_alpha(),
                    "gameover": pygame.image.load(os.path.join(sprites_dir, "gameover.png")).convert_alpha(),
                    "message": pygame.image.load(os.path.join(sprites_dir, "message.png")).convert_alpha(),
                }

                self.images_loaded = True
                print("资源加载成功")
            except pygame.error as e:
                print(f"资源加载失败: {e}")

    def get_background_images(self) -> Dict[str, pygame.Surface]:
        """获取背景图片资源"""
        if not self.images_loaded:
            self.load_images()
        return self.background_images

    def get_bird_images(self) -> Dict[str, pygame.Surface]:
        """获取小鸟图片资源"""
        if not self.images_loaded:
            self.load_images()
        return self.bird_images

    def get_pipe_images(self) -> Dict[str, pygame.Surface]:
        """获取管道图片资源"""
        if not self.images_loaded:
            self.load_images()
        return self.pipe_images

    def get_other_images(self) -> Dict[str, pygame.Surface]:
        """获取其他图片资源"""
        if not self.images_loaded:
            self.load_images()
        return self.other_images
