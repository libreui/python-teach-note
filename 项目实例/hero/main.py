import conf
from master import Master
from enemy import Enemy
from skill import Skill


class Game:
    def __init__(self, master, enemies):
        self.__name = conf.__GAME_NAME__
        self.__version = conf.__GAME_VERSION__
        # 当前选择的敌人编号
        self.__selected_enemy_num = 0
        # 当前选中的敌人对象
        self.__selected_enemy = None
        self.master = master
        self.enemies = enemies

    def start(self):
        self.__header()
        while True:

            # 主角登场
            self.master.description()

            # 展示敌人信息
            self.__show_enemies()

            n = int(input("选择敌人编号："))
            self.__selected_enemy_num = n

            # 选择玩家技能
            self.master.show_skills()
            n = int(input("选择攻击技能："))
            self.master.set_selected_skill(n)

            # 攻击敌人, 并处理减血
            self.master.selected_skill.attack(
                self.__selected_enemy_num, self.enemies)

            # 敌人攻击回合
            self.__enemys_round()


            if n == 'q':
                break


    def __enemys_round(self):
        """敌人回合"""
        for enemy in self.enemies:
            enemy.attack(self.master)

    def __header(self):
        print('=' * conf.__WIDTH__)
        print(f'{self.__name} v{self.__version}')
        print('=' * conf.__WIDTH__)

        print("游戏背景：")
        print("""
        欢迎来到江湖，你是江湖中的一位侠客，
        听说有一把传说中的屠龙宝刀藏在某个地方，
        你决定踏上寻找屠龙宝刀的道路
        ......
        """)


    def __show_enemies(self):
        """展示敌人信息列表"""
        print(f'----------- 敌人信息 -----------')
        for i in range(len(self.enemies)):
            enemy = self.enemies[i]
            print(f'{i}.{enemy.name}: 生命:{enemy.hp}, 攻击力:{enemy.ack}')
        print('-' * conf.__WIDTH__)



    def __str__(self):
        return f'{self.__name} {self.__version}'


if __name__ == '__main__':
    # 创建技能
    skills = [
        Skill('普通攻击', 10, 10, False),
        Skill('乾坤一掷', 20, 20, False),
        Skill('降龙十八掌', 30, 30, True),
    ]
    # 创建主角
    player = Master(conf.__PLAYER_NAME__, conf.__PLAYER_HP__, conf.__PLAYER_MP__, skills)

    # 创建敌人, 名字使用天龙八部中的反面角色的名字
    enemies = [
        Enemy("段正淳", 100, 10, 0),
        Enemy("段誉", 100, 10, 0),
        Enemy("慕容复", 100, 10, 0),
        Enemy("萧峰", 100, 10, 0),
    ]

    game = Game(player, enemies)
    game.start()

