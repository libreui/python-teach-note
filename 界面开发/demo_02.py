import tkinter as tk
from tkinter.ttk import Treeview


# 创建主窗口
root = tk.Tk()
# 设置窗口标题
root.title("列表窗口")
# 设置窗口大小
root.geometry("800x600")

# 创建列表框
treeview = Treeview(root, columns=("id", "name", "age", "sex", "class"), show="headings")
treeview.grid(row=0, column=0, sticky="nsew")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# 设置表头
treeview.heading("id", text="ID")
treeview.heading("name", text="姓名", anchor=tk.W)
treeview.heading("age", text="年龄")
treeview.heading("sex", text="性别")
treeview.heading("class", text="班级")

# 设置列的属性
treeview.column("id", width=50, anchor="center")
treeview.column("name", width=100, anchor=tk.W)
treeview.column("age", width=50, anchor="center")

# 插入数据
data_1 = ("1", "张三", "18", "男", "一班")
data_2 = ["2", "李四", "19", "女", "二班"]
data_3 = ("3", "王五", "20", "男", "三班")
treeview.insert("", "end", values=data_1)
treeview.insert("", "end", values=data_2)
treeview.insert("", "end", values=data_3)


root.mainloop()

