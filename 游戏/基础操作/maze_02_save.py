import pygame
import random
import os

# 初始化Pygame
pygame.init()

# 设置常量
WIDTH = 500
HEIGHT = 500
CELL_SIZE = 10
MARGIN = 10
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
maze = [[[True, True, True, True] for _ in range(COLS)] for _ in range(ROWS)]


def generate_maze():
    """使用深度优先搜索算法生成迷宫"""
    stack = [(0, 0)]
    visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
    visited[0][0] = True

    while stack:
        current = stack[-1]
        row, col = current

        neighbors = []
        if row > 0 and not visited[row - 1][col]:
            neighbors.append(('up', row - 1, col))
        if col < COLS - 1 and not visited[row][col + 1]:
            neighbors.append(('right', row, col + 1))
        if row < ROWS - 1 and not visited[row + 1][col]:
            neighbors.append(('down', row + 1, col))
        if col > 0 and not visited[row][col - 1]:
            neighbors.append(('left', row, col - 1))

        if neighbors:
            direction, next_row, next_col = random.choice(neighbors)

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

            # 线粗为1
            if maze[row][col][0]:
                pygame.draw.line(screen, BLACK, (x, y), (x + CELL_SIZE, y), 1)
            if maze[row][col][1]:
                pygame.draw.line(screen, BLACK, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE), 1)
            if maze[row][col][2]:
                pygame.draw.line(screen, BLACK, (x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE), 1)
            if maze[row][col][3]:
                pygame.draw.line(screen, BLACK, (x, y), (x, y + CELL_SIZE), 1)

    # 绘制入口（左上角）
    pygame.draw.rect(screen, WHITE, (MARGIN, MARGIN, CELL_SIZE, CELL_SIZE))

    # 绘制出口（右下角）
    exit_x = MARGIN + (COLS - 1) * CELL_SIZE
    exit_y = MARGIN + (ROWS - 1) * CELL_SIZE
    pygame.draw.rect(screen, WHITE, (exit_x, exit_y, CELL_SIZE, CELL_SIZE))
    maze[ROWS - 1][COLS - 1][2] = False
    pygame.draw.rect(screen, WHITE, (exit_x, exit_y + CELL_SIZE, CELL_SIZE, MARGIN))

    pygame.display.flip()


def find_path():
    """使用BFS算法找到从入口到出口的路径"""
    start = (0, 0)
    end = (ROWS - 1, COLS - 1)
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


def save_maze_image(include_path=True):
    """保存迷宫为图片，默认包含路径，保存到桌面"""
    draw_maze()
    if include_path:
        path = find_path()
        draw_path(path)
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    filename = "maze_with_path.png" if include_path else "maze.png"
    save_path = os.path.join(desktop_path, filename)
    pygame.image.save(screen, save_path)
    print(f"迷宫图片已保存到: {save_path}")


# 生成迷宫
generate_maze()

# 询问用户是否包含路径
print("是否在图片中包含寻路结果？(y/n，默认y):")
include_path_input = input().strip().lower()
include_path = include_path_input in ('', 'y', 'yes')

# 绘制迷宫
draw_maze()
if include_path:
    path = find_path()
    draw_path(path)

# 保存图片
save_maze_image(include_path)

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
