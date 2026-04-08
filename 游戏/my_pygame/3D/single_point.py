import math
import pygame
import sys

# 初始化pygame
pygame.init()

# 设置窗口尺寸和标题
WIDTH, HEIGHT = 800, 600
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
SCALE = 50  # 缩放因子
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D房间透视 - 移动眼睛观察")

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
LIGHT_GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# 字体设置
pygame.font.init()
font_small = pygame.font.SysFont("simHei", 24)

def perspective_projection(point_3d, camera_position, focal_length):
    """将三维点投影到二维平面上"""
    x, y, z = point_3d
    cam_x, cam_y, cam_z = camera_position

    # 计算点到相机的距离
    distance = z - cam_z

    # 避免除以零
    if distance <= 0:
        return None

    # 计算投影点的坐标
    x_proj = focal_length * (x - cam_x) / distance + cam_x
    y_proj = focal_length * (y - cam_y) / distance + cam_y

    return x_proj, y_proj

def to_screen_coords(proj_point):
    """将投影坐标转换为屏幕坐标"""
    if proj_point is None:
        return None
    x, y = proj_point
    # 应用缩放并转换到屏幕坐标系
    screen_x = CENTER_X + x * SCALE
    screen_y = CENTER_Y - y * SCALE  # 反转y轴
    return (screen_x, screen_y)

def create_rectangle(width, height, depth):
    """创建一个矩形的8个顶点和边"""
    half_w = width / 2
    half_h = height / 2
    half_d = depth / 2
    
    # 矩形的8个顶点
    vertices = [
        (-half_w, -half_h, -half_d),  # 0: 左下后
        (half_w, -half_h, -half_d),   # 1: 右下后
        (half_w, half_h, -half_d),    # 2: 右上后
        (-half_w, half_h, -half_d),   # 3: 左上后
        (-half_w, -half_h, half_d),   # 4: 左下前
        (half_w, -half_h, half_d),    # 5: 右下前
        (half_w, half_h, half_d),     # 6: 右上前
        (-half_w, half_h, half_d)     # 7: 左上前
    ]
    
    # 矩形的边索引
    edges = [
        # 后边
        (0, 1), (1, 2), (2, 3), (3, 0),
        # 前边
        (4, 5), (5, 6), (6, 7), (7, 4),
        # 连接前后的边
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]
    
    return vertices, edges

def draw_rectangle(vertices, edges, position, rotation, camera_pos, focal_length, color=WHITE):
    """绘制矩形，包括透视投影"""
    # 计算变换后的顶点
    transformed_vertices = []
    for vertex in vertices:
        # 旋转顶点
        rotated = vertex  # 简化：不旋转物体
        # 平移顶点
        translated = (rotated[0] + position[0], 
                     rotated[1] + position[1], 
                     rotated[2] + position[2])
        # 投影顶点
        projected = perspective_projection(translated, camera_pos, focal_length)
        # 转换为屏幕坐标
        screen_coords = to_screen_coords(projected)
        transformed_vertices.append(screen_coords)
    
    # 绘制边
    for edge in edges:
        i, j = edge
        if transformed_vertices[i] and transformed_vertices[j]:
            pygame.draw.line(screen, color, 
                           transformed_vertices[i], 
                           transformed_vertices[j], 2)

def create_room(length, width, height):
    """创建房间的各个面（墙壁、地板、天花板）"""
    # 房间的边
    half_l = length / 2
    half_w = width / 2
    half_h = height / 2
    
    # 创建地板
    floor_vertices, _ = create_rectangle(length, 0.1, width)
    floor_position = (0, -half_h, 0)  # 地板位于底部
    
    # 创建墙壁
    # 前墙
    front_wall_vertices, _ = create_rectangle(length, height, 0.1)
    front_wall_position = (0, 0, half_w)  # 前墙在z轴正方向
    
    # 后墙
    back_wall_vertices, _ = create_rectangle(length, height, 0.1)
    back_wall_position = (0, 0, -half_w)  # 后墙在z轴负方向
    
    # 左墙
    left_wall_vertices, _ = create_rectangle(0.1, height, width)
    left_wall_position = (-half_l, 0, 0)  # 左墙在x轴负方向
    
    # 右墙
    right_wall_vertices, _ = create_rectangle(0.1, height, width)
    right_wall_position = (half_l, 0, 0)  # 右墙在x轴正方向
    
    # 创建天花板
    ceiling_vertices, _ = create_rectangle(length, 0.1, width)
    ceiling_position = (0, half_h, 0)  # 天花板位于顶部
    
    # 返回所有墙的顶点、边和位置
    room_parts = [
        (floor_vertices, floor_position, GRAY),
        (front_wall_vertices, front_wall_position, LIGHT_GRAY),
        (back_wall_vertices, back_wall_position, LIGHT_GRAY),
        (left_wall_vertices, left_wall_position, LIGHT_GRAY),
        (right_wall_vertices, right_wall_position, LIGHT_GRAY),
        (ceiling_vertices, ceiling_position, GRAY)
    ]
    
    return room_parts

def main():
    # 创建房间
    room_parts = create_room(10, 10, 5)  # 10x10x5的房间
    
    # 创建房间内的物体
    # 桌子
    table_vertices, table_edges = create_rectangle(2, 1, 1)
    table_position = (-2, -2, 2)  # 位于房间左下角
    
    # 椅子
    chair_vertices, chair_edges = create_rectangle(0.5, 0.5, 0.5)
    chair_position = (-3, -2, 0)  # 位于桌子旁边
    
    # 书架
    bookshelf_vertices, bookshelf_edges = create_rectangle(3, 2, 0.5)
    bookshelf_position = (0, 0, -3)  # 位于后墙中央
    
    # 初始参数设置
    camera_position = [0, -1.5, 0]  # 相机位置（模拟眼睛高度）
    focal_length = 1.0  # 固定焦距
    
    # 时钟控制帧率
    clock = pygame.time.Clock()
    
    # 主循环
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # 持续按键检测 - 相机移动
        keys = pygame.key.get_pressed()
        
        # 移动相机（上下左右键）
        if keys[pygame.K_LEFT]:
            camera_position[0] -= 0.1
        if keys[pygame.K_RIGHT]:
            camera_position[0] += 0.1
        if keys[pygame.K_UP]:
            camera_position[1] += 0.1
        if keys[pygame.K_DOWN]:
            camera_position[1] -= 0.1
        # 添加前进后退（W/S键）
        if keys[pygame.K_w]:
            camera_position[2] += 0.1
        if keys[pygame.K_s]:
            camera_position[2] -= 0.1
        
        # 限制相机在房间内移动
        camera_position[0] = max(-4, min(4, camera_position[0]))  # 限制在x轴范围内
        camera_position[1] = max(-2, min(2, camera_position[1]))  # 限制在y轴范围内
        camera_position[2] = max(-4, min(4, camera_position[2]))  # 限制在z轴范围内
        
        # 清除屏幕
        screen.fill(BLACK)
        
        # 绘制房间
        for vertices, position, color in room_parts:
            _, edges = create_rectangle(1, 1, 1)  # 临时创建边，实际使用时应该优化
            draw_rectangle(vertices, edges, position, (0, 0, 0), 
                          camera_position, focal_length, color)
        
        # 绘制房间内的物体
        draw_rectangle(table_vertices, table_edges, table_position, (0, 0, 0), 
                      camera_position, focal_length, RED)
        draw_rectangle(chair_vertices, chair_edges, chair_position, (0, 0, 0), 
                      camera_position, focal_length, BLUE)
        draw_rectangle(bookshelf_vertices, bookshelf_edges, bookshelf_position, (0, 0, 0), 
                      camera_position, focal_length, GREEN)
        
        # 显示操作提示
        instructions = "上下左右键：移动相机视角 | W/S：前进后退 | ESC键：退出"
        text = font_small.render(instructions, True, WHITE)
        screen.blit(text, (20, 20))
        
        # 显示当前位置
        pos_text = f"当前位置: X={camera_position[0]:.1f}, Y={camera_position[1]:.1f}, Z={camera_position[2]:.1f}"
        pos_display = font_small.render(pos_text, True, WHITE)
        screen.blit(pos_display, (20, 45))
        
        # 更新显示
        pygame.display.flip()
        
        # 控制帧率
        clock.tick(60)
    
    # 退出程序
    pygame.quit()
    sys.exit()

# 运行主函数
if __name__ == "__main__":
    main()