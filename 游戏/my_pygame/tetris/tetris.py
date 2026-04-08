import sys
import pygame
from pprint import pprint

from settings import Settings
from game_stats import GameStats
from cube_shape import CubeShape


class Tetris:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.stats = GameStats(self)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Tetris")

        self.clock = pygame.time.Clock()
        self.fps = self.settings.fps

        self.cube = None

    def run(self):
        while True:
            self.clock.tick(self.fps)
            self.__check_event()
            self.__pin_cube()
            self.__update_screen()

    def __draw_grids(self):
        """绘制网格"""
        # 绘制竖线
        for i in range(self.settings.grid_num_width):
            pygame.draw.line(self.screen,
                             self.settings.line_color,
                             (i * self.settings.grid_width, 0),
                             (i * self.settings.grid_width, self.settings.height))

        # 绘制横线
        for i in range(self.settings.grid_num_height):
            pygame.draw.line(self.screen,
                             self.settings.line_color,
                             (0, i * self.settings.grid_width),
                             (self.settings.width, i * self.settings.grid_width))

        # 绘制边界
        pygame.draw.line(self.screen,
                         self.settings.line_color,
                         (self.settings.grid_width * self.settings.grid_num_width, 0),
                         (self.settings.grid_width * self.settings.grid_num_width, self.settings.height))

    def __check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.stats.gameover:
                    self.stats.gameover = False
                    self.cube = CubeShape(self)
                    break
                if event.key == pygame.K_UP:
                    self.cube.rotate()
                elif event.key == pygame.K_LEFT:
                    self.cube.left()
                elif event.key == pygame.K_RIGHT:
                    self.cube.right()
                elif event.key == pygame.K_DOWN:
                    self.cube.down()
                elif event.key == pygame.K_SPACE:
                    while self.cube.down():
                        pass
                # self.__remove_full_line()

    def __pin_cube(self):
        if self.stats.gameover is False and self.stats.counter % self.settings.fps == 0:
            if not self.cube.down():
                for cube in self.cube.get_all_gridpos():
                    self.settings.screen_color_matrix[cube[0]][cube[1]] = self.cube.color
                self.cube = CubeShape(self)
                # 判断是否已经到屏幕顶端，需要清楚屏幕方块
                if self.cube.conflict(self.cube.center):
                    self.stats.gameover = True
                    self.cube = None
                    # 积分清零
                    self.stats.clear_score()
                    self.settings.screen_color_matrix = [[None] * self.settings.grid_num_width for _ in
                                                         range(self.settings.grid_num_height)]
            self.__remove_full_line()
        self.stats.counter += 1

    def __draw_matrix(self):
        """绘制堆积方块"""
        for i, row in zip(range(self.settings.grid_num_height), self.settings.screen_color_matrix):
            for j, color in zip(range(self.settings.grid_num_width), row):
                if color is not None:
                    pygame.draw.rect(self.screen, color,
                                     (j * self.settings.grid_width, i * self.settings.grid_width,
                                      self.settings.grid_width, self.settings.grid_width))
                    pygame.draw.rect(self.screen, self.settings.white,
                                     (j * self.settings.grid_width, i * self.settings.grid_width,
                                      self.settings.grid_width, self.settings.grid_width), 2)

    def __remove_full_line(self):
        """消除满行"""
        # 创建一个新的矩阵
        new_matrix = [[None] * self.settings.grid_num_width for _ in range(self.settings.grid_num_height)]
        index = self.settings.grid_num_height - 1
        for i in range(self.settings.grid_num_height - 1, -1, -1):
            # is_full = True
            is_full = all(self.settings.screen_color_matrix[i])
            # for j in range(self.settings.grid_num_width):
            #     if self.settings.screen_color_matrix[i][j] is None:
            #         is_full = False
            #         continue
            if not is_full:
                new_matrix[index] = self.settings.screen_color_matrix[i]
                index -= 1
            else:
                # 满行，积分+1
                self.stats.score += 1

        self.settings.screen_color_matrix = new_matrix

    def __update_screen(self):
        self.screen.fill(self.settings.black)
        self.__draw_grids()
        self.__draw_matrix()
        if self.cube is not None:
            self.cube.draw()
        self.__show_welcome()
        self.__show_score()
        pygame.display.update()

    def __show_score(self):
        """显示分数"""
        self.__show_text('得分：{}'.format(self.stats.score),
                         20, self.settings.width + self.settings.side_width // 2, 100,
                         self.settings.white)

    def __show_welcome(self):
        if self.stats.gameover:
            color = self.settings.white
            self.__show_text('俄罗斯方块',
                             50, self.settings.width / 2, self.settings.height / 2, color)
            self.__show_text('按任意键开始',
                             30, self.settings.width / 2, self.settings.height / 2 + 50, color)

    def __show_text(self, text, size, x, y, color):
        color = self.settings.white if color is None else color
        font_path = "./static/djzt.otf"
        font = pygame.font.Font(font_path, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)


if __name__ == '__main__':
    tetris = Tetris()
    tetris.run()
