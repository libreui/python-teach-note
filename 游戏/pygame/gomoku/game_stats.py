class GameStats:
    def __init__(self, gomoku):
        # 初始化游戏设置
        self.settings = gomoku.settings
        # 初始化当前玩家为 None
        self.current_play = None
        # 初始化游戏状态为未激活
        self.game_active = False
        self.win = -1

    def reset_stats(self):
        # 初始化当前玩家为 None
        self.current_play = None
        # 初始化游戏状态为未激活
        self.game_active = False
        self.win = -1

    def set_player(self, color):
        """设置当前玩家"""
        self.current_play = color

    def change_player(self):
        """切换玩家"""
        if self.current_play is None:
            self.current_play = self.settings.black_player
        elif self.current_play == self.settings.black_player:
            self.current_play = self.settings.white_player
        else:
            self.current_play = self.settings.black_player

    def __check_win(self, board):
        """
        判断是否胜利, 黑棋胜利0，白棋胜利1， 和棋-1
        :return: 0 or 1 or -1
        """
        # 判定胜利
        for row in board:
            if ''.join(row).find(self.settings.black_player * 5) != -1:
                return 0
            elif ''.join(row).find(self.settings.white_player * 5) != -1:
                return 1
        else:
            return -1

    def check_win_all(self, board):
        """检查全部胜利情况"""
        board_b = [list(i) for i in zip(*board)]
        board_c = [[] for _ in range(self.settings.board_size * 2 - 1)]
        for row in range(self.settings.board_size):
            for col in range(self.settings.board_size):
                board_c[row - col].append(board[row][col])
        board_d = [[] for _ in range(self.settings.board_size * 2 - 1)]
        for row in range(self.settings.board_size):
            for col in range(self.settings.board_size):
                board_d[row + col].append(board[row][col])
        win = [self.__check_win(board),
               self.__check_win(board_b),
               self.__check_win(board_c),
               self.__check_win(board_d)]
        for winner in win:
            if winner == 0:
                self.win = 0
            elif winner == 1:
                self.win = 1
            elif winner == 2:
                self.win = 2
