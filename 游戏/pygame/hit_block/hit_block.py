import pygame
import sys
from pygame.sprite import Sprite, Group


class Block(Sprite):
    """砖块类"""

    def __init__(self, game, x=0, y=0):
        super().__init__()

        self.screen = game.screen

        self.color = (255, 255, 255)
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y,
                                game.get_block_width(),
                                game.get_block_height())

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Ball(Sprite):
    def __init__(self, ball_game, paddle):
        super(Ball, self).__init__()
        self.paddle = paddle
        self.screen = ball_game.screen
        self.screen_rect = ball_game.screen.get_rect()

        self.game = ball_game

        self.radius = 6
        self.color = (255, 255, 255)
        self.speed = 5
        self.origin_direction = [-1, -1]
        self.direction = self.origin_direction

        self.x, self.y = 0, 0
        self.reset()
        self.rect = pygame.Rect(self.x, self.y, self.radius, self.radius)


    def reset(self):
        self.x = self.paddle.rect.centerx - self.radius//2
        self.y = self.paddle.rect.y
        self.direction = self.origin_direction

    def update(self):
        self.x += self.speed * self.direction[0]
        self.y += self.speed * self.direction[1]

        # TODO 解决小球碰壁的问题
        if self.x + self.radius >= self.screen_rect.right:
            self.direction[0] = -1
        if self.x - self.radius <= self.screen_rect.left:
            self.direction[0] = 1
        if self.y + self.radius >= self.screen_rect.bottom:
            self.direction = [0, 0]
            self.game.reset()

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
        self.width = 100
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



class Game:
    def __init__(self):
        """游戏初始化"""

        self._init_settings()

        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("打砖块")

        self.game_active = False

        self.play_button = Button(self, "Play")

        # 实例化一个时钟
        self.clock = pygame.time.Clock()

        # 砖块的Group
        self.blocks = Group()

        # TODO 创建砖块并添加到砖块集合
        self._fleet_blocks()

        # 创建球拍
        self.pandle = Paddle(self)

        # 实例化球
        self.ball = Ball(self, self.pandle)

    def reset(self):
        self.ball.reset()
        self.game_active = False

        # 清空方块并重新创建
        self.blocks.empty()
        self._fleet_blocks()

    def _fleet_blocks(self):
        """创建砖块"""
        _space = self.__block_width + 5
        _count = 800 // _space
        print("=========>", _count)
        for j in range(1, 10):
            for i in range(_count):
                block = Block(self, i * _space, j * _space)
                self.blocks.add(block)

    def _init_settings(self):
        self.__block_width, self.__block_height = 15, 15

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

                self.ball.draw()
                self.ball.update()

                self.pandle.draw()
                self.pandle.update(pygame.mouse.get_pos())

                self._collided_paddle()
                self._collided_block()

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
        collided = pygame.sprite.collide_rect(self.ball, self.pandle)
        # 检查球碰撞了球拍的长度的比例
        if collided:
            # 计算球和球拍的中心点的距离
            distance = self.ball.rect.centerx - self.pandle.rect.centerx
            # 计算球和球拍的中心点的距离占球拍长度的比例
            ratio = distance / self.pandle.rect.width
            ratio *= 2

            print("比例：", ratio)
            # 根据比例计算球的方向
            self.ball.direction = [ratio, -1]
        # if collided:
        #     self.ball.direction[1] = -1

    def _collided_block(self):
        """碰撞砖块检测"""
        collided = pygame.sprite.spritecollide(self.ball, self.blocks, True)
        if collided:
            # 如果碰到了砖块的侧壁，那么改变方向
            self.ball.direction[1] = 1


if __name__ == "__main__":
    game = Game()
    game.run()
