import pygame

from settings import Settings
from cube_shape import CubeShape


class Tetris:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.height))

        self.clock = pygame.time.Clock()
        self.cube = CubeShape(self)

    def run(self):
        while True:
            self.__event_handler()
            self.__update_screen()

    def __event_handler(self):
        """事件处理器"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def __update_screen(self):
        """更新屏幕"""
        self.screen.fill(self.settings.black)
        # 绘制界面网格以及侧边
        self.__draw_grids()
        # 绘制积木
        self.cube.draw()

        pygame.display.update()
        # 帧率
        self.clock.tick(self.settings.fps)

    def __draw_grids(self):
        """绘制界面网格"""
        for row in range(self.settings.grid_num_height):
            # (0, 0), (width, 0)
            pygame.draw.line(self.screen, self.settings.line_color,
                             (0, row * self.settings.grid_width),
                             (self.settings.width, row * self.settings.grid_width))

        for col in range(self.settings.grid_num_width):
            pygame.draw.line(self.screen, self.settings.line_color,
                             (col * self.settings.grid_width, 0),
                             (col * self.settings.grid_width, self.settings.height))

        # 绘制边界
        pygame.draw.line(self.screen, self.settings.line_color,
                         (self.settings.width, 0),
                         (self.settings.width, self.settings.height))


if __name__ == '__main__':
    tetris = Tetris()
    tetris.run()