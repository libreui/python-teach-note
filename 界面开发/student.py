import tkinter as tk
import tkinter.filedialog as tkFileDialog
import csv

window = tk.Tk()
window.title('学生信息管理系统')

WIDTH = 600
HEIGHT = 400

window.geometry('%dx%d' % (WIDTH, HEIGHT))

# 表头
tableHeader = ['班级', '姓名', '年龄', '性别']


def new_file():
    """新建CSV文件"""
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


def open_file():
    """打开CSV文件"""
    file_path = tkFileDialog.askopenfilename(
        title="打开文件",
        filetypes=[('CSV', '*.csv')],
        initialdir='./'
    )
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()


def save_file():
    """保存CSV文件"""
    pass

def save_as():
    """另存为CSV文件"""
    pass




menubar = tk.Menu(window)

# 创建一个名字是"file"的下拉菜单，其中包括"打开"、"保存"和"退出"三个子菜单, 退出前面要有分割线，每个项目有快捷键
fileMenu = tk.Menu(menubar, tearoff=False)
fileMenu.add_command(label="新建...", command=lambda: new_file())
fileMenu.add_command(label="打开...", command=lambda: open_file())
fileMenu.add_command(label="保存", command=lambda: save_file())
fileMenu.add_command(label="另存为...", command=lambda: save_as())
fileMenu.add_separator()
fileMenu.add_command(label="退出", command=window.quit)

# 将"file"和"edit"菜单添加到"menubar"菜单中
menubar.add_cascade(label="文件", menu=fileMenu)

# 显示菜单
window.config(menu=menubar)

tk.mainloop()
