import pygame
import sys
from settings import Settings
from board import Board
from game_stats import GameStats
from button import Button
from gomoku_ai import GomokuAI


class Gomoku:
    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_icon(pygame.image.load(self.settings.icon_img))
        pygame.display.set_caption(self.settings.title)

        self.clock = pygame.time.Clock()
        self.stats = GameStats(self)
        self.board = Board(self)
        self.bg = pygame.image.load(self.settings.bg_img)

        # 实例化ai
        self.ai = GomokuAI(self.board.board)

        # 创建按钮
        self.__create_button()

    def start(self):
        """游戏开始"""
        while True:
            if not self.stats.ai_running:
                self.__check_events()
            else:
                self.__ai_set_chess()
            self.__update_screen()

    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.__check_click(event)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and self.stats.win > -1:
                    self.stats.reset_stats()
                    self.board.reset()
                # 这里原本是按任意键开始游戏
                # self.stats.game_active = True

    def __update_screen(self):
        """更新屏幕"""
        self.clock.tick(self.settings.fps)
        self.screen.blit(self.bg, (0, 0))
        self.__draw_grid()
        if self.stats.game_active:
            self.board.draw()
        else:
            self.__draw_button()

        self.__show_win_text()

        pygame.display.flip()

    def __draw_grid(self):
        """绘制棋盘"""
        for col in range(self.settings.board_size):
            pygame.draw.line(self.screen, self.settings.line_color,
                             (col * self.settings.cell_size + self.settings.board_side, self.settings.board_side),
                             (col * self.settings.cell_size + self.settings.board_side,
                              self.settings.height - self.settings.board_side), 1)
            pygame.draw.line(self.screen, self.settings.line_shadow_color,
                             (col * self.settings.cell_size + (self.settings.board_side + 1),
                              (self.settings.board_side + 1)),
                             (col * self.settings.cell_size + (self.settings.board_side + 1),
                              self.settings.height - (self.settings.board_side + 1)), 1)

        for row in range(self.settings.board_size):
            pygame.draw.line(self.screen, self.settings.line_color,
                             (self.settings.board_side, row * self.settings.cell_size + self.settings.board_side),
                             (self.settings.width - self.settings.board_side,
                              row * self.settings.cell_size + self.settings.board_side), 1)
            pygame.draw.line(self.screen, self.settings.line_shadow_color,
                             ((self.settings.board_side + 1), row * self.settings.cell_size +
                              (self.settings.board_side + 1)),
                             (self.settings.width - (self.settings.board_side + 1),
                              row * self.settings.cell_size + (self.settings.board_side + 1)), 1)

        self.__draw_dot(7, 7)
        self.__draw_dot(3, 3)
        self.__draw_dot(3, 11)
        self.__draw_dot(11, 3)
        self.__draw_dot(11, 11)

    def __draw_dot(self, row, col):
        """绘制棋盘原点"""
        pygame.draw.circle(self.screen, self.settings.dot_color,
                           (col * self.settings.cell_size + self.settings.board_side,
                            row * self.settings.cell_size + self.settings.board_side), 5)

    def __create_button(self):
        """创建按钮"""
        self.ai_button = Button(self, self.settings.button_img_ai)
        self.two_button = Button(self, self.settings.button_img_two)
        self.ai_button.rect.centerx = self.screen_rect.centerx - 100
        self.two_button.rect.centerx = self.screen_rect.centerx + 100

    def __draw_button(self):
        """绘制按钮"""
        self.ai_button.draw()
        self.two_button.draw()

    def __button_click(self, event):
        """按钮点击事件"""

        self.stats.change_player()

        mouse_pos = event.pos
        button_ai_clicked = self.ai_button.rect.collidepoint(mouse_pos)
        button_two_clicked = self.two_button.rect.collidepoint(mouse_pos)

        if button_ai_clicked and not self.stats.game_active:
            # 开始人机对战
            self.stats.game_active = True
            self.stats.mode = self.settings.mode_single
        if button_two_clicked and not self.stats.game_active:
            self.stats.game_active = True
            self.stats.mode = self.settings.mode_two

    def __set_chess(self, event):
        if self.stats.win >= 0:
            return
        x, y = event.pos
        col = round((x - self.settings.board_side) / self.settings.cell_size)
        row = round((y - self.settings.board_side) / self.settings.cell_size)

        # 落子
        ret = self.board.make_move(row, col, self.stats.current_player)

        if ret:
            if self.stats.mode == self.settings.mode_single:
                self.stats.ai_running = True
            self.stats.change_player()

    def __ai_set_chess(self):
        """AI落子"""
        if self.stats.win >= 0:
            self.stats.ai_running = False
            return
        # 计算AI落子点
        ai_pos_row, ai_pos_col = self.ai.get_best_move()
        ret = self.board.make_move(ai_pos_row, ai_pos_col, self.stats.current_player)
        if ret:
            self.stats.change_player()
            self.stats.ai_running = False

    def __check_click(self, event):
        """打印鼠标位置, 并绘制棋子"""
        if not self.stats.game_active:
            self.__button_click(event)
        elif self.stats.ai_running:  # ai运行时候不能点击
            return
        else:
            self.__set_chess(event)

            # 检查输赢
            self.stats.check_win_all(self.board.board)

    def __show_win_text(self):
        """显示输赢信息"""
        if self.stats.win < 0:
            return
        win_txt = ''
        if self.stats.win == 0:
            win_txt = '黑棋胜利'
        elif self.stats.win == 1:
            win_txt = '白棋胜利'
        elif self.stats.win == 2:
            win_txt = '平局'
        font = pygame.font.Font(self.settings.font, 36)
        font_image = font.render(win_txt, True, (0, 0, 0))
        font_rect = font_image.get_rect()
        font_rect.midtop = self.screen_rect.midtop
        self.screen.blit(font_image, font_rect)

        self.__show_esc_text()

    def __show_esc_text(self):
        font = pygame.font.Font(self.settings.font, 12)
        font_image = font.render('按ESC键重新开始', True, (0, 0, 0))
        font_rect = font_image.get_rect()
        font_rect.midtop = (self.screen_rect.midtop[0], self.screen_rect.midtop[1] + 40)
        self.screen.blit(font_image, font_rect)


if __name__ == '__main__':
    # 创建一个 Gomoku 类的实例
    gomoku = Gomoku()
    # 调用 start 方法开始游戏
    gomoku.start()
