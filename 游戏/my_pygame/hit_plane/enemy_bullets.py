from pygame.sprite import Sprite
import pygame


class EnemyBullet(Sprite):
    def __init__(self, enemy):
        super().__init__()
        self.screen = enemy.screen
        self.settings = enemy.settings
        self.rect = pygame.Rect(0, 0, 2*self.settings.enemy_bullet_radius, 2*self.settings.enemy_bullet_radius)
        self.rect.center = enemy.rect.center

        self.x, self.y = self.rect.center
        self.dx = 0 # 水平方向速度
        self.dy = 0 # 垂直方向速度

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.rect.x = self.x
        self.rect.x = self.y
        if self.y > self.screen.get_rect().bottom:
            self.kill()

    def check_edge(self):
        return self.y <= 0

    def show_bullet(self):
        pygame.draw.circle(self.screen,
                           self.settings.enemy_bullet_color,
                           (int(self.x), int(self.y)),
                           self.settings.enemy_bullet_radius)
