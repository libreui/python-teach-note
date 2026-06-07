import pygame
import random

# 初始化Pygame
pygame.init()

# 设置画面尺寸
WIDTH = 500
HEIGHT = 500
CELL_SIZE = 10
MARGIN = 10  # 边距
ROWS = (HEIGHT - MARGIN * 2) // CELL_SIZE
COLS = (WIDTH - MARGIN * 2) // CELL_SIZE

# 设置颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 创建窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("迷宫")

# 初始化迷宫格子
# 每个格子用四个布尔值表示：上、右、下、左是否有墙
maze = [[[True, True, True, True] for _ in range(COLS)] for _ in range(ROWS)]


def generate_maze():
    """使用深度优先搜索算法生成迷宫"""
    stack = [(0, 0)]
    visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
    visited[0][0] = True

    while stack:
        current = stack[-1]
        row, col = current

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
    """使用BFS算法找到从入口到出口的路径"""
    start = (0, 0)
    end = (ROWS - 1, COLS - 1)
    
    # 方向：上、右、下、左（对应maze中的索引）
    directions = [(-1, 0, 0, 2), (0, 1, 1, 3), (1, 0, 2, 0), (0, -1, 3, 1)]
    
    visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
    queue = [(start, [start])]
    visited[0][0] = True
    
    while queue:
        (row, col), path = queue.pop(0)
        
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
    """用红色绘制迷宫路径"""
    if not path:
        return
    
    for i in range(len(path) - 1):
        row1, col1 = path[i]
        row2, col2 = path[i + 1]
        
        x1 = MARGIN + col1 * CELL_SIZE + CELL_SIZE // 2
        y1 = MARGIN + row1 * CELL_SIZE + CELL_SIZE // 2
        x2 = MARGIN + col2 * CELL_SIZE + CELL_SIZE // 2
        y2 = MARGIN + row2 * CELL_SIZE + CELL_SIZE // 2
        
        pygame.draw.line(screen, RED, (x1, y1), (x2, y2), 1)
    
    pygame.display.flip()


# 生成并绘制迷宫
generate_maze()
draw_maze()

# 找到并绘制路径
path = find_path()
draw_path(path)

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
