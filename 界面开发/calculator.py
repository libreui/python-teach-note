import tkinter as tk

window = tk.Tk()
# window.geometry("300x300")
window.resizable(False, False)

# 计算的得数
eqNum = 0

value = tk.StringVar()
tk.Entry(window, width=10, font=("楷体", 30), textvariable=value, justify=tk.RIGHT).grid(row=0, columnspan=4)
value.set("0")


def callback(arg):
    """按钮点击"""
    value.set(str(arg))
    # TODO 记录点击的按钮数字还是符号，入栈
    # 如果是数字累计，直到按下了一个符号
    # 如果是等号，就计算结果


def clear():
    """清空计算"""
    pass


def setSymbol():
    """设置符号"""
    pass


def setPercent():
    """设置百分比结果"""
    pass


tk.Button(window, text="AC", command=clear).grid(row=1, column=0, sticky=tk.EW)

tk.Button(window, text="+/-", command=setSymbol).grid(row=1, column=1, sticky=tk.EW)
tk.Button(window, text="%", command=setPercent).grid(row=1, column=2, sticky=tk.EW)

btnDiv = tk.Button(window, text="÷")
btnDiv.config(command=lambda: callback("-"))
btnDiv.grid(row=1, column=3, sticky=tk.EW)

btn7 = tk.Button(window, text="7")
btn7.config(command=lambda: callback(7))
btn7.grid(row=2, column=0, sticky=tk.EW)

btn8 = tk.Button(window, text="8")
btn8.config(command=lambda: callback(8))
btn8.grid(row=2, column=1, sticky=tk.EW)

btn9 = tk.Button(window, text="9")
btn9.config(command=lambda: callback(9))
btn9.grid(row=2, column=2, sticky=tk.EW)

btnX = tk.Button(window, text="×")
btnX.config(command=lambda: callback("x"))
btnX.grid(row=2, column=3, sticky=tk.EW)

btn4 = tk.Button(window, text="4")
btn4.config(command=lambda: callback(4))
btn4.grid(row=3, column=0, sticky=tk.EW)

btn5 = tk.Button(window, text="5")
btn5.config(command=lambda: callback(5))
btn5.grid(row=3, column=1, sticky=tk.EW)

btn6 = tk.Button(window, text="6")
btn6.config(command=lambda: callback(6))
btn6.grid(row=3, column=2, sticky=tk.EW)

btnSub = tk.Button(window, text="-")
btnSub.config(command=lambda: callback("-"))
btnSub.grid(row=3, column=3, sticky=tk.EW)

btn1 = tk.Button(window, text="1")
btn1.config(command=lambda: callback(1))
btn1.grid(row=4, column=0, sticky=tk.EW)

btn2 = tk.Button(window, text="2")
btn2.config(command=lambda: callback(2))
btn2.grid(row=4, column=1, sticky=tk.EW)

btn3 = tk.Button(window, text="3")
btn3.config(command=lambda: callback(3))
btn3.grid(row=4, column=2, sticky=tk.EW)

btnPlus = tk.Button(window, text="+")
btnPlus.config(command=lambda: callback("+"))
btnPlus.grid(row=4, column=3, sticky=tk.EW)

btn0 = tk.Button(window, text="0")
btn0.config(command=lambda: callback(0))
btn0.grid(row=5, column=0, columnspan=2, ipadx=26, sticky=tk.EW)

btnDot = tk.Button(window, text=".")
btnDot.config(command=lambda: callback("."))
btnDot.grid(row=5, column=2, ipadx=3, sticky=tk.EW)

btnEq = tk.Button(window, text="=")
btnEq.config(command=lambda: callback("="))
btnEq.grid(row=5, column=3, sticky=tk.EW)

window.mainloop()
