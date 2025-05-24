import random

import pygame
import sys

from pygame import Rect
from pygame.sprite import Sprite, Group


class Block(Sprite):
    """砖块类"""

    def __init__(self, game, x=0, y=0):
        super().__init__()

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        # 是否可以被删除
        self.killed_enable = True

        self.color = (255, 255, 255)
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y,
                                game.get_block_width(),
                                game.get_block_height())

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Ball(Sprite):
    def __init__(self, ball_game, paddle, diction=None):
        super(Ball, self).__init__()

        # 设置默认方向
        if diction is None:
            diction = [-1, -1]

        self.paddle = paddle
        self.screen = ball_game.screen
        self.screen_rect = ball_game.screen.get_rect()

        self.game = ball_game

        self.radius = 6
        self.color = (255, 255, 255)
        self.speed = 5
        self.origin_direction = diction
        self.direction = self.origin_direction

        self.x, self.y = 0, 0
        self.reset()
        self.rect = pygame.Rect(self.x, self.y, self.radius, self.radius)

    def _get_speed(self):
        if self.game.cur_point == 0:
            return self.speed
        return self.speed + (self.game.cur_point / self.game.total_point) * 10

    def reset(self):
        self.x = self.paddle.rect.centerx - self.radius // 2
        self.y = self.paddle.rect.y - 20
        self.direction = self.origin_direction

    def update(self):
        self.x += self._get_speed() * self.direction[0]
        self.y += self._get_speed() * self.direction[1]

        # TODO 解决小球碰壁的问题
        if self.x + self.radius >= self.screen_rect.right:
            self.direction[0] = -1
        if self.x - self.radius <= self.screen_rect.left:
            self.direction[0] = 1
        if self.y + self.radius >= self.screen_rect.bottom:
            self.direction = [0, 0]
            self.game.reset(self)

        if self.y - self.radius <= self.screen_rect.top:
            self.direction[1] = 1

        self.rect.centerx = self.x
        self.rect.centery = self.y

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)


class Paddle(Sprite):
    """
    球拍对象
    @param ball_game: 游戏对象
    @param side: 球拍的位置，left or right
    """

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.x, self.y = 0, 0
        self.width = 800
        self.height = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10
        self.color = (255, 255, 255)

    def update(self, mouse_pos):
        """球拍只能上下跟随鼠标移动"""
        self.rect.centerx = mouse_pos[0]

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Button:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # 设置按钮的一些基本属性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)

        # 按钮矩形
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 文字对象 + 文字大小
        self.font = pygame.font.SysFont(None, 48)

        # 绘制文字
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """绘制按钮文字"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """绘制按钮"""
        # 绘制按钮矩形
        self.screen.fill(self.button_color, self.rect)
        # 绘制按钮文字
        self.screen.blit(self.msg_image, self.msg_image_rect)


class ProgressBar:
    def __init__(self, surface, x, y, width, height):
        self.surface = surface
        self.surface_rect = surface.get_rect()
        self.x = x
        self.y = y
        self.bg = (255, 255, 255)
        self.front = (0, 0, 0)
        self.bg_rect = Rect(self.x, self.y, width, height)
        self.front_rect = Rect(self.bg_rect.x + 1, self.bg_rect.y + 1, width - 2, height - 2)

    def draw_text(self, cur=0, total=0):
        font = pygame.font.SysFont(None, 9)
        text = font.render(f"{cur}/{total}", True, self.bg, self.front)
        x = self.front_rect.x + (self.front_rect.width - text.get_width()) // 2
        y = self.front_rect.y + (self.front_rect.height - text.get_height()) // 2
        self.surface.blit(text, (x, y))

    def draw(self, cur=0, total=100):
        # 当前进度，总进度
        # 绘制背景
        pygame.draw.rect(self.surface, self.bg, self.bg_rect)
        pygame.draw.rect(self.surface, self.front, self.front_rect)
        # 设置宽度
        if total == 0:
            return
        progress_width = (self.bg_rect.width - 4) * (cur / total)
        progress_rect = Rect(self.front_rect.x + 1,
                             self.front_rect.y + 1,
                             progress_width, self.bg_rect.height - 4)

        pygame.draw.rect(self.surface, self.bg, progress_rect)
        # self.draw_text(cur, total)


class DarkBlock(Block):
    def __init__(self, game, x=0, y=0):
        super().__init__(game, x, y)
        self.killed_enable = False
        self.color = (150, 150, 150)



class GreenBlock(Block):
    def __init__(self, game, x=0, y=0):
        super().__init__(game, x, y)
        self.count = random.randint(1, 3)
        self.color = (255, 165, 0)


    def draw_text(self):
        # pygame.font.SysFont(None, 8)
        font = pygame.font.Font("unifont.otf", 12)
        text = font.render(f"{self.count}", True, (0, 0, 0), None)
        x = self.rect.x + (self.rect.width - text.get_width()) // 2
        self.screen.blit(text, (x, self.rect.y))

    def draw(self):
        super().draw()
        self.draw_text()

    def update(self):
        self.y += 2
        self.rect.centery = self.y


class Game:
    def __init__(self):
        """游戏初始化"""

        self.cur_point = 0
        self.total_point = 0
        self._init_settings()

        self.w = 800
        self.h = 600

        pygame.init()
        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("打砖块")

        self.game_active = False

        self.play_button = Button(self, "Play")

        # 实例化一个时钟
        self.clock = pygame.time.Clock()

        # 实例化进度条
        self.progress_bar = ProgressBar(self.screen, self.w - 105, 5, 100, 10)

        # 砖块的Group
        self.blocks = Group()

        # 创建砖块并添加到砖块集合
        self._fleet_blocks()

        # 创建球拍
        self.pandle = Paddle(self)

        # 实例化球编组
        self.ball_count = 1
        self.balls = Group()
        self._feet_balls()

        # 创建彩色砖块编组
        self.green_blocks = Group()

    def reset(self, ball=None):
        # 删除球
        if ball and len(self.balls) > 1:
            self.balls.remove(ball)
        else:
            self._rest_balls()

            # 清空方块并重新创建
            self.blocks.empty()
            self._fleet_blocks()

            # 清空积分
            self.cur_point = 0
            self.total_point = 0

            self.game_active = False

    def _add_green_block(self, block):
        """添加彩色砖块"""
        if len(self.green_blocks) > 2:
            return
        if self.cur_point % 10 != 0:
            return

        green_block = GreenBlock(self, block.rect.x, block.rect.y)
        self.green_blocks.add(green_block)

        print(len(self.green_blocks))

    def _fleet_blocks(self):
        """创建砖块"""
        _space = self.__block_width + 5
        _count = 800 // _space
        for j in range(1, 10):
            for i in range(_count):
                if random.randint(0, 10) > 8:
                    block = DarkBlock(self, i * _space, j * _space)
                else:
                    block = Block(self, i * _space, j * _space)
                self.blocks.add(block)
                self.total_point += 1

    def _feet_balls(self):
        for i in range(self.ball_count):
            # 创建一个0到1的小数
            ball = Ball(self, self.pandle, [random.uniform(-1, 1), -1])
            self.balls.add(ball)

    def _split_ball(self, count):
        """分裂小球"""
        for ball in self.balls:
            for i in range(count):
                x = ball.x
                y = ball.y
                diction = [random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)]
                new_ball = Ball(self, self.pandle, diction)
                new_ball.x = x
                new_ball.y = y
                self.balls.add(new_ball)

    def _rest_balls(self):
        # 删除所有球
        # 并再次创建
        self.balls.empty()
        self._feet_balls()

    def _draw_score(self):
        """绘制积分"""
        font = pygame.font.SysFont(None, 20)
        score_image = font.render(f"Score: {self.cur_point}/{self.total_point}", True, (255, 255, 255))
        self.screen.blit(score_image, (5, 5))

    def _init_settings(self):
        self.__block_width, self.__block_height = 15, 15
        self.cur_point = 0
        self.total_point = 0

    def get_block_width(self):
        """获取砖块的宽"""
        return self.__block_width

    def get_block_height(self):
        return self.__block_height

    def run(self):
        """运行游戏"""
        while True:
            self.screen.fill((0, 0, 0))
            # 事件循环
            self._check_event()

            if not self.game_active:
                # 显示鼠标
                pygame.mouse.set_visible(True)
                self.play_button.draw_button()
            else:
                # 隐藏鼠标
                pygame.mouse.set_visible(False)
                # 渲染屏幕
                for block in self.blocks:
                    block.draw()

                # 绘制球编组中的球
                for ball in self.balls:
                    ball.draw()
                self.balls.update()

                self.pandle.draw()
                self.pandle.update(pygame.mouse.get_pos())

                # 绘制彩色砖块
                for green_block in self.green_blocks:
                    green_block.draw()
                self.green_blocks.update()

                self._collided_paddle()
                self._collided_block()
                self._collided_green_block()

                # 绘制积分
                self._draw_score()

                # 绘制进度条
                self.progress_bar.draw(self.cur_point, self.total_point)


            pygame.display.update()

            self.clock.tick(60)

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._click_play_button(pygame.mouse.get_pos())

    def _click_play_button(self, mouse_pos):
        """点击开始按钮"""
        if self.play_button.rect.collidepoint(mouse_pos):
            self.game_active = True

    def _collided_paddle(self):
        """碰撞球拍检测"""
        for ball in self.balls:
            collided = pygame.sprite.collide_rect(ball, self.pandle)
            # 检查球碰撞了球拍的长度的比例
            if collided:
                # 计算球和球拍的中心点的距离
                distance = ball.rect.centerx - self.pandle.rect.centerx
                # 计算球和球拍的中心点的距离占球拍长度的比例
                ratio = distance / self.pandle.rect.width
                ratio *= 2

                # 根据比例计算球的方向
                ball.direction = [ratio, -1]
            # if collided:
            #     self.ball.direction[1] = -1

    def _collided_block(self):
        """碰撞砖块检测"""
        for ball in self.balls:

            # 不是True|False, [block,block]
            collided_block = pygame.sprite.spritecollide(ball, self.blocks, False)

            # 如果碰到的的砖块killed_enable是True则改变方向并加分，否则不加分只改方向
            if collided_block:
                for block in collided_block:
                    if block.killed_enable:
                        self.blocks.remove(block)
                        # 如果碰到了砖块的侧壁，那么改变方向[0, 0]
                        ball.direction[1] = -ball.direction[1]
                        self.cur_point += 1
                        # 添加彩色砖块
                        self._add_green_block(collided_block[0])
                    else:
                        ball.direction[1] = -ball.direction[1]

    def _collided_green_block(self):
        """碰撞彩色砖块检测"""
        for green_block in self.green_blocks:
            collided = pygame.sprite.collide_rect(green_block, self.pandle)
            if collided:
                # TODO 分裂小球
                self._split_ball(green_block.count)
                self.green_blocks.remove(green_block)
            # 超过屏幕底部删除
            if green_block.rect.bottom >= self.h:
                self.green_blocks.remove(green_block)


if __name__ == "__main__":
    game = Game()
    game.run()
