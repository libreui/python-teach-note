from pygame.sprite import Sprite
from resource import ResourceManager

class Ground(Sprite):
    def __init__(self, flappy):
        super().__init__()
        self.resource = ResourceManager()

        self.flappy = flappy
        self.screen = flappy.screen
        self.screen_rect = flappy.screen.get_rect()
        self.config = flappy.config

        # 加载地面图片
        self.image = self.resource.get_other_images()['base']
        self.rect = self.image.get_rect()
        self.rect.bottomleft = self.screen_rect.bottomleft
        
        # 获取地面图宽度，用于滚动判断
        self.ground_width = self.rect.width
        
        # 第二张地面图的位置（在第一张图右边）
        self.rect2 = self.image.get_rect()
        self.rect2.x = self.ground_width
        self.rect2.bottom = self.screen_rect.bottom
        
        # 累积移动量（用于实现小于1像素的慢速移动）
        # 原理：将每次的小速度累积，只有当累积量>=1时才实际移动
        self.accumulator = 0.0

    def update(self):
        """更新地面位置，实现无限滚动"""
        # 计算当前帧的滚动速度（基础速度 × 地面滚动系数）
        # 地面作为近景，移动速度较快（透视效果）
        scroll_speed = self.config.SPEED * self.config.GROUND_SCROLL_FACTOR
        
        # 累积移动量（关键：实现小于1像素的慢速移动）
        self.accumulator += scroll_speed
        
        # 只有当累积量超过等于1像素时才实际移动
        if self.accumulator >= 1.0:
            # 计算需要移动的像素数（取整）
            move_pixels = int(self.accumulator)
            
            # 移动两张地面图
            self.rect.x -= move_pixels
            self.rect2.x -= move_pixels
            
            # 重置累积器，保留小数部分（用于下次累积）
            self.accumulator -= move_pixels

        # 当第一张图完全移出屏幕左边时，将它放到屏幕最右边
        if self.rect.x <= -self.ground_width:
            self.rect.x = self.ground_width

        # 当第二张图完全移出屏幕左边时，将它放到屏幕最右边
        if self.rect2.x <= -self.ground_width:
            self.rect2.x = self.ground_width

    def draw(self):
        """绘制两张地面图"""
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image, self.rect2)