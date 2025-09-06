import matplotlib.pyplot as plt
import pandas as pd

year = 2020
month = 2
file_name = "../db/beijing_tianqi.csv"
df = pd.read_csv(file_name)

df['date'] = pd.to_datetime(df['date'], format="%Y年%m月%d日")
df = df[(df['date'].dt.year == year) & (df['date'].dt.month == month)]
# 只显示月日
x = df['date'].dt.strftime("%d")
y = df['minTemp']
y2 = df['maxTemp']

plt.rcParams['font.family'] = ['SimSong']
plt.rcParams['axes.unicode_minus'] = False


fig, ax = plt.subplots()
fig.set_size_inches((10, 6))

ax.plot(x, y2, 'r.-', x, y, 'b.-')
ax.set_title(f"{year}年{month}月北京天气")
ax.set_xlabel("日期")
ax.set_ylabel("温度(℃)")
ax.legend(['最高温度', '最低温度'])


# 显示网格，颜色淡一些
plt.grid(alpha=0.3)

plt.show()

'''
[
    ['2020年2月1日', 33,33],
    ['2020年2月2日', 34,32],
    ['2020年2月3日', 35,33],
]
[]
'''

