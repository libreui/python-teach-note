import pygame
import random

# 初始化游戏
pygame.init()

# 设置游戏窗口
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("飞机大战")

# 加载图片
player_img = pygame.image.load('./images/me1.png')
enemy_img = pygame.image.load('./images/enemy1.png')
bullet_img = pygame.image.load('./images/bullet1.png')

# 玩家类
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = player_img
        self.speed = 5
        self.bullets = []
    
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
    
    def shoot(self):
        bullet = Bullet(self.x + 24, self.y)
        self.bullets.append(bullet)
    
    def update_bullets(self):
        for bullet in self.bullets:
            bullet.move()
            if bullet.y < 0:
                self.bullets.remove(bullet)

# 敌人类
class Enemy:
    def __init__(self):
        self.x = random.randint(0, screen_width - 64)
        self.y = random.randint(-150, -50)
        self.img = enemy_img
        self.speed = 2
    
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
    
    def move(self):
        self.y += self.speed
        if self.y > screen_height:
            self.x = random.randint(0, screen_width - 64)
            self.y = random.randint(-150, -50)

# 子弹类
class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = bullet_img
        self.speed = 7
    
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
    
    def move(self):
        self.y -= self.speed

player = Player(370, 480)
enemies = [Enemy() for _ in range(5)]
clock = pygame.time.Clock()

# 游戏主循环
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player.speed
    if keys[pygame.K_RIGHT] and player.x < screen_width - 64:
        player.x += player.speed
    
    for enemy in enemies:
        enemy.draw()
        enemy.move()
    
    player.draw()
    player.update_bullets()
    
    for bullet in player.bullets:
        bullet.draw()
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
