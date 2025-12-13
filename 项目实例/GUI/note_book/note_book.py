from tkinter import *
from tkinter import filedialog

main_window = Tk()
main_window.geometry("800x600")
main_window.title("Note Book - by Libre")

# 当前文件保存路径
save_path = ""


def save(file_path, content):
    global save_path
    if file_path:
        # 写入文件
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
            # 更新保存路径
            save_path = file_path


def open_save_dialog():
    return filedialog.asksaveasfilename(defaultextension=".txt",
                                        initialdir="~/Desktop",
                                        filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")])


# 保存文档
def save_file():
    file_path = save_path

    # 获取文本输入框中的内容
    content = txt_area.get("1.0", END)
    # 打开文件对话框，选择保存路径
    if save_path == "":
        file_path = open_save_dialog()

    print(f"file_path: {file_path}")
    save(file_path, content)


def save_other_file():
    # 获取文本输入框中的内容
    content = txt_area.get("1.0", END)
    # 打开文件对话框，选择保存路径
    file_path = open_save_dialog()

    print(f"file_path: {file_path}")
    save(file_path, content)


def new_file():
    global save_path
    save_path = ""
    txt_area.delete("1.0", END)
    save_other_file()


menu = Menu(main_window)

file_menu = Menu(menu, tearoff=False)
file_menu.add_command(label="新建...", command=new_file, accelerator="Command+n")
file_menu.add_command(label="打开")
file_menu.add_command(label="保存", command=save_file, accelerator="Command+S")
file_menu.add_command(label="另存为...", command=save_other_file, accelerator="Command+Shift+S")
file_menu.add_separator()
file_menu.add_command(label="退出")
menu.add_cascade(label="文件", menu=file_menu)

edit_menu = Menu(menu, tearoff=False)
edit_menu.add_command(label="撤销")
edit_menu.add_command(label="重做")
edit_menu.add_separator()
edit_menu.add_command(label="剪切")
edit_menu.add_command(label="复制")
edit_menu.add_command(label="粘贴")
edit_menu.add_separator()
edit_menu.add_command(label="删除")
edit_menu.add_command(label="全选")
menu.add_cascade(label="编辑", menu=edit_menu)

main_window.config(menu=menu)

root = Frame(main_window)
# 填满整个窗口
root.pack(fill=BOTH, expand=True)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# 文本输入填满整个窗口
txt_area = Text(root, bg="white", fg="black", font=("宋体", 12))
# txt_area.insert(END, "Hello World!")
# txt_area.insert(2.0, "OK!")
txt_area.grid(row=0, column=0, sticky=NSEW)

# 设置保存按钮的快捷键为 Ctrl+S
main_window.bind("<Command-n>", lambda event: new_file())
main_window.bind("<Command-s>", lambda event: save_file())
main_window.bind("<Command-S>", lambda event: save_other_file())

main_window.mainloop()
