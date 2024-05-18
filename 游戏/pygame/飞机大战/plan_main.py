import pygame
from game_sprites import *


class PlanGame(object):
    def __init__(self):
        print("游戏初始化...")
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
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


    def __update_sprites(self):
        self.backgrounds.update()
        self.backgrounds.draw(self.screen)

        # 敌机组更新
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        # 飞机组更新
        self.hero_group.update()
        self.hero_group.draw(self.screen)


    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlanGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌人出场")
                enemy = Enemy()
                self.enemy_group.add(enemy)

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


