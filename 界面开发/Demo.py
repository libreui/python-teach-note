import tkinter as tk
from tkinter import ttk


def button_clicked(item_id):
    print(f"Button clicked for item: {item_id}")


root = tk.Tk()

tree = ttk.Treeview(root, columns=('Size', 'Modified'))
tree.heading('#0', text='Name')
tree.heading('Size', text='Size')
tree.heading('Modified', text='Modified')

# 创建一个滚动条，并与treeview组件关联
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

# 布局
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# 插入数据
tree.insert('', 'end', text='Item 1', values=('1KB', 'Today'))
button = tk.Button(root, text="Click Me", command=lambda: button_clicked('Item 1'))
button.pack()

root.mainloop()
