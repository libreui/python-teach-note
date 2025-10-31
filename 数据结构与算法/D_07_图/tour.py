#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
骑士周游问题可视化
使用pygame库展示骑士周游算法的执行过程
"""

import pygame
import sys
import time
from dfs_knight_graph import knight_graph, knight_tour, order_by_avail, post_to_node_id
from graph import Graph
from vertex import Vertex

# 初始化pygame
try:
    pygame.init()
except:
    print("无法初始化pygame库，请确保已安装pygame: pip install pygame")
    sys.exit(1)

# 可视化参数设置
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
BOARD_SIZE = 8  # 棋盘大小8x8
SQUARE_SIZE = SCREEN_WIDTH // BOARD_SIZE
ANIMATION_SPEED = 0.1  # 动画速度（秒）

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)

# 创建屏幕
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("骑士周游问题可视化")
clock = pygame.time.Clock()

# 字体设置
try:
    font = pygame.font.Font(None, 36)
except:
    font = pygame.font.SysFont("Arial", 36)

# 定义全局变量以实现可视化追踪
global_path = []  # 存储整个路径
current_step = 0  # 当前步骤
running = True  # 程序运行状态
paused = False  # 暂停状态
found_solution = False  # 是否找到解决方案
tour_running = True  # 控制周游算法是否继续运行

# 线程安全的锁
import threading
path_lock = threading.Lock()

# 绘制函数（必须在主线程中执行）
def draw_board():
    """绘制棋盘"""
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            # 棋盘交替颜色
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, 
                             (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            # 绘制网格线
            pygame.draw.rect(screen, GRAY, 
                             (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)

            # 显示坐标标签
            if row == 0:
                label = font.render(str(col), True, BLACK if color == WHITE else WHITE)
                screen.blit(label, (col * SQUARE_SIZE + 5, 5))
            if col == 0:
                label = font.render(str(row), True, BLACK if color == WHITE else WHITE)
                screen.blit(label, (5, row * SQUARE_SIZE + 5))

def draw_knight(row, col):
    """绘制骑士棋子"""
    # 计算圆心位置
    center_x = col * SQUARE_SIZE + SQUARE_SIZE // 2
    center_y = row * SQUARE_SIZE + SQUARE_SIZE // 2
    radius = SQUARE_SIZE // 3
    
    # 绘制骑士棋子（简化为圆形）
    pygame.draw.circle(screen, RED, (center_x, center_y), radius)
    pygame.draw.circle(screen, BLACK, (center_x, center_y), radius, 2)  # 边框

def draw_path(path):
    """绘制已走过的路径"""
    if len(path) < 2:
        return
    
    # 绘制路径线条
    for i in range(len(path) - 1):
        # 从节点ID获取行列坐标
        row1, col1 = id_to_pos(path[i].get_id())
        row2, col2 = id_to_pos(path[i+1].get_id())
        
        # 计算起点和终点坐标
        start_x = col1 * SQUARE_SIZE + SQUARE_SIZE // 2
        start_y = row1 * SQUARE_SIZE + SQUARE_SIZE // 2
        end_x = col2 * SQUARE_SIZE + SQUARE_SIZE // 2
        end_y = row2 * SQUARE_SIZE + SQUARE_SIZE // 2
        
        # 绘制路径线段
        pygame.draw.line(screen, BLUE, (start_x, start_y), (end_x, end_y), 3)
        
    # 绘制路径上的步骤数字
    for i, vertex in enumerate(path):
        row, col = id_to_pos(vertex.get_id())
        x = col * SQUARE_SIZE + SQUARE_SIZE // 2 - 10
        y = row * SQUARE_SIZE + SQUARE_SIZE // 2 - 10
        
        # 绘制数字背景
        pygame.draw.circle(screen, YELLOW, 
                          (col * SQUARE_SIZE + SQUARE_SIZE // 2, 
                           row * SQUARE_SIZE + SQUARE_SIZE // 2), 20)
        
        # 绘制数字
        label = font.render(str(i), True, BLACK)
        screen.blit(label, (x, y))

def id_to_pos(node_id):
    """将节点ID转换为棋盘上的行列坐标"""
    row = node_id // BOARD_SIZE
    col = node_id % BOARD_SIZE
    return row, col

def pos_to_id(row, col):
    """将棋盘上的行列坐标转换为节点ID"""
    return row * BOARD_SIZE + col

# 修改 knight_tour 函数以支持可视化
def knight_tour_visual(n, path, u, limit):
    """支持可视化的骑士周游算法"""
    global global_path, current_step, found_solution, paused, tour_running
    
    u.set_color('gray')
    path.append(u)
    
    with path_lock:
        global_path.append(u)
    
    # 等待直到解除暂停或程序结束
    while paused and tour_running:
        time.sleep(0.1)
    
    if not tour_running:
        return False
    
    with path_lock:
        current_step += 1
    
    if n < limit:
        nbr_list = order_by_avail(u)
        i = 0
        done = False
        while i < len(nbr_list) and not done and tour_running:
            # 检查暂停状态
            while paused and tour_running:
                time.sleep(0.1)
            
            if not tour_running:
                return False
            
            if nbr_list[i].get_color() == 'white':
                done = knight_tour_visual(n + 1, path, nbr_list[i], limit)
            i += 1
        
        if not done and tour_running:
            # 回溯
            with path_lock:
                current_step -= 1
                backtrack_vertex = path.pop()
                backtrack_vertex.set_color('white')
                
                # 如果在路径中，则从global_path中移除
                if backtrack_vertex in global_path:
                    global_path.remove(backtrack_vertex)
    else:
        done = True
        with path_lock:
            found_solution = True
        
    return done

def main():
    """主函数"""
    global running, paused, current_step, global_path, found_solution, tour_running
    
    # 创建骑士周游图
    print("正在创建骑士周游图...")
    kt_graph = knight_graph(BOARD_SIZE)
    print(f"图创建完成: {kt_graph.num_vertices}个顶点, {kt_graph.num_edges}条边")
    
    # 设置起始顶点 (0,0) 对应ID 0
    start_vertex = kt_graph.get_vertex(7)
    
    # 创建线程来运行骑士周游算法
    tour_thread = threading.Thread(target=knight_tour_visual, 
                                   args=(0, [], start_vertex, BOARD_SIZE*BOARD_SIZE-1))
    tour_thread.daemon = True  # 设为守护线程，主线程结束时自动终止
    tour_thread.start()
    
    # 主事件循环
    while running:
        # 处理事件（只在主线程中执行）
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                tour_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                    print("暂停" if paused else "继续")
                elif event.key == pygame.K_r:
                    # 重置程序
                    print("重置程序...")
                    tour_running = False  # 停止当前线程的执行
                    time.sleep(0.1)  # 等待线程结束
                    
                    with path_lock:
                        current_step = 0
                        global_path = []
                        found_solution = False
                        paused = False
                        tour_running = True
                    
                    # 重新创建图和顶点
                    kt_graph = knight_graph(BOARD_SIZE)
                    start_vertex = kt_graph.get_vertex(0)
                    
                    # 重启骑士周游线程
                    tour_thread = threading.Thread(target=knight_tour_visual, 
                                                   args=(0, [], start_vertex, BOARD_SIZE*BOARD_SIZE-1))
                    tour_thread.daemon = True
                    tour_thread.start()
                elif event.key == pygame.K_q:
                    running = False
                    tour_running = False
        
        # 绘制当前状态（只在主线程中执行）
        with path_lock:
            draw_board()
            draw_path(global_path[:current_step])
            if current_step > 0:
                current_row, current_col = id_to_pos(global_path[current_step-1].get_id())
                draw_knight(current_row, current_col)
            
            # 显示当前步骤和状态信息
            status_text = f"步骤: {current_step}/{BOARD_SIZE*BOARD_SIZE-1}"
            if found_solution:
                status_text += " - 找到解决方案!"
            elif paused:
                status_text += " - 已暂停"
            
            status_label = font.render(status_text, True, BLACK)
            screen.blit(status_label, (10, SCREEN_HEIGHT - 40))
            
            # 显示暂停信息
            if paused:
                pause_label = font.render("已暂停 - 按空格键继续", True, BLACK)
                screen.blit(pause_label, (SCREEN_WIDTH // 3, SCREEN_HEIGHT - 40))
        
        pygame.display.flip()
        clock.tick(60)  # 限制帧率
    
    pygame.quit()
    sys.exit(0)

if __name__ == "__main__":
    main()