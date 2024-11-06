class Enemy:
    def __init__(self, name, hp, attack, exp):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.exp = exp

    def __str__(self):
        return f'{self.name}, {self.hp}, {self.attack}, {self.exp}'


if __name__ == '__main__':
    enemy = Enemy('小兵', 100, 10, 10)
    print(enemy)
