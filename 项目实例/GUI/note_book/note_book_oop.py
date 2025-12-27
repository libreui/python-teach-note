from tkinter import *
from tkinter import filedialog


class NoteBook(Tk):
    """笔记本应用程序的主类，继承自Tk"""

    def __init__(self):
        """初始化笔记本应用"""
        super().__init__()

        # 设置窗口属性
        self.geometry("800x600")
        self.title("Note Book - by Libre")

        # 当前文件保存路径
        self.save_path = ""

        # 初始化UI组件
        self.setup_ui()

        # 设置快捷键
        self.setup_shortcuts()

    def setup_ui(self):
        """设置用户界面组件"""
        # 创建菜单栏
        self.setup_menu()

        # 创建文本编辑区域
        self.setup_text_area()

    def setup_menu(self):
        """创建菜单栏"""
        # 创建主菜单
        menu = Menu(self)

        # 创建文件菜单
        file_menu = Menu(menu, tearoff=False)
        file_menu.add_command(label="新建...", command=self.new_file, accelerator="Command+n")
        file_menu.add_command(label="打开...", command=self.open_file, accelerator="Command+o")
        file_menu.add_command(label="保存", command=self.save_file, accelerator="Command+S")
        file_menu.add_command(label="另存为...", command=self.save_other_file, accelerator="Command+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="退出", command=self.quit, accelerator="Command+Q")
        menu.add_cascade(label="文件", menu=file_menu)

        # 创建编辑菜单
        edit_menu = Menu(menu, tearoff=False)
        edit_menu.add_command(label="撤销")
        edit_menu.add_command(label="重做")
        edit_menu.add_separator()
        edit_menu.add_command(label="剪切")
        edit_menu.add_command(label="复制")
        edit_menu.add_command(label="粘贴")
        edit_menu.add_separator()
        edit_menu.add_command(label="删除")
        edit_menu.add_command(label="全选", command=self.select_all)
        menu.add_cascade(label="编辑", menu=edit_menu)

        # 设置菜单
        self.config(menu=menu)

    def setup_text_area(self):
        """创建文本编辑区域"""
        # 创建主框架
        root = Frame(self)
        root.pack(fill=BOTH, expand=True)
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        # 创建滚动条
        scrollbar = Scrollbar(root)
        scrollbar.grid(row=0, column=1, sticky=NS)

        # 创建文本区域
        self.txt_area = Text(root, bg="white",
                             fg="black",
                             font=("宋体", 12),
                             yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.txt_area.yview)
        self.txt_area.grid(row=0, column=0, sticky=NSEW)

    def setup_shortcuts(self):
        """设置键盘快捷键"""
        self.bind("<Command-n>", lambda event: self.new_file())
        self.bind("<Command-s>", lambda event: self.save_file())
        self.bind("<Command-S>", lambda event: self.save_other_file())
        self.bind("<Command-o>", lambda event: self.open_file())
        self.bind("<Command-q>", lambda event: self.quit())

    def quit(self):
        """退出应用程序"""
        self.destroy()

    def save(self, file_path, content):
        """保存内容到指定文件路径"""
        if file_path:
            # 写入文件
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
                # 更新保存路径
                self.save_path = file_path

    def open_save_dialog(self):
        """打开保存文件对话框"""
        return filedialog.asksaveasfilename(defaultextension=".txt",
                                            initialdir="~/Desktop",
                                            filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")])

    def save_file(self):
        """保存当前文档"""
        file_path = self.save_path

        # 获取文本输入框中的内容
        content = self.txt_area.get("1.0", END)
        # 打开文件对话框，选择保存路径
        if self.save_path == "":
            file_path = self.open_save_dialog()

        print(f"file_path: {file_path}")
        self.save(file_path, content)

    def open_file(self):
        """打开文件"""
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                self.txt_area.delete("1.0", END)
                self.txt_area.insert(END, content)
                self.save_path = file_path

    def select_all(self):
        """全选文本"""
        self.txt_area.tag_add(SEL, "1.0", END)
        self.txt_area.mark_set(INSERT, END)
        self.txt_area.see(INSERT)

    def save_other_file(self):
        """另存为文件"""
        # 获取文本输入框中的内容
        content = self.txt_area.get("1.0", END)
        # 打开文件对话框，选择保存路径
        file_path = self.open_save_dialog()

        print(f"file_path: {file_path}")
        self.save(file_path, content)

    def new_file(self):
        """新建文件"""
        self.save_path = ""
        self.txt_area.delete("1.0", END)
        self.save_other_file()


if __name__ == "__main__":
    # 创建并运行应用程序
    app = NoteBook()
    app.mainloop()
