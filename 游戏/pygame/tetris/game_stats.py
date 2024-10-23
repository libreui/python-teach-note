class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, game):
        """初始化统计信息"""
        self.score = 0
        self.level = 1

        self.game_active = False
        self.cube_active = False
