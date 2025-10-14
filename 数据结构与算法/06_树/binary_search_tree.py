from tree_node import TreeNode


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
            self.size += 1

    def _put(self, key, val, current_node):
        if key == current_node.key:
            # 使用正确的replace_node_data方法，保留现有子节点
            current_node.replace_node_data(key, val, current_node.left_child, current_node.right_child)
        elif key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val, parent=current_node)
                self.size += 1
        else:
            # 修正右子树递归调用，使用方法调用结果而不是方法引用
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val, parent=current_node)
                self.size += 1

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif key == current_node.key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            remove_node = self._get(key, self.root)
            if remove_node:
                self.remove(remove_node)
                self.size -= 1
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

    def remove(self, current_node):
        if current_node.is_leaf():
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_both_children():
            succ = current_node.find_successor()
            succ.splice_out()
            current_node.key = succ.key
            current_node.payload = succ.payload
        else:
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:
                    current_node.replace_node_data(current_node.left_child.key,
                                                    current_node.left_child.payload,
                                                    current_node.left_child.left_child,
                                                    current_node.left_child.right_child)
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_node_data(current_node.right_child.key,
                                                   current_node.right_child.payload,
                                                   current_node.right_child.left_child,
                                                   current_node.right_child.right_child)

    def __delitem__(self, key):
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

