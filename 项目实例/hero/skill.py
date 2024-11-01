class Skill:
    def __init__(self, name, mp, ack, aoe):
        self.name = name
        self.mp = mp
        self.ack = ack
        self.aoe = aoe

        # 玩家
        self.__player = None


    def setPlayer(self, player):
        self.__player = player

    def showPlayer(self):
        print(self.__player)


    def attack(self, index, enemies):
        """攻击目标"""
        enemy = enemies[index]
        if not self.aoe:
            enemy.bleed(self.ack)
        else:
            self.__aoe(enemies)

    def __aoe(self, enemies):
        """群体攻击"""
        for enemy in enemies:
            enemy.bleed(self.ack)



    def __str__(self):
        return f"技能名称：{self.name}，消耗魔法：{self.mp}，攻击力：{self.attack}，是否范围攻击：{self.aoe}"


if __name__ == "__main__":
    from master import Master

    skill = Skill("火球术", 50, 100, True)
    player = Master('aaa', 2, 2, [skill])
    skill.showPlayer ()

