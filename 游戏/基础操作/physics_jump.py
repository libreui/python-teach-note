import random

import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
radius = 20
x = screen.get_rect().centerx
y = screen.get_rect().bottom - radius
g = 0.8
v_y = 0

speed = 5
x_direction = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                v_y = -15


    parseed = pygame.key.get_pressed()
    if parseed[pygame.K_LEFT]:
        x_direction = -1
    elif parseed[pygame.K_RIGHT]:
        x_direction = 1
    else:
        x_direction = 0


    v_y += g
    y += v_y

    x += speed * x_direction

    if y + radius >= screen.get_rect().bottom:
        y = screen.get_rect().bottom - radius
        # v_y = -v_y * 0.8


    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    pygame.display.flip()
    clock.tick(60)
