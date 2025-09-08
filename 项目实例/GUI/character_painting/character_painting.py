import time
import tkinter as tk
from tkinter import filedialog, LEFT, NW, ttk

from PIL import Image, ImageTk
import numpy as np

from conversion import picture_conversion

img_tk = ""
img_show_tk = ""
file_path = ""

root = tk.Tk()

WIDTH = 600
HEIGHT = 250

root.title('字符画')
root.geometry('%dx%d' % (WIDTH, HEIGHT))

# 创建一个画布
CANVAS_SIZE = 250
canvas = tk.Canvas(root, width=CANVAS_SIZE, height=CANVAS_SIZE)
canvas.pack(side=LEFT, anchor=NW)

# 创建一个画布
CANVAS_SIZE = 250
canvas_show = tk.Canvas(root, width=CANVAS_SIZE, height=CANVAS_SIZE)
canvas_show.pack(side=tk.RIGHT, anchor=NW)


# 创建一个显示图片的控件 图片等比例到250*250
def open_file():
    global img_tk, file_path
    # 使用openfile加载图片
    default_path = './input_img/cat.jpg'
    file_path = tk.filedialog.askopenfilename(title="打开图片",
                                              filetypes=[('JPG', '*.jpg'), ('PNG', '*.png')],
                                              initialdir=default_path)

    img = Image.open(file_path)
    img_width, img_height = img.size
    ratio = min(CANVAS_SIZE/img_width, CANVAS_SIZE/img_height)

    # 计算缩放后的尺寸
    new_width = int(img_width * ratio)
    new_height = int(img_height * ratio)
    img_resize = img.resize((new_width, new_height))
    img_tk = ImageTk.PhotoImage(img_resize)

    canvas.create_image(CANVAS_SIZE//2, CANVAS_SIZE//2, image=img_tk)


# 创建一个按钮用来打开文件
button = tk.Button(root, text='打开图片', command=open_file)
button.pack(side=tk.TOP, anchor=NW)

# 创建一个文本框用来输入字符画的字符
text = tk.Text(root, width=10, height=5)
text.pack(side=tk.TOP, anchor=NW)

# 创建一个下拉菜单用来选择清晰度[清晰, 一般, 字符]
combo = tk.ttk.Combobox(root, values=['清晰', '一般', '字符'])
# 默认值
combo.current(0)
# 宽度
combo['width'] = 6
combo.pack(side=tk.TOP, anchor=NW)


def refresh():
    global img_show_tk
    t = str(time.time())
    export_path = './export_img/' + t + '.png'
    # 获取文本框字符
    input_char = text.get("1.0", tk.END).strip()
    # 获取下拉菜单的值
    pix_distance = combo.get()
    # 调用图片转换函数
    is_over = picture_conversion(file_path, export_path, input_char, pix_distance)
    if is_over:
        # 打开图片
        img = Image.open(export_path)
        img_width, img_height = img.size
        ratio = min(CANVAS_SIZE / img_width, CANVAS_SIZE / img_height)
        # 计算缩放后的尺寸
        new_width = int(img_width * ratio)
        new_height = int(img_height * ratio)
        img_resize = img.resize((new_width, new_height))
        img_show_tk = ImageTk.PhotoImage(img_resize)
        canvas_show.create_image(CANVAS_SIZE // 2, CANVAS_SIZE // 2, image=img_show_tk)


# 创建一个转换ImageButton
image_button = tk.Button(root, command=refresh)
# 按钮图片
image_button_img = Image.open('./img/refresh.png')
image_button_img = image_button_img.resize((40, 40))
image_button_img = ImageTk.PhotoImage(image_button_img)
image_button.config(image=image_button_img, compound=tk.LEFT, padx=5, pady=5, width=50, height=50)
image_button.pack(side=tk.TOP, anchor=NW)

# 消息循环
root.mainloop()
