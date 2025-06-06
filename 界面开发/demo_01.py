import tkinter as tk
from tkinter import *
import tkinter.messagebox as msgbox

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

# 创建一个menu菜单
main_menu = Menu(root)

file_menu = Menu(main_menu, tearoff=False)
file_menu.add_command(label="打开", accelerator="Ctrl+N")
file_menu.add_command(label="保存")
file_menu.add_separator()
file_menu.add_command(label="退出", command=root.quit)

sub_menu = Menu(file_menu, tearoff=False)
sub_menu.add_checkbutton(label="Python")
sub_menu.add_checkbutton(label="C#")
file_menu.add_cascade(label="喜好", menu=sub_menu)

# 添加子菜单
main_menu.add_cascade(label="文件", menu=file_menu)

root.config(menu=main_menu)


def show_about(event):
    print(help(event))


def clicked():
    print(button.get)
    print("Hello World")


# 创建一个Label
label = Label(root, text="Hello World", font=("微软雅黑", "18", "italic"), fg="red", bg="blue", width=20, height=3,
              wraplength=100, justify="left", anchor="nw")

# 创建一个输入框
entry = Entry(root, width=20)
entry.grid()

# 创建一个按钮
button = Button(root, text="关于", command=lambda: print(entry.get()))
button.grid()

root.bind("<ButtonPress-3>", show_about)
# root.bind("<ButtonPress-3>", show_about)
# root.bind("<Control-Shift-Key-A>", show_about)

# # 创建一个复选框
# var1 = IntVar()
# var2 = IntVar()
# var3 = IntVar()
# checkbox1 = Checkbutton(root, text="Python", variable=var1, onvalue=1, offvalue=0)
# checkbox1.grid()
# checkbox2 = Checkbutton(root, text="C#", variable=var2, onvalue=1, offvalue=0)
# checkbox2.grid()
# checkbox3 = Checkbutton(root, text="我再学python", variable=var3, onvalue=1,
#                         offvalue=0, font=("微软雅黑", "18", "italic"))
# checkbox3.grid()

root.mainloop()  # 消息循环
