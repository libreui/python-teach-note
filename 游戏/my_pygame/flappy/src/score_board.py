from pygame import Rect
from resource import ResourceManager

class ScoreBoard:
    def __init__(self, flappy):

        self.screen = flappy.screen # 屏幕表面
        self.screen_rect = flappy.screen.get_rect() # 屏幕矩形

        self.resource = ResourceManager()
        self.images = self.resource.get_score_images()

        self.score = 0 # 得分
        self.score_group = []

        self.rect = Rect(0, 0, 24, 36)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = 50

    def update(self):
        """更新积分板"""
        self.score_group = list(str(self.score))

    def draw(self):
        """绘制积分板"""
        # 计算分数的总宽度
        total_width = len(self.score_group) * self.rect.width
        # 计算起始位置
        start_x = self.screen_rect.centerx - total_width // 2


        for i, digit in enumerate(self.score_group):
            _image = self.images[digit]
            _rect = Rect(start_x + i * self.rect.width, self.rect.y, self.rect.width, self.rect.height)
            self.screen.blit(_image, _rect)


    def reset(self):
        """重置积分板"""
        self.score = 0
        self.score_group = []
