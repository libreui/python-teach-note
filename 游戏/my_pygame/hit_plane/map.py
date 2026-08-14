import pygame


class Map:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings

        self.image = pygame.image.load("./image/ditu.jpg")
        self.rect = self.image.get_rect()

        self.image_o = self.image.copy()
        self.rect_o = self.image_o.get_rect()
        self.rect_o.bottom = self.screen_rect.top


    def update(self):
        if self.rect.top >= self.screen_rect.bottom:
            self.rect.bottom = self.screen_rect.top
        if self.rect_o.top >= self.screen_rect.bottom:
            self.rect_o.bottom = self.screen_rect.top

        self.rect.y += self.settings.map_speed
        self.rect_o.y += self.settings.map_speed


    def show_map(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image_o, self.rect_o)
