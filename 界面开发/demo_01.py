import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox

# 初始化类库
root = tk.Tk()
# 使窗口居中
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
w = width // 2 - 200
h = height // 2 - 150
root.geometry(f"600x400+{w}+{h}")
root.title("Login")
# 是否可以缩放
root.resizable(False, False)
# 是否允许最大化
root.maxsize(800, 600)
root.minsize(400, 300)


# 创建一个单选按钮
v = tk.IntVar()
v.set(0)
Radiobutton(root, text="One", variable=v, value=1).grid()
Radiobutton(root, text="Two", variable=v, value=2).grid()
Radiobutton(root, text="Three", variable=v, value=3).grid()



root.mainloop() # 消息循环
