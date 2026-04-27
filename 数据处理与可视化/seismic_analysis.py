import pandas as pd
import matplotlib.pyplot as plt

file_name = "./data/dizhen-2025.xls"
df = pd.read_excel(file_name, sheet_name="速报目录")
data = df.iloc[:100, 5]

print(data)
x = df.iloc[:100, 1]
fig, ax = plt.subplots()
# 设置y轴范围
ax.set_ybound(0, 50)
ax.plot(x, data)
plt.show()
