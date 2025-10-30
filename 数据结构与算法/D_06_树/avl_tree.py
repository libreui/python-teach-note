from binary_search_tree import BinarySearchTree
from tree_node import TreeNode

class AVLTree(BinarySearchTree):
    def __init__(self):
        super().__init__()

    def _put(self, key, value, current_node: TreeNode):
        if key == current_node.key:
            current_node.replace_node_data(key, value, current_node.left_child, current_node.right_child)
        elif key < current_node.key:
            if current_node.has_left_child():
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, value, parent=current_node)
                self.update_balance(current_node.left_child)
        else:
            if current_node.has_right_child():
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, value, parent=current_node)
                self.update_balance(current_node.right_child)

    def update_balance(self, node: TreeNode):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.re_balance(node)
            return

        if node.parent is not None:
            if node.is_left_child():
                node.parent.balance_factor += 1
            else:
                node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def re_balance(self, node):
        if node.balance_factor < 0: # R型
            if node.right_child.balance_factor > 0: # L型
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
        else: # L型
            if node.left_child.balance_factor < 0: # R型
                self.rotate_left(node.left_child)
                self.rotate_right(node)
            else:
                self.rotate_right(node)

    def rotate_left(self, rot_root: TreeNode):
        new_root = rot_root.right_child
        rot_root.right_child = new_root.left_child
        if new_root.left_child is not None:
            new_root.left_child.parent = rot_root
        new_root.parent = rot_root.parent

        if rot_root.is_root():
            self.root = new_root
        else:
            if rot_root.is_left_child():
                rot_root.parent.left_child = new_root
            else:
                rot_root.parent.right_child = new_root
        new_root.left_child = rot_root
        rot_root.parent = new_root

        rot_root.balance_factor = rot_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(rot_root.balance_factor, 0)

    def rotate_right(self, rot_root: TreeNode):
        new_root = rot_root.left_child
        rot_root.left_child = new_root.right_child
        if new_root.right_child is not None:
            new_root.right_child.parent = rot_root
        new_root.parent = rot_root.parent

        if rot_root.is_root():
            self.root = new_root
        else:
            if rot_root.is_left_child():
                rot_root.parent.left_child = new_root
            else:
                rot_root.parent.right_child = new_root
        new_root.right_child = rot_root
        rot_root.parent = new_root

        rot_root.balance_factor = rot_root.balance_factor - 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor - 1 + max(rot_root.balance_factor, 0)


    def to_list(self):
        """将AVL树转换为有序列表
        
        返回一个包含树中所有键值对的列表，按键的升序排列
        每个元素是一个元组：(key, value)
        """
        result = []
        
        # 辅助递归函数，执行中序遍历并收集键值对
        def inorder_collect(node):
            if node:
                inorder_collect(node.left_child)  # 先处理左子树
                result.append((node.key, node.payload))  # 收集当前节点的键值对
                inorder_collect(node.right_child)  # 再处理右子树
        
        if self.root:
            inorder_collect(self.root)  # 从根节点开始遍历
        
        return result

    # 在AVLTree类中添加print_tree方法
    
    def print_tree(self):
        """使用空格符号以堆形状可视化打印二叉树，确保根节点正确显示"""
        if not self.root:
            print("Empty tree")
            return
        
        # 计算树的高度
        def get_height(node):
            if not node:
                return 0
            return 1 + max(get_height(node.left_child), get_height(node.right_child))
        
        height = get_height(self.root)
        max_width = 2 ** height * 4 - 3  # 计算最大宽度
        
        # 使用层序遍历存储每个节点及其在每层的位置
        from collections import deque
        levels = []
        queue = deque([(self.root, 0)])
        
        while queue:
            level_size = len(queue)
            level_nodes = []
            has_non_null = False
            
            for _ in range(level_size):
                node, pos = queue.popleft()
                level_nodes.append((node, pos))
                
                if node:
                    has_non_null = True
                    # 计算子节点位置
                    next_level_pos = 2 * pos
                    queue.append((node.left_child, next_level_pos))
                    queue.append((node.right_child, next_level_pos + 1))
                else:
                    # 空节点也占位
                    queue.append((None, 0))
                    queue.append((None, 0))
            
            levels.append(level_nodes)
            
            # 如果当前层全为空节点，则停止
            if not has_non_null:
                break
        
        # 打印树的结构（仅使用空格）
        level_height = height - 1
        for i, level in enumerate(levels):
            if i >= height:  # 只打印到计算的高度
                break
            
            # 计算当前层的节点间距
            spacing = 2 ** (level_height - i) * 2 - 1
            node_width = spacing + 1
            
            # 打印节点值
            line = [' '] * max_width
            for node, pos in level:
                if node:
                    node_str = f"{node.key}({node.balance_factor})"
                    # 计算节点位置 - 修正计算逻辑确保根节点和所有节点正确显示
                    if i == 0:  # 根节点层
                        node_pos = max_width // 2 - len(node_str) // 2
                    else:
                        node_pos = pos * node_width * 2 + spacing - len(node_str) // 2
                    
                    # 确保位置在有效范围内
                    if 0 <= node_pos < max_width:
                        for j, c in enumerate(node_str):
                            if node_pos + j < max_width:
                                line[node_pos + j] = c
            print(''.join(line))

    def _print_tree_recursive(self, node, prefix, is_last):
        """递归打印树结构，使用ASCII字符表示层级关系"""
        if node is None:
            return
        
        # 处理左右子节点
        if node.has_right_child():
            right_prefix = prefix + ("    " if is_last else "│   ")
            self._print_tree_recursive(node.right_child, right_prefix, False)
        
        # 打印当前节点
        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{node.key}({node.balance_factor}) [{node.payload}]")
        
        # 处理左子节点
        if node.has_left_child():
            left_prefix = prefix + ("    " if is_last else "│   ")
            self._print_tree_recursive(node.left_child, left_prefix, True)

    def print_tree_as_table(self):
        """以表格形式打印AVL树的结构信息"""
        if not self.root:
            print("Empty tree")
            return
        
        # 使用层序遍历收集所有节点信息
        from collections import deque
        nodes_info = []
        queue = deque([(self.root, 0, None)])  # (node, level, parent_key)
        
        while queue:
            node, level, parent_key = queue.popleft()
            
            # 收集节点信息
            node_info = {
                'Key': node.key,
                'Value': node.payload,
                'Balance': node.balance_factor,
                'Level': level,
                'Parent': parent_key,
                'Left Child': node.left_child.key if node.left_child else None,
                'Right Child': node.right_child.key if node.right_child else None
            }
            nodes_info.append(node_info)
            
            # 将子节点加入队列
            if node.left_child:
                queue.append((node.left_child, level + 1, node.key))
            if node.right_child:
                queue.append((node.right_child, level + 1, node.key))
        
        # 打印表格
        # 定义表头
        headers = ['Key', 'Value', 'Balance', 'Level', 'Parent', 'Left Child', 'Right Child']
        
        # 计算每列的最大宽度
        max_widths = {header: len(header) for header in headers}
        for node in nodes_info:
            for header in headers:
                value = node[header]
                # 处理None值
                value_str = str(value) if value is not None else "None"
                max_widths[header] = max(max_widths[header], len(value_str))
        
        # 打印分隔线
        separator = '+'
        for header in headers:
            separator += '-' * (max_widths[header] + 2) + '+'
        
        # 打印表头
        print(separator)
        header_line = '|'
        for header in headers:
            header_line += f" {header.center(max_widths[header])} |"
        print(header_line)
        print(separator)
        
        # 打印数据行
        for node in nodes_info:
            row = '|'
            for header in headers:
                value = node[header]
                value_str = str(value) if value is not None else "None"
                row += f" {value_str.center(max_widths[header])} |"
            print(row)
            print(separator)

# 在主程序中添加表格形式打印的调用
if __name__ == '__main__':
    avl_tree = AVLTree()
    avl_tree[1] = 'a'
    avl_tree[2] = 'b'
    avl_tree[3] = 'c'
    avl_tree[4] = 'd'
    avl_tree[5] = 'e'
    avl_tree[3] = 'f'
    avl_tree[6] = 'g'

    print("AVL树结构 (表格形式):")
    avl_tree.print_tree_as_table()

    print("\nAVL树结构 (堆形状):")
    avl_tree.print_tree()

    # for key in avl_tree:
    #     print(f"{key}")