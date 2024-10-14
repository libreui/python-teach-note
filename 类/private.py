# 私有属性、私有方法
class P:
    def __init__(self):
        # 公有
        self.name = "李四"
        # 私有
        self.__name = "张三"


    def showName(self):
        print(self.__name)


    def update(self, name):
        self.__name = name




p = P()
p.showName()
p.update("王五")
p.showName()


