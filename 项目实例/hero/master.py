import conf


class Master:
    def __init__(self, name, hp, mp, skills):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = skills
        self.selected_skill = None

        self.__setToSkill()

    def __setToSkill(self):
        """给技能装载玩家信息"""
        for skill in self.skills:
            skill.setPlayer(self)

    def description(self):
        print(f'-------- {self.name} --------')
        print(f'生命：{self.hp}, 魔法：{self.mp}')
        print('-' * conf.__WIDTH__)

    def show_skills(self):
        """展示玩家技能列表"""
        print(f'----------- 选择技能 -----------')
        for i, skill in enumerate(self.skills):
            aoe = '是' if skill.aoe else '否'
            print(f'{i}.{skill.name}: 伤害:{skill.ack}, 消耗:{skill.mp}, 群攻:{aoe}')
        print('-' * conf.__WIDTH__)

    def set_selected_skill(self, num):
        """设置玩家选择的技能"""
        if num >= len(self.skills):
            print(f'请输入正确的技能编号!')
            return
        self.selected_skill = self.skills[num]

    def bleed(self, n):
        """出血"""
        self.hp -= n
        self.hp = 0 if self.hp < 0 else self.hp

    def __str__(self):
        return self.name


if __name__ == '__main__':
    master = Master('张无忌', 2000, 100, '')
    master.description()
    master.bleed(20)
    master.description()

