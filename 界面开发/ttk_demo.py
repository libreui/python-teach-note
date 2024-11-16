import ttkbootstrap as ttk
from ttkbootstrap.constants import *

window = ttk.Window(
    title='ttkbootstrap',
    themename='minty',
    size=(600, 400),
    resizable=None,
    position=(500, 300),
    alpha=1.0,
    minsize=(400, 300),
    maxsize=(1920, 1080),
)

ttk.Button(window, text='按钮', bootstyle=SUCCESS).grid(padx=10, pady=10)
ttk.Button(window, text='按钮', bootstyle=INFO).grid(padx=10, pady=10)
ttk.Button(window, text='按钮', bootstyle=INFO).grid(padx=10, pady=10)
ttk.Button(window, text='按钮', bootstyle=INFO).grid(padx=10, pady=10)


window.mainloop()
