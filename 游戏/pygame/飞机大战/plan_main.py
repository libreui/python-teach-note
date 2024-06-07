import pygame
import random
from game_sprites import *


class PlanGame(object):
    def __init__(self):
        print("游戏初始化...")
        pygame.init()
        # 1.创建游戏窗口, 设置窗口大小
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏时钟
        self.clock = pygame.time.Clock()
        # 3. 调用创建精灵和精灵组的代码
        self.__create_sprites()
        # 4. 设置定时器事件
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)


    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(True)
        self.backgrounds = pygame.sprite.Group(bg1, bg2)

        # 敌机精灵
        self.enemy_group = pygame.sprite.Group()

        # 英雄精灵
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)


    def __check_collide(self):
        """碰撞检测"""
        # 1. 子弹摧毁敌机
        # collide = pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        # 如果子弹摧毁了敌机，播放敌机爆炸动画，并移除子弹和敌机
        if len(self.enemy_group) > 0:
            for bullet in self.hero.bullets:
                bullet.check_collide(self.enemy_group)



    def __update_sprites(self):
        self.backgrounds.update()
        self.backgrounds.draw(self.screen)

        # 敌机组更新
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        # 飞机组更新
        self.hero_group.update()
        self.hero_group.draw(self.screen)

        # 子弹精灵族更新
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)


    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlanGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:

                if random.randint(0, 10) > 9:
                    enemy = BigEnemy()
                    self.enemy_group.add(enemy)
                    print("敌人出场", enemy.rect)
                else:
                    enemy = Enemy()
                    self.enemy_group.add(enemy)
                    print("敌人出场", enemy.rect)


            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE:
                    self.hero.fire()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 3
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -3
        else:
            self.hero.speed = 0


    def start(self):
        print("游戏开始...")
        while True:
            self.clock.tick(FRAME_PER_SEC)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()


    @staticmethod
    def __game_over():
        print("游戏结束...")
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlanGame()
    game.start()


