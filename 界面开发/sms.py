import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


root = tk.Tk()
root.geometry("600x800")

ttk.Treeview(root, columns=('id', 'title')).pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# 第一行的 Frame
frame_row1 = tk.Frame(root)
frame_row1.pack(side=tk.TOP, fill=tk.X)
txt_address = tk.Label(frame_row1, text="地址：")
txt_address.pack(side=tk.LEFT, anchor=tk.NW)
edit_address = tk.Entry(frame_row1)
edit_address.pack(side=tk.LEFT, anchor=tk.NW)

# 第二行的 Frame
frame_row2 = tk.Frame(root)
frame_row2.pack(side=tk.TOP, fill=tk.X)
txt_phone = tk.Label(frame_row2, text="电话：")
txt_phone.pack(side=tk.LEFT, anchor=tk.NW)
edit_phone = tk.Entry(frame_row2)
edit_phone.pack(side=tk.LEFT, anchor=tk.NW)


tk.mainloop()
