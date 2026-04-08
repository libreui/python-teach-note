import pygame
import random

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("贪吃蛇")

# SCORE_FONT = pygame.font.SysFont("SimSong", 25)
SCORE_FONT = pygame.font.Font('./djzt.otf', 25)
# RESULT_FONT = pygame.font.SysFont("SimSong", 25)
RESULT_FONT = pygame.font.Font('./djzt.otf', 25)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SNAKE_BLOCK = 10
SNAKE_SPEED = 8


def draw_score(score):
    """绘制得分"""
    score_text = SCORE_FONT.render("总分数: " + str(score), True, WHITE)
    score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 20))
    SCREEN.blit(score_text, score_rect)


def draw_snake(snake_list):
    """绘制蛇, 由于都是方块，绘制时无需考虑蛇头和蛇身的区别"""
    for x in snake_list:
        pygame.draw.rect(SCREEN, GREEN, [x[0], x[1], SNAKE_BLOCK, SNAKE_BLOCK])


def food_position():
    """随机生成食物的位置"""
    food_x = round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK, SNAKE_BLOCK))
    food_y = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK, SNAKE_BLOCK))
    return food_x, food_y


def draw_result(snake_length):
    """绘制游戏结束后的结果"""
    # 在屏幕中央显示文本
    game_over_text = SCORE_FONT.render("游戏结束", True, RED)
    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    SCREEN.blit(game_over_text, game_over_rect)

    # 显示最终得分
    final_score_text = RESULT_FONT.render("最终得分: " + str(snake_length - 1), True, RED)
    final_score_rect = final_score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    SCREEN.blit(final_score_text, final_score_rect)

    # 显示重新开始提示
    restart_text = RESULT_FONT.render("按'Q'键退出，按'C'键重新开始游戏", True, RED)
    restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
    SCREEN.blit(restart_text, restart_rect)


def game_loop():
    """游戏主循环"""
    game_over = False  # 游戏是否结束
    game_close = False  # 单次游戏是否结束

    # 初始化蛇的坐标和增量
    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2
    x1_change = 0
    y1_change = 0

    # 蛇的身体列表，初始长度为1
    snake_list = []
    snake_length = 1

    # 随机生成食物的位置
    food_x, food_y = food_position()

    while not game_over:
        # 如果游戏结束但未选择退出或重玩， 则进入次循环
        while game_close:
            # 清空屏幕准备下一轮游戏
            SCREEN.fill(BLACK)
            draw_result(snake_length)
            pygame.display.update()  # 更新屏幕

            # 监听键盘事件
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # 监听键盘事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # 左：x坐标减少一个区块，y坐标不变
                    x1_change = -1
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    # 右：x坐标增加一个区块，y坐标不变
                    x1_change = 1
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    # 上：y坐标减少一个区块，x坐标不变
                    y1_change = -1
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    # 下：y坐标增加一个区块，x坐标不变
                    y1_change = 1
                    x1_change = 0

        # 退出游戏
        if game_over:
            break

        # 检测蛇头是否撞墙
        if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
            game_close = True

        # 更新蛇的位置
        x1 += x1_change * SNAKE_BLOCK
        y1 += y1_change * SNAKE_BLOCK

        # 清空屏幕，准备下一轮蛇的绘制
        SCREEN.fill(BLACK)

        # 绘制食物
        pygame.draw.rect(SCREEN, RED, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])

        # 新的蛇头位置， 同时删除最后蛇尾区块， 保持蛇的总长度不变
        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]  # 删除蛇尾

        # 检查蛇头是否碰到身体
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # 绘制蛇
        draw_snake(snake_list)

        # 绘制得分
        draw_score(snake_length - 1)

        # 更新屏幕
        pygame.display.update()

        # 检查蛇头是否碰到食物， 如果碰到则增加长度并重新生成食物
        if x1 == food_x and y1 == food_y:
            food_x, food_y = food_position()
            snake_length += 1

        # 控制游戏帧率
        clock = pygame.time.Clock()
        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()


# 开始游戏
if __name__ == '__main__':
    game_loop()
