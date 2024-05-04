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

    def __update_sprites(self):
        self.backgrounds.update()
        self.backgrounds.draw(self.screen)


    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlanGame.__game_over()


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


