# 相对路径、绝对路径

"""
路径：
    绝对路径：从根目录开始，例如：C:\Users\Administrator\Desktop\test.txt
    相对路径：相对于当前目录的路径，例如：./file/user.csv
    相对路径：相对于当前目录的路径，例如：../file/user.csv
模式：
    r 只读，如果文件不存在则报错
    w 只写，如果文件不存在则创建，如果文件存在则清空
    a 追加，如果文件不存在则创建，如果文件存在则在文件末尾追加
    r+ 读写，如果文件不存在则报错
    w+ 读写，如果文件不存在则创建，如果文件存在则清空
编码：
    encoding="utf-8" 指定编码格式，默认编码格式为系统默认编码格式
"""
f = open("./file/user.csv", "r", encoding="utf-8")