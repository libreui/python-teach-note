import pygame.image
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load("./images/alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """检测碰撞边缘"""
        screen_rect = self.screen.get_rect()
        if self.rect.left < screen_rect.left or self.rect.right > screen_rect.right:
            return True 
        
    def down(self):
        self.rect.y += self.settings.fleet_drop_speed
