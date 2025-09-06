import matplotlib.pyplot as plt
import pandas as pd

# 读取数据
df = pd.read_csv("../db/beijing_tianqi.csv")
df['date'] = pd.to_datetime(df['date'], format="%Y年%m月%d日")

# 假设最高温度列名为 high_temp，根据实际情况修改
high_temp = df['maxTemp']

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimSong']
# 解决负号显示问题
plt.rcParams['axes.unicode_minus'] = False

# 绘制最高温度直方图
# plt.figure(figsize=(10, 6))
n, bins, patches = plt.hist(high_temp, bins=20, edgecolor='black', alpha=0.7)

# 添加数据标签
for i in range(len(patches)):
    plt.text(bins[i]+0.5, n[i], str(int(n[i])), ha='center')

# 设置图表标题和坐标轴标签
plt.title('最高温度分布直方图')
plt.xlabel('最高温度')
plt.ylabel('频次')

# 显示图表
plt.show()
