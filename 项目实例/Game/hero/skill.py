class Skill:
    def __init__(self, name, mp, ack, aoe):
        self.name = name
        self.mp = mp
        self.ack = ack
        self.aoe = aoe

        # 玩家
        self.__player = None

    def set_player(self, player):
        # 设置一个玩家
        self.__player = player


    def attack(self, index, enemies):
        """攻击目标"""
        enemy = enemies[index]
        if not self.aoe:
            # 判断mp够不够
            self.__minus_mp(enemy)
            # 敌人如果死了，玩家获取经验
            self.__player.plus_exp(enemy)
        else:
            self.__aoe(enemies)


    def __aoe(self, enemies):
        """群体攻击"""
        for enemy in enemies:
            # 判断mp够不够
            self.__minus_mp(enemy)
            # 敌人如果死了，玩家获取经验
            self.__player.plus_exp(enemy)



    def __minus_mp(self, enemy):

        if self.__player.mp < self.mp:
            print(f"{self.__player.name}的魔法值不够")
            return
        enemy.bleed(self.ack)
        # 减去mp
        self.__player.mp -= self.mp
        if self.__player.mp < 0:
            self.__player.mp = 0
        self.__show_log(enemy)


    def __show_log(self, enemy):
        #  打印攻击敌人日志
        print(f"{self.__player.name}用{self.name}技能攻击了{enemy.name}, 造成了{self.ack}点伤害")


    def up_level(self):
        """升级"""
        self.ack *= self.__player.level




    def __str__(self):
        return f"技能名称：{self.name}，消耗魔法：{self.mp}，攻击力：{self.ack}，是否范围攻击：{self.aoe}"



if __name__ == "__main__":
    from master import Master

    skill = Skill("火球术", 50, 100, True)
    player = Master('aaa', 2, 2, [skill])


