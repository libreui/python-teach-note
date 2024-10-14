import conf


class Game:
    def __init__(self, master, enemies):
        self.__name = conf.__GAME_NAME__
        self.__version = conf.__GAME_VERSION__
        self.master = master
        self.enemies = enemies

    def start(self):
        self.__header()
        while True:

            # TODO 主角登场

            n = input("选择敌人编号：")
            if n == 'q':
                break


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


    def __str__(self):
        return f'{self.__name} {self.__version}'


if __name__ == '__main__':
    game = Game("master", "enemies")
    game.start()

