import conf


class Master:
    def __init__(self, name, hp, mp, skills):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = skills
        self.exp = 0
        # 定义当前级别
        self.level = 1

        # 定义升级经验阶梯
        self.base_exp = 10

        self.selected_skill = None

        self.__set_to_skill_player()


    def __get_level_exp(self, lv):
        """获取当前级别的经验"""
        return self.base_exp * (lv - 1) * 1.5 * (lv - 2)

    def __set_to_skill_player(self):
        """给技能装载玩家信息"""
        for skill in self.skills:
            skill.set_player(self)

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

    def is_died(self):
        """主角是否死亡"""
        return True if self.hp <= 0 else False

    def plus_exp(self, enemy):
        """获取敌人经验"""
        # 敌人如果死了，玩家获取经验
        if enemy.is_died():
            self.exp += enemy.exp
            # 打印日志，从谁身上获取了多少经验
            print(f'从{enemy.name}身上获取了{enemy.exp}经验')

            self.__up_level()

    def __up_level(self):
        # 判断是否升级
        if self.exp >= self.__get_level_exp(self.level + 1):
            self.level += 1
            print(f'恭喜你升级了，当前等级为{self.level}')

        for skill in self.skills:
            skill.up_level()

    def __str__(self):
        return self.name


if __name__ == '__main__':
    master = Master('张无忌', 2000, 100, '')
    master.description()
    master.bleed(20)
    master.description()

