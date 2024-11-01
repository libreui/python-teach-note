import pygame


class Board:
    def __init__(self, gomoku):
        self.screen = gomoku.screen
        self.settings = gomoku.settings
        self.stats = gomoku.stats
        self.board = [[''] * self.settings.board_size for _ in range(self.settings.board_size)]

    def reset(self):
        self.board = [[''] * self.settings.board_size for _ in range(self.settings.board_size)]

    def make_move(self, row, col, play):
        if self.board[row][col] == "":
            self.board[row][col] = play
        else:
            print('invalid move')

    def draw(self):
        for row in range(self.settings.board_size):
            for col in range(self.settings.board_size):
                if self.board[row][col] == '':
                    continue
                elif self.board[row][col] == self.settings.black_player:
                    self.__draw_black(row, col)
                elif self.board[row][col] == self.settings.white_player:
                    self.__draw_white(row, col)

    def __draw_black(self, row, col):
        pygame.draw.circle(self.screen, self.settings.black,
                           (col * self.settings.cell_size + self.settings.board_side,
                            row * self.settings.cell_size + self.settings.board_side), self.settings.chess_size)

    def __draw_white(self, row, col):
        pygame.draw.circle(self.screen, self.settings.white,
                           (col * self.settings.cell_size + self.settings.board_side,
                            row * self.settings.cell_size + self.settings.board_side), self.settings.chess_size)


