import pygame

# 常量定义
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Ball:
    def __init__(self, screen):
        self.screen = screen
        self.radius = 10
        self.x = screen.get_rect().centerx - 100
        self.y = screen.get_rect().centery
        self.x_value = -1
        self.trajectory = []
        self.max_trajectory_points = 100

    def map_range(self, value, in_range, out_range):
        """范围映射函数"""
        return (value - in_range[0]) / (in_range[1] - in_range[0]) * (out_range[1] - out_range[0]) + out_range[0]

    def update(self):
        """更新小球位置和轨迹"""
        self.x_value += 0.01
        
        # 检查是否需要重置
        if self.x_value > 1:
            self.x_value = -1
            self.trajectory = []
        
        # 计算新位置
        y_value = self.x_value ** 2
        self.x = self.map_range(self.x_value, (-1, 1), (self.screen.get_rect().centerx - 100, self.screen.get_rect().centerx + 100))
        self.y = self.map_range(y_value, (1, 0), (self.screen.get_rect().centery - 100, self.screen.get_rect().centery + 100))
        
        # 添加当前位置到轨迹
        self.trajectory.append((self.x, self.y))
        # 限制轨迹点数量
        if len(self.trajectory) > self.max_trajectory_points:
            self.trajectory.pop(0)

    def draw(self):
        """绘制轨迹和小球"""
        # 绘制轨迹
        if len(self.trajectory) > 1:
            pygame.draw.lines(self.screen, WHITE, False, self.trajectory, 2)
        # 绘制小球
        pygame.draw.circle(self.screen, WHITE, (self.x, self.y), self.radius)


def main():
    # 初始化Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    ball = Ball(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        ball.update()

        screen.fill(BLACK)
        ball.draw()

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
    