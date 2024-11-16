class GomokuAI:

    def __init__(self, board):
        """
        初始化 GomokuAI 类的实例。

        初始化棋盘状态、方向向量、游戏结束标志、先手标志、起始标志、AI 标志、
        最大值和最小值变量、列表、重启标志和退出标志。
        """
        self.L1_max = -100000  # 剪枝阈值
        self.L2_min = 100000

        self.dx = [1, 1, 0, -1, -1, -1, 0, 1]  # x,y方向向量
        self.dy = [0, 1, 1, 1, 0, -1, -1, -1]

        self.num = board

    def inBoard(self, x, y):
        """判断该点是否在棋盘范围内"""
        if 0 <= x < 15 and 0 <= y < 15:
            return True
        else:
            return False

    def downOk(self, x, y):
        """判断该点是否可落子，即是否在棋盘内且没有落子"""
        if self.inBoard(x, y) and self.num[x][y] == '':
            return True
        else:
            return False

    def get_best_move(self):
        return self.AI1()

    def AI1(self):
        """博弈树第一层"""
        self.L1_max = -100000
        keyi, keyj = -1, -1
        for x in [8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 0]:
            for y in [8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 0]:
                if not self.downOk(x, y):
                    continue
                self.num[x][y] = 'o'
                temp_point = self.getScore(x, y)
                if temp_point == 0:
                    self.num[x][y] = ''
                    continue
                if temp_point == 10000:
                    return x, y
                temp_point = self.AI2()
                self.num[x][y] = ''
                if temp_point > self.L1_max:  # 取极大
                    self.L1_max = temp_point
                    keyi, keyj = x, y
        return keyi, keyj

    def AI2(self):
        """博弈树第二层"""
        self.L2_min = 100000
        for x in [8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 0]:
            for y in [8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 0]:
                if not self.downOk(x, y):
                    continue
                self.num[x][y] = 'x'
                tempp = self.getScore(x, y)
                if tempp == 0:
                    self.num[x][y] = ''
                    continue
                if tempp == 10000:
                    self.num[x][y] = ''
                    return -10000
                tempp = self.AI3(tempp)
                if tempp < self.L1_max:  # L1层剪枝
                    self.num[x][y] = '';
                    return -10000
                self.num[x][y] = ''
                if tempp < self.L2_min:  # 取极小
                    self.L2_min = tempp
        return self.L2_min

    def AI3(self, p2):
        """博弈树第三层"""
        keyp = -100000
        for x in [8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 0]:
            for y in [8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 0]:
                if not self.downOk(x, y):
                    continue
                self.num[x][y] = 'o'
                tempp = self.getScore(x, y)
                if tempp == 0:
                    self.num[x][y] = ''
                    continue
                if tempp == 10000:
                    self.num[x][y] = ''
                    return 10000
                if tempp - p2 * 2 > self.L2_min:  # L2层剪枝
                    self.num[x][y] = ''
                    return 10000
                self.num[x][y] = ''
                if tempp - p2 * 2 > keyp:  # 取极大
                    keyp = tempp - p2 * 2
        return keyp

    def getScore(self, x, y):
        """对该点落子后的局势进行估分"""

        score = self.liveFour(x, y) * 1000 + (self.chongFour(x, y) + self.liveThree(x, y)) * 100
        for u in range(8):
            if self.inBoard(x + self.dx[u], y + self.dy[u]) and self.num[x + self.dx[u]][y + self.dy[u]] != '':
                score = score + 1
        return score

    def liveThree(self, x, y):
        """该点四个方向里活三，以及八个方向里断三的个数"""
        key = self.num[x][y]
        s = 0
        for u in range(4):
            samekey = 1
            samekey, i = self.numofSamekey(x, y, u, 1, key, samekey)
            if not self.downOk(x + self.dx[u] * i, y + self.dy[u] * i):
                continue
            if not self.downOk(x + self.dx[u] * (i + 1), y + self.dy[u] * (i + 1)):
                continue
            samekey, i = self.numofSamekey(x, y, u, -1, key, samekey)
            if not self.downOk(x + self.dx[u] * i, y + self.dy[u] * i):
                continue
            if not self.downOk(x + self.dx[u] * (i - 1), y + self.dy[u] * (i - 1)):
                continue
            if samekey == 3:
                s += 1
        for u in range(8):
            samekey = 0
            flag = True
            i = 1
            while self.sameColor(x + self.dx[u] * i, y + self.dy[u] * i, key) or flag:
                if not self.sameColor(x + self.dx[u] * i, y + self.dy[u] * i, key):
                    if flag and self.inBoard(x + self.dx[u] * i, y + self.dy[u] * i) and self.num[x + self.dx[u] * i][y + self.dy[u] * i] != 0:
                        samekey -= 10
                    flag = False
                samekey += 1
                i += 1
            if not self.downOk(x + self.dx[u] * i, y + self.dy[u] * i):
                continue
            if self.inBoard(x + self.dx[u] * (i - 1), y + self.dy[u] * (i - 1)) and self.num[x + self.dx[u] * (i - 1)][y + self.dy[u] * (i - 1)] == 0:
                continue
            samekey, i = self.numofSamekey(x, y, u, 1, key, samekey)
            if not self.downOk(x + self.dx[u] * i, y + self.dy[u] * i):
                continue
            if samekey == 3:
                s += 1
        return s

    def chongFour(self, x, y):
        """该点八个方向里(即v区分正负)，冲四局势的个数"""
        key = self.num[x][y]
        s = 0
        for u in range(8):
            samekey = 0
            flag = True
            i = 1
            while self.sameColor(x + self.dx[u] * i, y + self.dy[u] * i, key) or flag:
                if not self.sameColor(x + self.dx[u] * i, y + self.dy[u] * i, key):
                    if flag and self.inBoard(x + self.dx[u] * i, y + self.dy[u] * i) and self.num[x + self.dx[u] * i][y + self.dy[u] * i] != 0:
                        samekey -= 10
                    flag = False
                samekey += 1
                i += 1
            i -= 1
            if not self.inBoard(x + self.dx[u] * i, y + self.dy[u] * i):
                continue
            samekey, i = self.numofSamekey(x, y, u, -1, key, samekey)
            if samekey == 4:
                s += 1
        return s - self.liveFour(x, y) * 2

    def liveFour(self, x, y):
        """该点四个方向里(即v不区分正负)，活四局势的个数"""
        key = self.num[x][y]
        s = 0
        for u in range(4):
            samekey = 1
            samekey, i = self.numofSamekey(x, y, u, 1, key, samekey)
            if not self.downOk(x + self.dx[u] * i, y + self.dy[u] * i):
                continue
            samekey, i = self.numofSamekey(x, y, u, -1, key, samekey)
            if not self.downOk(x + self.dx[u] * i, y + self.dy[u] * i):
                continue
            if samekey == 4:
                s = s + 1
        return s

    def numofSamekey(self, x, y, u, i, key, sk):
        """统计在u方向上，和key值相同的点的个数，即和key同色的连子个数"""
        if i == 1:
            while self.sameColor(x + self.dx[u] * i, y + self.dy[u] * i, key):
                sk += 1
                i += 1
        elif i == -1:
            while self.sameColor(x + self.dx[u] * i, y + self.dy[u] * i, key):
                sk += 1
                i -= 1
        return sk, i

    def sameColor(self, x, y, i):
        if self.inBoard(x, y) and self.num[x][y] == i:
            return True
        else:
            return False
