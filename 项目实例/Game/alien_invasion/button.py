import pygame


class Button:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # 设置按钮的一些基本属性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)

        # 按钮矩形
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 文字对象 + 文字大小
        self.font = pygame.font.SysFont(None, 48)

        # 绘制文字
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """绘制按钮文字"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """绘制按钮"""
        # 绘制按钮矩形
        self.screen.fill(self.button_color, self.rect)
        # 绘制按钮文字
        self.screen.blit(self.msg_image, self.msg_image_rect)
