import tkinter as tk
from tkinter import messagebox

pwd = [
    ("admin", "123456"),
    ("user", "123456")
]

root = tk.Tk()
root.geometry("250x130")
root.title("wow~")

container = tk.Frame(root)
container.pack(expand=True)

name_var = tk.StringVar()
pwd_var = tk.StringVar()


def login_success():
    # 弹出登录成功的对话框
    tk.messagebox.showinfo("提示",
                           "登录成功", icon=messagebox.INFO)


def login_failed():
    tk.messagebox.showinfo("提示",
                           "账号密码错误", icon=messagebox.ERROR)


def on_login():
    username = name_var.get()
    password = pwd_var.get()
    is_login = False  # 是否登陆成功
    for u, p in pwd:
        if username == u and password == p:
            is_login = True
            break
    if is_login:
        login_success()
    else:
        login_failed()


def on_cancel():
    name_var.set("")
    pwd_var.set("")


tk.Label(container, text="登陆界面").grid(row=0, column=0, columnspan=3)
tk.Label(container, text="账号:").grid(row=1, column=0)
tk.Label(container, text="密码:").grid(row=2, column=0)
tk.Entry(container, textvariable=name_var).grid(row=1, column=1, columnspan=2)
# 密码输入框
tk.Entry(container, textvariable=pwd_var, show="*").grid(row=2, column=1, columnspan=2)

tk.Button(container, text="确定", command=on_login).grid(row=3, column=1)
tk.Button(container, text="取消", command=on_cancel).grid(row=3, column=2)

root.mainloop()
