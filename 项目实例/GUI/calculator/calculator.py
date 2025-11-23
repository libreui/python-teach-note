from tkinter import *
from tkinter import StringVar

root = Tk()
# root.geometry('300x300')
root.title('计算器')
root.resizable(False, False)

value_a = None  # 加法操作数a
value_b = None  # 加法操作数b
operator = None # 运算符
operator_count = 0  # 运算符数量
is_continue = True
values = [] # 操作数栈
is_calculating = False # 是否正在计算中


# 栈的数据结构 FILO
def new_on_operator(op):
    global operator, is_continue, is_calculating

    print(values, operator)
    v = entry_str.get()
    # 如果不是正在计算中，将当前输入框内容保存到栈中
    if not is_calculating:
        # 如果是第一次按符号键，将当前输入框内容保存到栈中
        values.append(v)
        entry_str.set('0')

    if len(values) == 1 and op != '=':
        operator = op
    elif len(values) >= 2:
        is_calculating = True # 正在计算中

        if not operator:
            operator = op

        val_a = values.pop()
        val_b = values.pop()
        tmp = eval(val_b + operator + val_a)
        values.append(str(tmp))
        entry_str.set(str(tmp))

        if op == '=':
            operator = None
        else:
            operator = op

    print(values, operator)


def on_clicked(text):
    """处理按钮点击事件，更新输入框显示"""
    global is_continue, operator_count, value_b, value_a, operator, is_calculating
    print(f'点击了按钮:{text}')

    if text in "+-*/=":
        is_continue = False
        new_on_operator(text)
        return

    # 如果没有运算符，但是输入了数字，清空栈
    if not operator and len(values) > 0:
        values.clear()

    operator_count = 0
    is_calculating = False  # 计算结束
    t = '' if entry_str.get() == '0' else entry_str.get()
    if is_continue:
        entry_str.set(t + text)
    else:
        entry_str.set(text)
        is_continue = True


# 输入框
entry_str = StringVar()
entry_str.set('0')
entry = Entry(root, textvariable=entry_str, width=15, font=("楷体", 40), justify=RIGHT)
# 沾满横向空间
entry.grid(row=0, column=0, columnspan=4)

# 按钮
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]
for i, button in enumerate(buttons):
    row = i // 4 + 1
    col = i % 4
    Button(root, text=button,
           width=3, height=2,
           font=("楷体", 30),
           command=lambda text=button: on_clicked(text)).grid(row=row, column=col)

Button(root, text='C', height=2,
       font=("楷体", 30),
       command=lambda: entry_str.set('0')).grid(row=5, column=0, columnspan=4, sticky=EW)

root.mainloop()
