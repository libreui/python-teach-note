import sys

import pygame
from pygame import Rect
from pygame.sprite import Sprite, Group
from pygame.time import Clock


class Block(Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen

        self.block = game.block
        self.x, self.y = 200, 200
        self.rect = Rect(self.x, self.y, self.block, self.block)

    def update(self, x, y):
        self.x = x
        self.y = y

        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect)


class Snake:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("贪吃蛇")

        self.block = 10
        self.clock = Clock()

        self.x_head = self.width // 2
        self.y_head = self.height // 2

        self.x_change = 0
        self.y_change = 0


        self.snakes = []
        self.snake_length = 1

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.x_change = -1
                    self.y_change = 0
                elif event.key == pygame.K_RIGHT:
                    self.x_change = 1
                    self.y_change = 0
                elif event.key == pygame.K_UP:
                    self.x_change = 0
                    self.y_change = -1
                elif event.key == pygame.K_DOWN:
                    self.x_change = 0
                    self.y_change = 1
                elif event.key == pygame.K_SPACE:
                    self.snake_length += 1

    def _update_score(self):
        # 当前蛇头的位置
        self.x_head += self.x_change * self.block
        self.y_head += self.y_change * self.block

        # 添加蛇头
        self.snakes.append([self.x_head, self.y_head])

        if len(self.snakes) > self.snake_length:
            del self.snakes[0]

        # 填充屏幕
        self.screen.fill((0, 0, 0))

        # 绘制蛇
        self._draw_snakes()

        pygame.display.update()

    def _draw_snakes(self):
        """绘制蛇身"""
        for snake in self.snakes:
            pygame.draw.rect(self.screen, (255, 255, 255), (snake[0], snake[1], self.block, self.block))

    def run(self):
        while True:
            self._check_events()
            self._update_score()

            self.clock.tick(20)



if __name__ == "__main__":
    game = Snake()
    game.run()


