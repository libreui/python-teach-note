class Skill:
    def __init__(self, name, mp, attack, aoe):
        self.name = name
        self.mp = mp
        self.attack = attack
        self.aoe = aoe

    def __str__(self):
        return f"技能名称：{self.name}，消耗魔法：{self.mp}，攻击力：{self.attack}，是否范围攻击：{self.aoe}"


if __name__ == "__main__":
    skill = Skill("火球术", 50, 100, True)
    print(skill)
