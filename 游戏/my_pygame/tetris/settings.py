class Settings:
    def __init__(self):
        self.grid_width = 20
        self.grid_num_width = 15
        self.grid_num_height = 25
        self.width, self.height = self.grid_width * self.grid_num_width, self.grid_width * self.grid_num_height
        self.side_width = 200
        self.screen_width = self.width + self.side_width

        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.line_color = (51, 51, 51)

        self.screen_color_matrix = [[None] * self.grid_num_width for _ in range(self.grid_num_height)]

        self.fps = 30

        # 积木颜色
        self.cube_color = [
            (0xcc, 0x99, 0x99), (0xff, 0xff, 0x99), (0x66, 0x66, 0x99),
            (0x99, 0x00, 0x66), (0xff, 0xcc, 0x00), (0xcc, 0x00, 0x33),
            (0xff, 0x00, 0x33), (0x00, 0x66, 0x99), (0xff, 0xff, 0x33),
            (0x99, 0x00, 0x33), (0xcc, 0xff, 0x66), (0xff, 0x99, 0x00)
        ]

