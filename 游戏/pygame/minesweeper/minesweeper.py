import pygame
from pygame.sprite import Sprite


class Minesweeper:
    def __init__(self):
        self.config = Config()
        self.state = State(self.config)

        pygame.init()
        pygame.display.set_caption(self.config.caption)
        self.screen = pygame.display.set_mode((self.config.width, self.config.height))
        self.clock = pygame.time.Clock()

        self._init_mines()

    def _init_mines(self):
        for i in range(self.config.mines_size):
            for j in range(self.config.mines_size):
                self.state.mines[i][j] = Mine(self, i, j)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_mines_clicked(event)

    def _check_mines_clicked(self, event):
        pos = pygame.mouse.get_pos()
        # 区分左键还是右键
        if event.button == 1: # 左键点击
            for row in self.state.mines:
                for mine in row:
                    if mine is not None:
                        mine.on_mouse_left_down(pos)
        elif event.button == 3: # 右键点击
            for row in self.state.mines:
                for mine in row:
                    if mine is not None:
                        mine.on_mouse_right_down(pos)


    def run(self):
        while True:
            self.screen.fill(self.config.bg_color)
            self.clock.tick(self.config.fps)
            self._check_events()

            self._draw_mines()

            pygame.display.flip()

    def _draw_mines(self):
        for row in self.state.mines:
            for mine in row:
                if mine is not None:
                    mine.draw()

class Config:
    def __init__(self):
        self.caption = "Minesweeper"

        self.mines_size = 25
        self.grid_size = 10

        self.width = self.mines_size * self.grid_size
        self.height = self.mines_size * self.grid_size
        self.fps = 60
        self.bg_color = (192, 192, 192)



class State:
    def __init__(self, config):
        self.config = config
        # 储存每个格子地雷数量的二位数组，初始值为None
        self.mines = [[None for _ in range(self.config.mines_size)] for _ in range(self.config.mines_size)]


class Mine(Sprite):
    def __init__(self, game, row, col):
        super().__init__()
        self.screen = game.screen
        self.config = game.config
        self.x = row * self.config.mines_size
        self.y = col * self.config.mines_size
        self.mark = False
        self.is_clicked = False

        self.image = pygame.image.load("./image/9.gif")
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)


    def draw(self):
        self.screen.blit(self.image, self.rect)

    def on_mouse_right_down(self, pos):
        if self.rect.collidepoint(pos):
            if self.is_clicked:
                return
            self.mark = not self.mark
            if self.mark:
                self.image = pygame.image.load("./image/10.gif")
            else:
                self.image = pygame.image.load("./image/9.gif")


    def on_mouse_left_down(self, pos):
        if self.rect.collidepoint(pos) and self.mark is not True:
            self.image = pygame.image.load("./image/0.jpg")
            self.is_clicked = True





if __name__ == "__main__":
    minesweeper = Minesweeper()
    minesweeper.run()