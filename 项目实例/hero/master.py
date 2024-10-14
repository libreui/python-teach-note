import conf


class Master:
    def __init__(self, name, hp, mp, skills):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = skills

    def description(self):
        print(f'-------- {self.name} --------')
        print(f'生命：{self.hp}, 魔法：{self.mp}')
        print('-' * conf.__WIDTH__)


if __name__ == '__main__':
    master = Master('张无忌', 2000, 100, '')
    master.description()

