from pygame.sprite import Sprite
import pygame


class Bullet(Sprite):
    """子弹类"""
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.rect = pygame.Rect(0, 0, self.settings.bullet_radius, self.settings.bullet_radius)

        self.x, self.y = game.plane.rect.centerx, game.plane.rect.top - 20
        self.rect.centerx = self.x
        self.rect.top = self.y

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.top = self.y

    def check_edge(self):
        return self.y <= 0

    def draw_bullet(self):
        pygame.draw.circle(self.screen,
                           self.settings.bullet_color,
                           (int(self.x), int(self.y)),
                           self.settings.bullet_radius)
