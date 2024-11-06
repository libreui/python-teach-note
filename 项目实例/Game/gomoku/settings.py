class Settings:
    def __init__(self):

        self.font = './static/djzt.otf'

        self.mode_single = 1
        self.mode_two = 2

        self.title = '五子棋 by Libre'
        self.icon_img = './static/gomoku_icon.png'
        self.button_img_ai = './static/ai.png'
        self.button_img_two = './static/tow.png'
        self.fps = 30

        self.dot_color = (70, 70, 70)
        self.bg_color = (255, 0, 0)
        self.line_color = (0, 0, 0)
        self.line_shadow_color = (230, 230, 230)

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.black_player = 'x'
        self.white_player = 'o'

        self.width = 750
        self.height = 750

        self.board_size = 15
        self.cell_size = 50
        self.board_side = self.cell_size // 2
        self.chess_size = 20

        self.bg_img = "./static/gomoku_bg.jpg"
