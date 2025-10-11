class MaxHeapVisualizer:
    """大堆（最大堆）可视化工具

    用于将任意列表转换为大堆并进行树状结构可视化。
    大堆性质：每个节点的值都大于或等于其子节点的值。
    """

    def __init__(self):
        """初始化大堆可视化工具"""
        self.heap_list = [0]  # 索引0不使用，方便计算父节点和子节点
        self.current_size = 0  # 当前堆的大小

    def perc_down(self, i):
        """向下调整大堆，确保大堆性质被维持"""
        while (i * 2) <= self.current_size:
            # 找到最大的子节点
            mc = self.max_child(i)
            # 如果当前节点的值小于最大子节点的值，交换它们
            if self.heap_list[i] < self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            # 移动到最大子节点，继续向下调整
            i = mc

    def max_child(self, i):
        """找到指定节点的最大子节点"""
        # 如果右子节点索引超出堆的大小范围，返回左子节点索引
        if i*2+1 > self.current_size:
            return i * 2
        else:
            # 比较左右子节点的值，返回较大值的索引
            if self.heap_list[i * 2] > self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def build_heap(self, alist):
        """根据给定列表构建大堆"""
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [0] + alist  # 在索引0处添加哨兵元素
        while i > 0:
            self.perc_down(i)
            i //= 2

    def print_tree(self):
        """在命令行中可视化打印大堆的树状结构"""
        if self.current_size == 0:
            print("空堆")
            return

        # 计算树的高度
        height = 0
        temp_size = self.current_size
        while temp_size > 0:
            height += 1
            temp_size = temp_size // 2

        # 每一层的节点间距，根据高度动态调整
        max_width = 2 ** height

        # 从根节点开始逐层打印
        level = 0
        while 2 ** level <= self.current_size + 1:
            # 计算当前层的起始和结束索引
            start_idx = 2 ** level
            end_idx = min(2 ** (level + 1) - 1, self.current_size)

            # 计算当前层的缩进和节点间距
            indent = max_width // (2 ** (level + 1))
            spacing = max_width // (2 ** level)

            # 打印当前层的节点
            print(' ' * indent, end='')
            for i in range(start_idx, end_idx + 1):
                print(f"{self.heap_list[i]:^3}", end='')
                if i < end_idx:
                    print(' ' * (spacing - 3), end='')  # 减去数字占用的宽度
            print()

            # 打印连接线条（如果不是最后一层）
            if level < height - 1:
                print(' ' * (indent - 1), end='')
                for i in range(start_idx, end_idx + 1):
                    if 2 * i <= self.current_size:
                        print('/', end='')
                    else:
                        print(' ', end='')

                    if 2 * i + 1 <= self.current_size:
                        print('\\', end='')
                    else:
                        print(' ', end='')

                    if i < end_idx:
                        print(' ' * (spacing - 2), end='')  # 减去斜线占用的宽度
                print()

            level += 1

# 测试代码：将给定列表可视化为大堆
if __name__ == '__main__':
    # 用户提供的列表
    input_list = [33, 27, 18, 21, 19, 14, 5, 9, 17, 11]

    # 创建大堆可视化工具并构建大堆
    max_heap = MaxHeapVisualizer()
    max_heap.build_heap(input_list)

    # 打印原始列表
    print(f"原始列表: {input_list}")

    # 打印构建的大堆内部表示
    print(f"大堆内部表示: {max_heap.heap_list[1:]}")  # 跳过索引0的哨兵元素

    # 可视化打印大堆树状结构
    print("大堆树状结构:")
    max_heap.print_tree()
