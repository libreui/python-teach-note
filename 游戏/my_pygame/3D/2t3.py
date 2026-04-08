import pygame

# 窗口设置
WIDTH, HEIGHT = 800, 600
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2

# 初始化pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Rectangle Projection - X-axis Parallel")

# 投影参数
SCALE = 40
CAMERA_POSITION = [0, 0, 0]  # 相机初始位置
FOCAL_LENGTH = 2.0
CAMERA_SPEED = 2.0  # 相机移动速度

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def perspective_projection(point_3d, camera_position, focal_length):
    """将3D点投影到2D平面"""
    x, y, z = point_3d
    cam_x, cam_y, cam_z = camera_position

    # 计算点到相机的z轴距离
    distance = z - cam_z

    # 避免除零错误和位于相机后方的点
    if distance <= 0:
        return None

    # 透视投影计算
    x_proj = focal_length * (x - cam_x) / distance
    y_proj = focal_length * (y - cam_y) / distance

    return x_proj, y_proj


def to_screen_coords(proj_point):
    """将投影坐标转换为屏幕坐标"""
    if proj_point is None:
        return None
    x, y = proj_point
    return CENTER_X + x * SCALE, CENTER_Y - y * SCALE  # 注意y轴反转


def draw_3d_plane(point_3d):
    """通过顶点xyz绘制一个3d平面"""

    # 投影4个顶点
    proj_vertices = []
    for vertex in point_3d:
        proj_point = perspective_projection(vertex, CAMERA_POSITION, FOCAL_LENGTH)
        proj_vertices.append(to_screen_coords(proj_point))

    # print(point_3d, proj_vertices)


    # 绘制矩形的4条边
    pygame.draw.lines(screen,
                      WHITE, True,
                      proj_vertices,
                      1)


# 主循环
running = True
clock = pygame.time.Clock()

while running:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # 键盘持续按下处理
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        CAMERA_POSITION[0] -= CAMERA_SPEED  # 向左移动相机
    if keys[pygame.K_RIGHT]:
        CAMERA_POSITION[0] += CAMERA_SPEED  # 向右移动相机
    if keys[pygame.K_UP]:
        CAMERA_POSITION[1] -= CAMERA_SPEED  # 向上移动相机
    if keys[pygame.K_DOWN]:
        CAMERA_POSITION[1] += CAMERA_SPEED  # 向下移动相机

    # 清除屏幕
    screen.fill(BLACK)

    # 绘制平行于x轴的矩形
    point_3d = [(-50, 0, 30),
                (50, 0, 30),
                (50, 0, 100),
                (-50, 0, 100)]
    draw_3d_plane(point_3d)  # 宽度=10, 高度=5, 深度=3

    # 更新显示
    pygame.display.flip()

    # 控制帧率
    clock.tick(60)

# 退出pygame
pygame.quit()
