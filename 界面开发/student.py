import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.filedialog as tkFileDialog
import csv

# 当前打开的文件路径
current_csv_path = ''

window = tk.Tk()
window.title('studentsystem')

WIDTH = 600
HEIGHT = 400

window.geometry('%dx%d' % (WIDTH, HEIGHT))
window.resizable(False, False)

tableHeader = ('班级', '姓名', '年龄', '性别')


def new_file():
    """新建CSV文件"""
    global current_csv_path
    # 弹出新建文件名对话框
    file_name = tkFileDialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")],
        initialdir='./'
    )
    if file_name:
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(tableHeader)
        # 打开新文件
        current_csv_path = file_name
    print("当前文件：", current_csv_path)


def open_file():
    """打开CSV文件"""
    global current_csv_path
    file_path = tkFileDialog.askopenfilename(
        title="打开文件",
        filetypes=[('CSV', '*.csv')],
        initialdir='./'
    )
    if file_path:
        with open(file_path, 'r') as file:
            content = list(csv.reader(file))
    # 将文件写入treeview
    if len(content) > 1:
        insertTreeView(content)
    else:
        messagebox.showerror("错误", "文件内容为空")

    current_csv_path = file_path

    print("当前文件：", current_csv_path)


def insertTreeView(content):
    """输入内容到treeview中"""
    # 删除所有数据
    treeview.delete(*treeview.get_children())

    for i in range(len(content)-1):
        treeview.insert('', END, values=[i] + content[i+1])


def save_file():
    """保存CSV文件"""
    if len(treeview.get_children()) == 0:
        messagebox.showinfo("提示", "没有数据需要保存")
        return

    data = [treeview.item(i)["values"][1:] for i in treeview.get_children()]
    if current_csv_path:
        with open(current_csv_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(tableHeader)
            writer.writerows(data)
        messagebox.showinfo("提示", "保存成功")
        print("保存文件成功")


def save_as():
    """另存为CSV文件"""
    # treeview_data = [treeview.item(i)["values"] for i in treeview.get_children()]
    for i in treeview.get_children():
        item = treeview.item(i)
        print(item["values"])
    pass


def delete_selected():
    select_item = treeview.selection()
    for item in select_item:
        treeview.delete(item)
    treeview.pack()


def add_student():

    if current_csv_path == '':
        messagebox.showinfo("提示", "请先打开或新建一个CSV文件")
        return

    new_win = tk.Toplevel()
    new_win.title("添加学生信息")
    new_win.geometry("300x200")
    new_win.resizable(False, False)

    # 创建输入框
    tk.Label(new_win, text="班级:").place(x=10, y=10)
    tk.Label(new_win, text="姓名:").place(x=10, y=40)
    tk.Label(new_win, text="年龄:").place(x=10, y=70)
    tk.Label(new_win, text="性别:").place(x=10, y=100)

    class_entry = tk.Entry(new_win)
    class_entry.place(x=100, y=10)

    name_entry = tk.Entry(new_win)
    name_entry.place(x=100, y=40)

    age_entry = tk.Entry(new_win)
    age_entry.place(x=100, y=70)

    sex_entry = tk.Entry(new_win)
    sex_entry.place(x=100, y=100)

    # 创建确认按钮
    confirm_btn = tk.Button(new_win, text="确认", command=lambda: add_student_info(class_entry.get(), name_entry.get(), age_entry.get(), sex_entry.get()))
    confirm_btn.place(x=100, y=130)

    def add_student_info(class_name, name, age, sex):
        # 获取当前行数
        current_row = len(treeview.get_children())
        # 插入数据
        treeview.insert('', END, values=(current_row, class_name, name, age, sex))
        new_win.destroy()





menubar = tk.Menu(window)

# 创建一个名字是"res"的下拉菜单，其中包括"打开"、"保存"和"退出"三个子菜单, 退出前面要有分割线，每个项目有快捷键
fileMenu = tk.Menu(menubar, tearoff=False)
fileMenu.add_command(label="新建...", command=lambda: new_file())
fileMenu.add_command(label="打开...", command=lambda: open_file())
fileMenu.add_command(label="保存", command=lambda: save_file())
fileMenu.add_command(label="另存为...", command=lambda: save_as())
fileMenu.add_separator()
fileMenu.add_command(label="退出", command=window.quit)

# 将"res"和"edit"菜单添加到"menubar"菜单中
menubar.add_cascade(label="文件", menu=fileMenu)

# 显示菜单
window.config(menu=menubar)


frame = tk.Frame(window)
frame.place(x=0, y=40, width=WIDTH, height=HEIGHT-40)
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# treeview
treeview = ttk.Treeview(
    frame,
    columns=("id", "class", "name", "age", "sex"),
    show='headings',
    yscrollcommand=scrollbar.set
)

treeview.column('id', width=30, stretch=NO)
treeview.column('class', width=114, anchor=W)
treeview.column('name', width=114, anchor=W)
treeview.column('age', width=114, anchor=W)
treeview.column('sex', width=114, anchor=W)

# 表头 ('班级', '姓名', '年龄', '性别')
treeview.heading('id', text="编号")
treeview.heading('class', text="班级")
treeview.heading('name', text="姓名")
treeview.heading('age', text="年龄")
treeview.heading('sex', text="性别")


treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
# 绑定表格滚动条
scrollbar.config(command=treeview.yview)

# 创建添加按钮
btnAdd = tk.Button(window, text="添加", command=add_student)
btnAdd.pack(side=LEFT, anchor=NW)

# 创建删除按钮
btnDelete = tk.Button(window, text="删除", command=delete_selected)
btnDelete.pack(side=LEFT, anchor=NW)


tk.mainloop()
