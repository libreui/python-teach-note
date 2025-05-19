import random

from pygame.sprite import Sprite


class EnemyTank(Sprite):
    def __init__(self, tw, elements, pos=(0, 0)):
        super().__init__()
        self.tw = tw
        self.map = tw.map
        self.res = tw.res
        self.elements = elements
        self.direction = self._get_direction()
        # 等级
        self.level = random.randint(0, 3)
        self.tank_image = self.res.enemy_tank[0][0]
        self.image = self._get_direction_image()
        self.rect = self.image.get_rect()

    def _get_direction(self):
        return random.choice(['up', 'down', 'left', 'right'])

    def _get_direction_image(self):
        if self.direction == 'up':
            return self.tank_image.subsurface((0, 0), (96, 48))
        elif self.direction == 'down':
            return self.tank_image.subsurface((0, 48), (96, 48))
        elif self.direction == 'left':
            return self.tank_image.subsurface((0, 96), (96, 48))
        elif self.direction == 'right':
            return self.tank_image.subsurface((0, 144), (96, 48))