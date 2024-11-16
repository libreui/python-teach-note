import pygame


class Button:
    def __init__(self, gomoku, image_path):
        self.screen = gomoku.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = gomoku.settings

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def draw(self):
        self.screen.blit(self.image, self.rect)
