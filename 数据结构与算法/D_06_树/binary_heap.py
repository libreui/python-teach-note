class BinaryHeap:
    """二叉堆（最小堆）实现
    
    二叉堆是一种特殊的完全二叉树，其中每个节点的值都小于或等于其子节点的值（最小堆）。
    本实现使用列表存储二叉堆，其中索引为0的位置不存储实际数据，用于简化索引计算。
    """
    
    def __init__(self):
        """初始化一个空的最小堆
        
        初始化两个成员变量：
        - heap_list: 存储堆元素的列表，索引0放置哨兵元素0
        - current_size: 当前堆中元素的数量
        """
        self.heap_list = [0]  # 索引0不使用，方便计算父节点和子节点
        self.current_size = 0  # 当前堆的大小

    def perc_up(self, i):
        """向上调整堆，确保堆的性质被维持
        
        参数:
            i: 需要向上调整的元素的索引
        """
        # 当节点有父节点时继续循环（i//2 > 0）
        while i // 2 > 0:
            # 如果当前节点的值小于其父节点的值，交换它们
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            # 移动到父节点，继续向上调整
            i //= 2

    def insert(self, k):
        """向堆中插入一个新元素
        
        参数:
            k: 要插入的元素值
        """
        # 将新元素添加到堆的末尾
        self.heap_list.append(k)
        # 增加堆的大小
        self.current_size += 1
        # 对新插入的元素进行向上调整，维持堆的性质
        self.perc_up(self.current_size)

    def min_child(self, i):
        """找到指定节点的最小子节点
        
        参数:
            i: 当前节点的索引
        
        返回:
            int: 最小子节点的索引
        """
        # 如果右子节点索引超出堆的大小范围，返回左子节点索引
        if i*2+1 > self.current_size:
            return i * 2
        else:
            # 比较左右子节点的值，返回较小值的索引
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def perc_down(self, i):
        """向下调整堆，确保堆的性质被维持
        
        参数:
            i: 需要向下调整的元素的索引
        """
        # 当节点有子节点时继续循环（i*2 <= current_size）
        while (i * 2) <= self.current_size:
            # 找到最小的子节点
            mc = self.min_child(i)
            # 如果当前节点的值大于最小子节点的值，交换它们
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            # 移动到最小子节点，继续向下调整
            i = mc

    def del_min(self):
        """删除并返回堆中的最小值（根节点）
        
        返回:
            堆中的最小值（根节点的值）
        """
        # 保存根节点的值（最小值）
        ret_val = self.heap_list[1]
        # 将最后一个元素移动到根节点位置
        self.heap_list[1] = self.heap_list[self.current_size]
        # 减小堆的大小
        self.current_size -= 1
        # 移除最后一个元素（已移动到根节点）
        self.heap_list.pop()
        # 对新的根节点进行向下调整，维持堆的性质
        self.perc_down(1)
        # 返回被删除的最小值
        return ret_val

    def build_heap(self, alist):
        i = len(alist) // 2
        self.current_size = len(alist)
        self.heap_list = [0] + alist
        while i > 0:
            self.perc_down(i)
            i //= 2
    
    # 打印二叉堆的树状结构图形
    def print_tree(self):
        """在命令行中可视化打印二叉堆的树状结构"""
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
            end_idx = min(2 ** (level + 1) - 1, self.current_size)\
            
            # 计算当前层的缩进和节点间距
            indent = max_width // (2 ** (level + 1))
            spacing = max_width // (2 ** level)\
            
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


if __name__ == '__main__':
    binary_heap = BinaryHeap()
    # binary_heap.insert(5)
    # binary_heap.insert(9)
    # binary_heap.insert(11)
    # binary_heap.insert(14)
    # binary_heap.insert(18)
    # binary_heap.insert(19)
    # binary_heap.insert(21)
    # binary_heap.insert(33)
    # binary_heap.insert(17)
    # binary_heap.insert(27)
    # print(binary_heap.heap_list)
    # print("二叉堆树状结构:")
    # binary_heap.print_tree()
    # print(binary_heap.min_child(2))
    # print(binary_heap.del_min())
    # print("删除最小值后的二叉堆树状结构:")
    # binary_heap.print_tree()
    # print(binary_heap.heap_list)
    #
    # alist = [9, 6, 5, 2, 3]
    # binary_heap.build_heap(alist)
    # binary_heap.print_tree()

    # binary_heap.build_heap([33, 27, 18, 21, 19, 14, 5, 9, 17, 11])
    binary_heap.build_heap([12, 11, 13, 5, 6, 7])
    binary_heap.print_tree()



