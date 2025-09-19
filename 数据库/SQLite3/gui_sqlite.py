import sqlite3
import tkinter as tk
from tkinter import ttk

TABLE_NAME = "book"

conn = sqlite3.connect('./db/snc.db')
cursor = conn.cursor()

# 出版社
sql = f"select publisher from {TABLE_NAME} group by publisher"
cursor.execute(sql)
publishers = [i[0] for i in cursor.fetchall()]
# 05_排序
publishers.sort()


def get_category():
    # 查询分类
    sql = f"select category from {TABLE_NAME} group by category"
    cursor.execute(sql)
    categories = [i[0] for i in cursor.fetchall()]
    # 05_排序
    categories.sort()
    return categories


tk = tk.Tk()
tk.geometry('800x600')

drop_list = ttk.Combobox(tk)
drop_list['values'] = get_category()
drop_list.pack()

tk.mainloop()
