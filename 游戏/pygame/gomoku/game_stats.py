class GameStats:
    def __init__(self, gomoku):
        # 初始化游戏设置
        self.settings = gomoku.settings
        # 初始化当前玩家为 None
        self.current_play = None
        # 初始化游戏状态为未激活
        self.game_active = False

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
