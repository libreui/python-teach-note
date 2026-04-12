import pygame


class Game:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    def __init__(self):
        # 游戏初始化
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.speed = 10
        self.direction = [0, 0]  # 方向[左右， 上下]

        self.rect = pygame.Rect(100, 100, 100, 100)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                self._key_down(event.key)
            elif event.type == pygame.KEYUP:
                self._key_up(event.key)

    def _key_up(self, key):
        pass
        # if key == pygame.K_LEFT or key == pygame.K_RIGHT:
        #     self.direction[0] = 0
        # elif key == pygame.K_UP or key == pygame.K_DOWN:
        #     self.direction[1] = 0

    def _key_down(self, key):
        pass
        # if key == pygame.K_LEFT and self.rect.left > 0:
        #     self.direction[0] = -1
        # elif key == pygame.K_RIGHT:
        #     self.direction[0] = 1
        # elif key == pygame.K_UP:
        #     self.direction[1] = -1
        # elif key == pygame.K_DOWN:
        #     self.direction[1] = 1

    def _move(self):
        """移动矩形"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.move_ip(-1 * self.speed, 0)
        elif keys[pygame.K_RIGHT] and self.rect.right < self.screen_rect.right:
            self.rect.move_ip(self.speed, 0)
        elif keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.move_ip(0, -1 * self.speed)
        elif keys[pygame.K_DOWN] and self.rect.bottom < self.screen_rect.bottom:
            self.rect.move_ip(0, self.speed)

    def _move_with_mouse(self):
        """移动矩形到鼠标位置"""
        pos = pygame.mouse.get_pos()
        # 矩形移动不要超出屏幕边界
        self.rect.center = pos




    def _draw(self):
        self.screen.fill(self.BLACK)
        # 改变矩形的位置
        # self.rect.move_ip(2, 2)
        pygame.draw.rect(self.screen, Game.WHITE, self.rect)

    def start(self):
        """游戏开始"""
        while True:
            self._check_events()
            self._move_with_mouse()
            self._draw()

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.start()
