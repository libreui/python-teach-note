from binary_tree import BinaryTree


def preorder(pt):
    if pt:
        print(pt.get_root_val())
        preorder(pt.get_left_child())
        preorder(pt.get_right_child())

def postorder(pt):
    if pt:
        postorder(pt.get_left_child())
        postorder(pt.get_right_child())
        print(pt.get_root_val())

def inorder(pt):
    if pt:
        inorder(pt.get_left_child())
        print(pt.get_root_val())
        inorder(pt.get_right_child())
