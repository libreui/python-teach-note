import operator

from stack import Stack
from binary_tree import BinaryTree
from tree_traversals import inorder

def build_parse_tree(fp_exp):
    fp_list = fp_exp.split()
    p_stack = Stack()
    e_tree = BinaryTree("")
    p_stack.push(e_tree)
    current_tree = e_tree

    for i in fp_list:
        if i == "(":
            current_tree.insert_left('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in '+-*/)':
            current_tree.set_root_val(eval(i))
            parent = p_stack.pop()
            current_tree = parent
        elif i in '+-*/':
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ")":
            current_tree = p_stack.pop()
        else:
            raise ValueError("Unknown operator: {}".format(i))
    return e_tree


def evaluate(parse_tree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    left_child = parse_tree.get_left_child()
    right_child = parse_tree.get_right_child()

    if left_child and right_child:
        fn = opers[parse_tree.get_root_val()]
        return fn(evaluate(left_child), evaluate(right_child))
    else:
        return parse_tree.get_root_val()

def postorder_reval(tree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    res1 = None
    res2 = None

    if tree:
        res1= postorder_reval(tree.get_left_child())
        res2 = postorder_reval(tree.get_right_child())
        if res1 and res2:
            return opers[tree.get_root_val()](res1, res2)
        else:
            return tree.get_root_val()

def print_exp(tree):
    s_val = ""
    if tree:
        s_val = "(" + print_exp(tree.get_left_child())
        s_val = s_val + str(tree.get_root_val())
        s_val = s_val + print_exp(tree.get_right_child()) + ")"
    return s_val

if __name__ == '__main__':
    pt = build_parse_tree("( ( 10 + 5 ) * 3 )")
    print(evaluate(pt))

    print(postorder_reval(pt))

    x = BinaryTree('*')
    x.insert_left('+')
    l = x.get_left_child()
    l.insert_left(4)
    l.insert_right(5)
    x.insert_right(7)

    print(print_exp(x))
    print(postorder_reval(x))


