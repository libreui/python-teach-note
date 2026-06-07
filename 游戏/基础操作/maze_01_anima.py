import pygame
import random

# 初始化pygame
pygame.init()

# 设置常量
WIDTH = 500  # 窗口宽度
HEIGHT = 500  # 窗口高度
CELL_SIZE = 10  # 格子大小
MARGIN = 10  # 边距

# 计算迷宫格子数量
ROWS = (HEIGHT - MARGIN * 2) // CELL_SIZE
COLS = (WIDTH - MARGIN * 2) // CELL_SIZE

# 设置颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)  # 当前正在处理的格子颜色
GREEN = (0, 255, 0)  # 已访问格子颜色

# 动画速度（毫秒）
ANIMATION_DELAY = 10

# 创建屏幕
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("迷宫生成与寻路")

# 初始化迷宫：每个格子有四堵墙 [上, 右, 下, 左]
maze = [[[True, True, True, True] for _ in range(COLS)] for _ in range(ROWS)]

def generate_maze():
    """使用深度优先搜索算法生成迷宫（带动画）"""
    stack = [(0, 0)]
    visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
    visited[0][0] = True

    # 初始绘制完整的网格
    draw_full_grid()

    while stack:
        # 处理事件，防止程序卡死
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        current = stack[-1]
        row, col = current

        # 绘制当前路径（蓝色高亮）
        for r, c in stack:
            x = MARGIN + c * CELL_SIZE + 1
            y = MARGIN + r * CELL_SIZE + 1
            pygame.draw.rect(screen, BLUE, (x, y, CELL_SIZE - 2, CELL_SIZE - 2))

        # 绘制已访问的格子（绿色）
        for r in range(ROWS):
            for c in range(COLS):
                if visited[r][c] and (r, c) not in stack:
                    x = MARGIN + c * CELL_SIZE + 1
                    y = MARGIN + r * CELL_SIZE + 1
                    pygame.draw.rect(screen, GREEN, (x, y, CELL_SIZE - 2, CELL_SIZE - 2))

        pygame.display.flip()
        pygame.time.delay(ANIMATION_DELAY)

        # 获取未访问的邻居
        neighbors = []
        # 上
        if row > 0 and not visited[row - 1][col]:
            neighbors.append(('up', row - 1, col))
        # 右
        if col < COLS - 1 and not visited[row][col + 1]:
            neighbors.append(('right', row, col + 1))
        # 下
        if row < ROWS - 1 and not visited[row + 1][col]:
            neighbors.append(('down', row + 1, col))
        # 左
        if col > 0 and not visited[row][col - 1]:
            neighbors.append(('left', row, col - 1))

        if neighbors:
            # 随机选择一个邻居
            direction, next_row, next_col = random.choice(neighbors)

            # 移除墙壁
            if direction == 'up':
                maze[row][col][0] = False
                maze[next_row][next_col][2] = False
            elif direction == 'right':
                maze[row][col][1] = False
                maze[next_row][next_col][3] = False
            elif direction == 'down':
                maze[row][col][2] = False
                maze[next_row][next_col][0] = False
            elif direction == 'left':
                maze[row][col][3] = False
                maze[next_row][next_col][1] = False

            visited[next_row][next_col] = True
            stack.append((next_row, next_col))
        else:
            stack.pop()

        # 重绘网格（移除墙壁后的状态）
        draw_full_grid()


def draw_full_grid():
    """绘制完整的网格（用于动画过程）"""
    screen.fill(WHITE)

    for row in range(ROWS):
        for col in range(COLS):
            x = MARGIN + col * CELL_SIZE
            y = MARGIN + row * CELL_SIZE

            # 绘制墙壁（实线）
            if maze[row][col][0]:
                pygame.draw.line(screen, BLACK, (x, y), (x + CELL_SIZE, y), 1)
            if maze[row][col][1]:
                pygame.draw.line(screen, BLACK, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE), 1)
            if maze[row][col][2]:
                pygame.draw.line(screen, BLACK, (x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE), 1)
            if maze[row][col][3]:
                pygame.draw.line(screen, BLACK, (x, y), (x, y + CELL_SIZE), 1)


def draw_maze():
    """绘制迷宫"""
    screen.fill(WHITE)

    for row in range(ROWS):
        for col in range(COLS):
            x = MARGIN + col * CELL_SIZE
            y = MARGIN + row * CELL_SIZE

            # 绘制墙壁（实线）
            # 上墙
            if maze[row][col][0]:
                pygame.draw.line(screen, BLACK, (x, y), (x + CELL_SIZE, y), 1)
            # 右墙
            if maze[row][col][1]:
                pygame.draw.line(screen, BLACK, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE), 1)
            # 下墙
            if maze[row][col][2]:
                pygame.draw.line(screen, BLACK, (x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE), 1)
            # 左墙
            if maze[row][col][3]:
                pygame.draw.line(screen, BLACK, (x, y), (x, y + CELL_SIZE), 1)

    # 绘制入口（左上角）
    pygame.draw.rect(screen, WHITE, (MARGIN, MARGIN, CELL_SIZE, CELL_SIZE))

    # 绘制出口（右下角）
    exit_x = MARGIN + (COLS - 1) * CELL_SIZE
    exit_y = MARGIN + (ROWS - 1) * CELL_SIZE
    pygame.draw.rect(screen, WHITE, (exit_x, exit_y, CELL_SIZE, CELL_SIZE))
    # 移除出口的墙（移除下墙，让玩家可以从底部出去）
    maze[ROWS - 1][COLS - 1][2] = False  # 移除下墙
    # 绘制出口通道
    pygame.draw.rect(screen, WHITE, (exit_x, exit_y + CELL_SIZE, CELL_SIZE, MARGIN))

    pygame.display.flip()


def find_path():
    """使用BFS算法找到从入口到出口的路径（带动画）"""
    start = (0, 0)
    end = (ROWS - 1, COLS - 1)

    # 方向：上、右、下、左（对应maze中的索引）
    directions = [(-1, 0, 0, 2), (0, 1, 1, 3), (1, 0, 2, 0), (0, -1, 3, 1)]

    visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
    queue = [(start, [start])]
    visited[0][0] = True

    while queue:
        # 处理事件，防止程序卡死
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        (row, col), path = queue.pop(0)

        # 绘制当前访问的格子（黄色）
        x = MARGIN + col * CELL_SIZE + 1
        y = MARGIN + row * CELL_SIZE + 1
        pygame.draw.rect(screen, (255, 255, 0), (x, y, CELL_SIZE - 2, CELL_SIZE - 2))
        pygame.display.flip()
        pygame.time.delay(ANIMATION_DELAY)

        if (row, col) == end:
            return path

        for dr, dc, wall_idx, neighbor_wall_idx in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < ROWS and 0 <= new_col < COLS:
                if not visited[new_row][new_col] and not maze[row][col][wall_idx]:
                    visited[new_row][new_col] = True
                    queue.append(((new_row, new_col), path + [(new_row, new_col)]))

    return []


def draw_path(path):
    """用红色绘制迷宫路径（带动画）"""
    if not path:
        return

    # 先重绘干净的迷宫
    draw_maze()

    for i in range(len(path) - 1):
        # 处理事件，防止程序卡死
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        row1, col1 = path[i]
        row2, col2 = path[i + 1]

        x1 = MARGIN + col1 * CELL_SIZE + CELL_SIZE // 2
        y1 = MARGIN + row1 * CELL_SIZE + CELL_SIZE // 2
        x2 = MARGIN + col2 * CELL_SIZE + CELL_SIZE // 2
        y2 = MARGIN + row2 * CELL_SIZE + CELL_SIZE // 2

        pygame.draw.line(screen, RED, (x1, y1), (x2, y2), 2)
        pygame.display.flip()
        pygame.time.delay(ANIMATION_DELAY)

    # 绘制起点和终点标记
    start_x = MARGIN + path[0][1] * CELL_SIZE + CELL_SIZE // 2
    start_y = MARGIN + path[0][0] * CELL_SIZE + CELL_SIZE // 2
    pygame.draw.circle(screen, (0, 255, 0), (start_x, start_y), CELL_SIZE // 3)

    end_x = MARGIN + path[-1][1] * CELL_SIZE + CELL_SIZE // 2
    end_y = MARGIN + path[-1][0] * CELL_SIZE + CELL_SIZE // 2
    pygame.draw.circle(screen, (255, 0, 0), (end_x, end_y), CELL_SIZE // 3)

    pygame.display.flip()


# 生成迷宫（带动画）
generate_maze()

# 绘制最终迷宫
pygame.time.delay(500)  # 暂停0.5秒
draw_maze()

# 找到路径（带动画）
path = find_path()

# 绘制路径（带动画）
draw_path(path)

# 保持窗口显示
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()