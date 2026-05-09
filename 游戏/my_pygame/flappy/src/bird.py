from pygame.sprite import Sprite
from resource import ResourceManager
from config import Config
from pygame import transform


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
        self.rotated_rect = self.rect  # 旋转后的矩形，用于碰撞检测

    def jump(self):
        """小鸟跳跃"""
        self.velocity = -5
        self.angle = 45  # 跳跃时向上旋转45度

    def update(self):
        """更新小鸟位置和动画"""
        self.velocity += self.config.GRAVITY
        self.rect.y += self.velocity

        # 屏幕上边界判断
        if self.rect.y <= 0:
            self.rect.y = 0

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
        rotated_image = transform.rotate(self.original_image, self.angle)
        self.rotated_rect = rotated_image.get_rect(center=self.rect.center)
        surface.blit(rotated_image, self.rotated_rect)

    def check_ground_collision(self, ground_y):
        """检测小鸟是否落地（使用旋转后的矩形进行精确碰撞）"""
        return self.rotated_rect.bottom >= ground_y

    def reset(self):
        """重置小鸟状态"""
        self.rect.center = (50, 150)
        self.velocity = 0
        self.angle = 0
        self.rotated_rect = self.rect
