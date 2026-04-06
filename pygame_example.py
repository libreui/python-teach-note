import pygame

class Game:

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    def __init__(self):
        # 游戏初始化
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

        self.rect = pygame.Rect(100, 100, 100, 100)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


    def _draw(self):
        self.screen.fill(self.BLACK)
        self.rect.left += 2
        pygame.draw.rect(self.screen, Game.WHITE, self.rect)


    def start(self):
        """游戏开始"""
        while True:
            self._check_events()

            self._draw()

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.start()

