# -*- coding: utf-8 -*-
"""
1024 小游戏 (pygame 版)
规则：4x4 网格中滑动方块，相同数字合并翻倍，凑到 1024 即获胜。
操作：方向键(↑↓←→)移动，R 重新开始，Q 退出。
"""

import random
import sys
import pygame

# ---------- 常量 ----------
WIN_WIDTH = 560
WIN_HEIGHT = 680
MARGIN = 30          # 网格外边距
GRID_SIZE = 4
CELL = 110           # 每格边长
GAP = 12             # 格间距
GRID_PIX = GRID_SIZE * CELL + (GRID_SIZE + 1) * GAP   # 网格总边长
TOP_OFFSET = 120     # 顶部信息区高度

BG_COLOR = (250, 248, 239)
PANEL_COLOR = (187, 173, 160)
EMPTY_COLOR = (205, 193, 180)

# 数字 -> 方块颜色
TILE_COLORS = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
}

TEXT_COLOR = (119, 110, 101)
LIGHT_TEXT = (249, 246, 242)
FONT_BIG = "simhei,pingfangsc,arial"
FPS = 60


class Board:
    """游戏逻辑：网格、移动与合并、胜负判断"""

    def __init__(self):
        self.grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
        self.score = 0
        self.won = False
        self.over = False
        self.spawn()
        self.spawn()

    def spawn(self):
        """在随机空位生成 2 或 4（90% 概率 2）"""
        empty = [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE)
                 if self.grid[r][c] == 0]
        if not empty:
            return
        r, c = random.choice(empty)
        self.grid[r][c] = 2 if random.random() < 0.9 else 4

    def _slide(self, line):
        """将一行/列向左滑动并合并，返回 (新行, 得分)"""
        vals = [v for v in line if v != 0]
        new_line, score = [], 0
        i = 0
        while i < len(vals):
            if i + 1 < len(vals) and vals[i] == vals[i + 1]:
                merged = vals[i] * 2
                new_line.append(merged)
                score += merged
                i += 2
            else:
                new_line.append(vals[i])
                i += 1
        new_line += [0] * (GRID_SIZE - len(new_line))
        return new_line, score

    def move(self, direction):
        """direction: 'up' 'down' 'left' 'right'。返回是否发生了移动"""
        moved = False
        total_score = 0

        for i in range(GRID_SIZE):
            if direction == 'left':
                line = [self.grid[i][c] for c in range(GRID_SIZE)]
            elif direction == 'right':
                line = [self.grid[i][c] for c in range(GRID_SIZE - 1, -1, -1)]
            elif direction == 'up':
                line = [self.grid[r][i] for r in range(GRID_SIZE)]
            else:  # down
                line = [self.grid[r][i] for r in range(GRID_SIZE - 1, -1, -1)]

            new_line, score = self._slide(line)

            # 注：line 取数时移动方向的前端已位于 index 0，
            # _coord 写回时也按前端对齐，因此无需 reverse。

            # 写回并检测是否移动
            for k in range(GRID_SIZE):
                r, c = self._coord(i, k, direction)
                if self.grid[r][c] != new_line[k]:
                    moved = True
                self.grid[r][c] = new_line[k]
            total_score += score

        if moved:
            self.score += total_score
            self.spawn()
            self._check_state()
        return moved

    @staticmethod
    def _coord(i, k, direction):
        """将逻辑下标 (i,k) 映射到网格坐标 (r,c)"""
        if direction == 'left':
            return i, k
        if direction == 'right':
            return i, GRID_SIZE - 1 - k
        if direction == 'up':
            return k, i
        return GRID_SIZE - 1 - k, i

    def _check_state(self):
        if any(1024 in row for row in self.grid):
            self.won = True
        elif self._no_moves():
            self.over = True

    def _no_moves(self):
        """网格是否还有任何可移动/可合并的相邻格"""
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                if self.grid[r][c] == 0:
                    return False
                if r + 1 < GRID_SIZE and self.grid[r][c] == self.grid[r + 1][c]:
                    return False
                if c + 1 < GRID_SIZE and self.grid[r][c] == self.grid[r][c + 1]:
                    return False
        return True

    def reset(self):
        self.__init__()


def cell_rect(r, c):
    """网格坐标 -> 屏幕矩形"""
    x = MARGIN + GAP + c * (CELL + GAP)
    y = TOP_OFFSET + GAP + r * (CELL + GAP)
    return pygame.Rect(x, y, CELL, CELL)


def draw_text(surface, text, size, color, center, bold=False):
    font = pygame.font.SysFont(FONT_BIG, size, bold=bold)
    img = font.render(str(text), True, color)
    rect = img.get_rect(center=center)
    surface.blit(img, rect)
    return rect


def draw(screen, board, game_over_msg=""):
    screen.fill(BG_COLOR)

    # 标题与得分
    draw_text(screen, "1024", 54, (119, 110, 101), (MARGIN + 80, 45), bold=True)
    score_box = pygame.Rect(WIN_WIDTH - MARGIN - 130, 22, 130, 52)
    pygame.draw.rect(screen, PANEL_COLOR, score_box, border_radius=8)
    draw_text(screen, "得分", 16, LIGHT_TEXT,
              (score_box.centerx, score_box.y + 15))
    draw_text(screen, board.score, 26, LIGHT_TEXT,
              (score_box.centerx, score_box.y + 37), bold=True)

    # 网格背景
    grid_rect = pygame.Rect(MARGIN, TOP_OFFSET, GRID_PIX, GRID_PIX)
    pygame.draw.rect(screen, PANEL_COLOR, grid_rect, border_radius=10)

    # 方块
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            val = board.grid[r][c]
            rect = cell_rect(r, c)
            pygame.draw.rect(screen, TILE_COLORS.get(val, (60, 58, 50)), rect,
                             border_radius=8)
            if val:
                color = LIGHT_TEXT if val > 4 else TEXT_COLOR
                size = 46 if val < 100 else (36 if val < 1000 else 30)
                draw_text(screen, val, size, color, rect.center, bold=True)

    # 提示
    draw_text(screen, "方向键移动 | R 重开 | Q 退出",
              18, (140, 130, 120), (WIN_WIDTH // 2, WIN_HEIGHT - 25))

    # 结束 / 胜利遮罩
    if board.over or board.won or game_over_msg:
        overlay = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((238, 228, 218, 190))
        screen.blit(overlay, (0, 0))
        if board.won:
            msg = "恭喜通关 1024！"
        elif board.over:
            msg = "游戏结束"
        else:
            msg = game_over_msg
        draw_text(screen, msg, 46, (119, 110, 101),
                  (WIN_WIDTH // 2, WIN_HEIGHT // 2 - 30), bold=True)
        draw_text(screen, "按 R 重新开始", 24, (119, 110, 101),
                  (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 20))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("1024 小游戏")
    clock = pygame.time.Clock()

    board = Board()
    game_over_msg = ""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    board.reset()
                    game_over_msg = ""
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

                key_map = {
                    pygame.K_LEFT: 'left',
                    pygame.K_RIGHT: 'right',
                    pygame.K_UP: 'up',
                    pygame.K_DOWN: 'down',
                }
                if event.key in key_map:
                    if not board.won and not board.over:
                        board.move(key_map[event.key])

        draw(screen, board, game_over_msg)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
