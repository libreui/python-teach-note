import pygame

from settings import Settings
from cube_shape import CubeShape
from game_stats import GameStats


class Tetris:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.stats = GameStats(self)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.height))

        self.clock = pygame.time.Clock()
        self.cube = CubeShape(self)
        self.fps = self.settings.fps

    def run(self):
        while True:
            self.clock.tick(self.fps)
            self.__event_handler()
            self.__pin_cube()
            self.__update_screen()

    def __pin_cube(self):
        """固定积木"""
        if self.stats.counter % self.fps == 0:
            if not self.cube.down():
                # 把原来的积木绘制在屏幕上
                for cube in self.cube.get_all_gridpos():
                    self.settings.screen_color_matrix[cube[0]][cube[1]] = self.cube.color

                # 创建新的积木
                self.cube = None
                self.cube = CubeShape(self)


        self.stats.counter += 1

    def __draw_matrix(self):
        """绘制矩阵"""
        for i, row in zip(range(0, self.settings.grid_num_height), self.settings.screen_color_matrix):
            for j, color in zip(range(0, self.settings.grid_num_width), row):
                if color is not None:
                    pygame.draw.rect(self.screen, color, (j * self.settings.grid_width,
                                                          i * self.settings.grid_width,
                                                          self.settings.grid_width,
                                                          self.settings.grid_width))



    def __event_handler(self):
        """事件处理器"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.cube.left()
                elif event.key == pygame.K_RIGHT:
                    self.cube.right()
                elif event.key == pygame.K_DOWN:
                    self.cube.down()
                elif event.key == pygame.K_UP:
                    self.cube.rotate()

    def __update_screen(self):
        """更新屏幕"""
        self.screen.fill(self.settings.black)
        # 绘制界面网格以及侧边
        self.__draw_grids()
        self.__draw_matrix()
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