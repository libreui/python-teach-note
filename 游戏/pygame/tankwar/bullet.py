from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, tw, tank):
        super().__init__()
        self.settings = tw.settings
        self.screen = tw.screen
        self.screen_rect = tw.screen.get_rect()
        self.res = tw.res
        self.image = self.res.bullet_up
        self.rect = self.image.get_rect()
        self.direction = tank.direction
        self.rect.center = tank.rect.center


    def update(self):
        if self.direction == 'up':
            self.image = self.res.bullet_up
            self.rect.y -= self.settings.bullet_speed
        elif self.direction == 'down':
            self.image = self.res.bullet_down
            self.rect.y += self.settings.bullet_speed
        elif self.direction == 'left':
            self.image = self.res.bullet_left
            self.rect.x -= self.settings.bullet_speed
        elif self.direction == 'right':
            self.image = self.res.bullet_right
            self.rect.x += self.settings.bullet_speed



