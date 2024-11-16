import random


class Enemy:
    def __init__(self, name, hp, ack, exp):
        self.name = name
        self.hp = hp
        self.ack = ack
        self.exp = exp

    def __str__(self):
        return f'{self.name}, {self.hp}, {self.ack}, {self.exp}'

    def bleed(self, n):
        """出血"""
        self.hp -= n
        self.hp = 0 if self.hp < 0 else self.hp

    def attack(self, player):
        """攻击玩家"""
        # 玩家闪避几率
        if random.randint(0, 100) <= 50:
            print(f"{self.name}攻击{player.name}，但是被闪避了")
            return
        player.bleed(self.ack)

    def is_died(self):
        """是否死亡"""
        return True if self.hp <= 0 else False


if __name__ == '__main__':
    enemy = Enemy('小兵', 100, 1000, 1000)
    print(enemy)
    from master import Master
    player = Master('aa', 100, 100, [])
    player.description()
    enemy.attack(player)
    player.description()
