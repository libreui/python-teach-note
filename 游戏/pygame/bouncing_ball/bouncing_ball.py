import pygame
from pygame.sprite import Sprite, Group


class Ball(Sprite):
    def __init__(self, ball_game):
        super(Ball, self).__init__()
        self.screen = ball_game.screen
        self.screen_rect = ball_game.screen.get_rect()

        self.radius = 6
        self.color = (255, 255, 255)
        self.speed = 5
        self.origin_direction = [-1, 1]
        self.direction = self.origin_direction

        self.x, self.y = 0, 0
        self.reset()
        self.rect = pygame.Rect(self.x, self.y, self.radius, self.radius)


    def reset(self):
        self.x = self.screen_rect.centerx - self.radius//2
        self.y = self.screen_rect.centery - self.radius//2
        self.direction = self.origin_direction

    def update(self):
        self.x += self.speed * self.direction[0]
        self.y += self.speed * self.direction[1]
        if self.x + self.radius >= self.screen_rect.right:
            self.direction = [0, 0]
        if self.x - self.radius <= self.screen_rect.left:
            self.direction = [0, 0]
        if self.y + self.radius >= self.screen_rect.bottom:
            self.direction[1] = -1
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
    def __init__(self, ball_game, side='left'):
        super(Paddle, self).__init__()
        self.screen = ball_game.screen
        self.screen_rect = ball_game.screen.get_rect()
        self.width = 10
        self.height = 100
        self.color = (255, 255, 255)

        self.x = self.screen_rect.left if side == 'left' else self.screen_rect.right - self.width
        self.y = self.screen_rect.centery - self.height//2
        # 左右球拍都距离屏幕边缘10像素
        if side == 'left':
            self.x = self.screen_rect.left + 10
        else:
            self.x = self.screen_rect.right - self.width - 10

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, mouse_pos):
        """球拍只能上下跟随鼠标移动"""
        self.rect.centery = mouse_pos[1]


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
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((600, 600))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Bouncing Ball")

        # 游戏状态
        self.game_active = False

        # 创建按钮
        self.play_button = Button(self, "Play")

        self.ball = Ball(self)

        self.paddle_left = Paddle(self, side='left')
        self.paddle_right = Paddle(self, side='right')

        self.paddles = Group()
        self.paddles.add(self.paddle_left, self.paddle_right)

        # 球拍的加速度
        self.paddle_acceleration = 0.0

    def run(self):
        while True:
            # 当前球拍的y
            current_y = self.paddle_left.rect.centery

            self._check_events()
            self._update_screen()
            self._check_lose()

            pygame.display.update()
            # 计算球拍的加速度
            self.paddle_acceleration = (self.paddle_left.rect.centery - current_y) / 10
            self.clock.tick(30)

    def _update_screen(self):
        self.screen.fill((0, 0, 0))

        if not self.game_active:
            # 绘制按钮
            self.play_button.draw_button()
        else:
            self.ball.draw()
            self.ball.update()

            self.paddle_left.draw()
            self.paddle_right.draw()

            self._check_collision()

        self.paddles.update(pygame.mouse.get_pos())

    def _check_lose(self):
        """检查小球是否离开屏幕"""
        if self.ball.x + self.ball.radius >= self.screen_rect.right\
                or self.ball.x - self.ball.radius <= self.screen_rect.left:
            self.game_active = False
            self.ball.reset()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_button_click(mouse_pos)

    def _check_button_click(self, mouse_pos):
        """检查按钮是否被点击"""
        if self.play_button.rect.collidepoint(mouse_pos):
            self.game_active = True

    def _check_collision(self):
        """检测小球与球拍的碰撞，并反弹"""

        if pygame.sprite.spritecollide(self.ball, self.paddles, False):
            # 小球碰到左边的球拍，改变方向
            if self.ball.x - self.ball.radius <= self.paddle_left.x + self.paddle_left.width:
                # 小球的方向改变，但是改变的方向是根据球拍的加速度来改变的
                self.ball.direction[0] = 1
            # 小球碰到右边的球拍，改变方向
            if self.ball.x + self.ball.radius >= self.paddle_right.x:
                self.ball.direction[0] = -1





if __name__ == '__main__':
    game = Game()
    game.run()
