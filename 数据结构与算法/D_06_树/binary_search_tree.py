from tree_node import TreeNode


class BinarySearchTree:
    """二叉搜索树类的实现"""

    def __init__(self):
        """初始化空的二叉搜索树"""
        self.root = None  # 根节点初始化为None
        self.size = 0  # 树中节点数量初始化为0

    def length(self):
        """返回树中节点的数量"""
        return self.size

    def __len__(self):
        """重载Python内置的len()函数，返回树中节点的数量"""
        return self.size

    def __iter__(self):
        """重载Python的迭代器协议，使得树对象可迭代"""
        return self.root.__iter__()  # 委托给根节点的迭代器

    def put(self, key, val):
        """向树中插入键值对(key, val)
        
        Args:
            key: 键，用于确定在树中的位置
            val: 与键关联的值
        """
        if self.root:
            # 如果树不为空，调用辅助方法_put递归插入
            self._put(key, val, self.root)
        else:
            # 如果树为空，创建新的根节点
            self.root = TreeNode(key, val)
            self.size += 1

    def _put(self, key, val, current_node):
        """递归辅助方法，用于在当前节点的子树中插入键值对
        
        Args:
            key: 要插入的键
            val: 要插入的值
            current_node: 当前搜索的节点
        """
        if key == current_node.key:
            # 键已存在，更新当前节点的数据
            # 使用replace_node_data方法，保留现有子节点
            current_node.replace_node_data(key, val, current_node.left_child, current_node.right_child)
        elif key < current_node.key:
            # 键小于当前节点的键，向左子树插入
            if current_node.has_left_child():
                # 如果有左子节点，递归向左子节点插入
                self._put(key, val, current_node.left_child)
            else:
                # 没有左子节点，创建新的左子节点
                current_node.left_child = TreeNode(key, val, parent=current_node)
                self.size += 1
        else:
            # 键大于当前节点的键，向右子树插入
            if current_node.has_right_child():
                # 如果有右子节点，递归向右子节点插入
                self._put(key, val, current_node.right_child)
            else:
                # 没有右子节点，创建新的右子节点
                current_node.right_child = TreeNode(key, val, parent=current_node)
                self.size += 1

    def __setitem__(self, key, value):
        """重载Python的[]运算符，允许使用tree[key] = value语法"""
        self.put(key, value)

    def get(self, key):
        """根据键获取对应的值
        
        Args:
            key: 要查找的键
            
        Returns:
            如果找到键，返回对应的值；否则返回None
        """
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload  # 返回找到节点的值
            else:
                return None
        else:
            return None  # 树为空，返回None

    def _get(self, key, current_node):
        """递归辅助方法，用于在当前节点的子树中查找键
        
        Args:
            key: 要查找的键
            current_node: 当前搜索的节点
            
        Returns:
            如果找到键，返回对应的节点；否则返回None
        """
        if not current_node:
            return None  # 当前节点为None，返回None表示未找到
        elif key == current_node.key:
            return current_node  # 找到键，返回当前节点
        elif key < current_node.key:
            # 键小于当前节点的键，向左子树查找
            return self._get(key, current_node.left_child)
        else:
            # 键大于当前节点的键，向右子树查找
            return self._get(key, current_node.right_child)

    def __getitem__(self, key):
        """重载Python的[]运算符，允许使用tree[key]语法获取值"""
        return self.get(key)

    def __contains__(self, key):
        """重载Python的in运算符，允许使用key in tree语法检查键是否存在"""
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        """从树中删除指定键的节点
        
        Args:
            key: 要删除的键
            
        Raises:
            KeyError: 如果键不在树中
        """
        if self.size > 1:
            # 树中有多个节点
            remove_node = self._get(key, self.root)
            if remove_node:
                # 找到要删除的节点，调用remove方法删除
                self.remove(remove_node)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')  # 键不在树中，抛出异常
        elif self.size == 1 and self.root.key == key:
            # 树中只有一个节点且是要删除的节点
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')  # 树为空或键不在树中，抛出异常

    def remove(self, current_node):
        """从树中删除指定节点，处理三种情况：
           1. 节点是叶子节点（没有子节点）
           2. 节点有一个子节点
           3. 节点有两个子节点
        
        Args:
            current_node: 要删除的节点
        """
        if current_node.is_leaf():
            # 情况1：节点是叶子节点
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None  # 如果是左子节点，将父节点的左子节点设为None
            else:
                current_node.parent.right_child = None  # 如果是右子节点，将父节点的右子节点设为None
        elif current_node.has_both_children():
            # 情况3：节点有两个子节点
            # 找到后继节点（右子树中的最小值）
            succ = current_node.find_successor()
            succ.splice_out()  # 从树中移除后继节点
            # 用后继节点的数据替换当前节点的数据
            current_node.key = succ.key
            current_node.payload = succ.payload
        else:
            # 情况2：节点有一个子节点
            if current_node.has_left_child():
                # 节点有左子节点
                if current_node.is_left_child():
                    # 当前节点是其父节点的左子节点
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    # 当前节点是其父节点的右子节点
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:
                    # 当前节点是根节点
                    current_node.replace_node_data(current_node.left_child.key,
                                                   current_node.left_child.payload,
                                                   current_node.left_child.left_child,
                                                   current_node.left_child.right_child)
            else:
                # 节点有右子节点
                if current_node.is_left_child():
                    # 当前节点是其父节点的左子节点
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    # 当前节点是其父节点的右子节点
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    # 当前节点是根节点
                    current_node.replace_node_data(current_node.right_child.key,
                                                   current_node.right_child.payload,
                                                   current_node.right_child.left_child,
                                                   current_node.right_child.right_child)

    def __delitem__(self, key):
        """重载Python的del运算符，允许使用del tree[key]语法删除节点"""
        self.delete(key)


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree[3] = 'red'
    tree[4] = 'blue'
    tree[6] = 'yellow'
    tree[2] = 'at'
    tree[3] = 'ooxx'
    tree[5] = 'o'
    tree[7] = 'z'
    tree[9] = 'x'
    tree[8] = 'w'
    tree[10] = 'y'
    tree[11] = 'z'

    # print(tree[3])
    # print(tree[4])
    # print(tree[6])
    # print(tree[2])
    #
    # print(3 in tree, 7 in tree)

    del tree[7]
    for key in tree:
        print(key)
