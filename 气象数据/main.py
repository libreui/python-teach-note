
'''
Description  : 
Version      : V1.0.0
Author       : Libre Gu 
Date         : 2023-09-11 21:47:20
LastEditors  : Libre Gu 
LastEditTime : 2023-09-11 22:18:37
FilePath     : main.py
Copyright 2023 Libre, All Rights Reserved. 
2023-09-11 21:47:20
'''
####################################
# 如果那你的python环境没有安装openpyxl:#
# 执行：pip install openpyxl        #
####################################
from openpyxl import load_workbook

# 定义文件地址 电脑上数据文件的绝对位置 e.g: (windwos)C:\data\xxxx.xlsx
filePath = "/Users/libre1/Code/PythonJupyter/气象数据/data/20230329/Cloud20230329_111209to20230329_111511.xlsx"
# 打开文件
excel = load_workbook(filePath, read_only=True)
# 打开Sheet
sheet = excel.active
# 获取所有行
rows = sheet.rows
# 获取表头
headers = [cell.value for cell in next(rows)]
# 创建空数据集合
all_rows = []
# 填充数据
for row in rows:
    # 创建一个空字典
    data = {}
    for title, cell in zip(headers, row):
        data[title] = cell.value
    #把当前行字典装入数据集
    all_rows.append(data)
# 打印
print(all_rows)
