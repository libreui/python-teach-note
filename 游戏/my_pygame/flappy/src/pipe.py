from config import Config
from resource import ResourceManager
from pygame.sprite import Sprite, Group
import pygame
import random


class Pipe(Sprite):
    """单个管道类（包含上管道和下管道）"""

    def __init__(self, x, gap_y):
        super().__init__()
        self.config = Config()
        self.resource = ResourceManager()

        # 管道是否被积分
        self.scored = False

        # 加载管道图片
        self.pipe_image = self.resource.get_pipe_images()[self.config.PIPE_COLOR]
        self.pipe_image_top = pygame.transform.flip(self.pipe_image, False, True)
        self.pipe_image_bottom = self.pipe_image

        # 管道位置参数
        self.gap_y = gap_y
        self.gap_height = self.config.PIPE_GAP

        # 创建上管道（从顶部延伸到空隙上方）
        self.top_rect = pygame.Rect(
            x,
            self.gap_y - self.config.PIPE_HEIGHT,
            self.config.PIPE_WIDTH,
            self.config.PIPE_HEIGHT
        )

        # 创建下管道（从空隙下方延伸到底部）
        self.bottom_rect = pygame.Rect(
            x,
            self.gap_y + self.gap_height,
            self.config.PIPE_WIDTH,
            self.config.PIPE_HEIGHT
        )

        # 设置精灵的主rect（用于碰撞检测）
        self.rect = pygame.Rect(x, 0, self.config.PIPE_WIDTH, self.config.HEIGHT)

    def update(self):
        """更新管道位置"""
        speed = self.config.SPEED
        self.top_rect.x -= speed
        self.bottom_rect.x -= speed
        self.rect.x -= speed

    def draw(self, screen):
        """绘制管道"""
        screen.blit(self.pipe_image_top, self.top_rect)
        screen.blit(self.pipe_image_bottom, self.bottom_rect)

    def is_off_screen(self):
        """检查管道是否已移出屏幕左侧"""
        return self.top_rect.right < 0


class PipeGroup:
    """管道编组类 - 管理所有管道的生成、更新和回收"""

    def __init__(self, flappy):
        self.flappy = flappy
        self.config = flappy.config
        self.screen = flappy.screen

        # 管道精灵组
        self.pipes = Group()

        # 管道生成控制
        self.pipe_spacing = self.config.PIPE_SPACING  # 管道水平间距（右边缘到右边缘）
        self.buffer_distance = self.config.WIDTH // 2  # 预生成距离（屏幕外多远开始生成）

    def build(self):
        """构建所有管道"""
        self._spawn_initial_pipes()

    def _spawn_initial_pipes(self):
        """生成初始管道（包含预生成管道）"""
        # 第一个管道从屏幕右侧外 buffer_distance 处开始
        # 这样管道可以平滑进入屏幕
        start_x = self.config.WIDTH + self.buffer_distance - self.config.PIPE_WIDTH

        # 生成多个管道，覆盖屏幕内和屏幕外缓冲区
        x = start_x
        while x < start_x + self.pipe_spacing * 5:  # 生成5个初始管道
            self._spawn_pipe(x)
            x += self.pipe_spacing

    def _spawn_pipe(self, x):
        """生成单个管道（带空隙）"""
        # 定义管道露出部分的高度（视觉效果）
        pipe_head_height = 50

        # 获取地面顶部Y坐标
        ground_top_y = self.flappy.ground.rect.top

        # 计算空隙中心位置范围
        min_y = self.config.PIPE_GAP // 2 + pipe_head_height
        max_y = ground_top_y - self.config.PIPE_GAP // 2 - pipe_head_height

        # 确保范围有效
        if min_y > max_y:
            min_y = max_y = ground_top_y // 2

        # 随机生成空隙中心位置
        gap_y = random.randint(min_y, max_y)

        # 创建管道对象并添加到组
        pipe = Pipe(x, gap_y)
        self.pipes.add(pipe)

    def update(self):
        """更新所有管道"""
        # 更新管道位置
        self.pipes.update()

        # 移除屏幕外的管道
        for pipe in self.pipes:
            if pipe.is_off_screen():
                pipe.kill()

        # 检查是否需要生成新管道
        if self.pipes:
            # 找到最右边管道的右边缘位置
            rightmost_pipe_right = max(pipe.top_rect.right for pipe in self.pipes)

            # 当最右边管道的右边缘 <= WIDTH + buffer_distance - pipe_spacing 时
            # 在屏幕外 buffer_distance 处生成新管道
            if rightmost_pipe_right <= self.config.WIDTH + self.buffer_distance - self.pipe_spacing:
                new_x = self.config.WIDTH + self.buffer_distance - self.config.PIPE_WIDTH
                self._spawn_pipe(new_x)

    def draw(self, surface):
        """绘制所有管道"""
        for pipe in self.pipes:
            pipe.draw(surface)

    def check_collision(self, bird):
        """检测小鸟与管道的碰撞"""
        for pipe in self.pipes:
            if bird.rotated_rect.colliderect(pipe.top_rect) or \
                    bird.rotated_rect.colliderect(pipe.bottom_rect):
                return True
        return False

    def reset(self):
        """重置所有管道"""

        self.pipes.empty()
        # self._spawn_initial_pipes()

    def check_score(self, bird):
        """检测小鸟是否通过管道并计分"""
        score_increment = 0
        for pipe in self.pipes:
            # 当小鸟的中心通过管道空隙的中心位置时计分
            # 这样视觉上更及时，不会有延迟感
            pipe_center_x = pipe.top_rect.centerx
            bird_center_x = bird.rotated_rect.centerx
            if not pipe.scored and bird_center_x > pipe_center_x:
                pipe.scored = True
                score_increment += 1
        return score_increment