import pygame.image


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = pygame.image.load('images/me1.png')
        self.speed = 5
        self.bullets = []


    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
