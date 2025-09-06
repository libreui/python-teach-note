import matplotlib.pyplot as plt
import pandas as pd

years = [2014, 2015]
df = pd.read_csv("../db/beijing_tianqi.csv")
df['date'] = pd.to_datetime(df['date'], format="%Y年%m月%d日")
df_2014 = df[(df['date'].dt.year == 2014)]
df_2015 = df[(df['date'].dt.year == 2015)]

plt.rcParams['font.family'] = ['SimSong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.titlesize'] = 16
plt.rcParams['figure.subplot.wspace'] = 0.3
plt.rcParams['figure.subplot.hspace'] = 0.3

fig, ax = plt.subplots(2, 1)
fig.set_size_inches((12, 8))

ax[0].plot(df_2014['date'].dt.strftime("%m-%d"), df_2014['minTemp'], 'b')
ax[0].plot(df_2014['date'].dt.strftime("%m-%d"), df_2014['maxTemp'], 'r')
ax[0].set_title(f"2014年北京天气")
ax[0].set_xlabel("日期")
ax[0].set_ylabel("温度(℃)")
ax[0].legend(['最低温度', '最高温度'])

ax[1].plot(df_2015['date'].dt.strftime("%m-%d"), df_2015['minTemp'], 'b')
ax[1].plot(df_2015['date'].dt.strftime("%m-%d"), df_2015['maxTemp'], 'r')
ax[1].set_title(f"2015年北京天气")
ax[1].set_xlabel("日期")
ax[1].set_ylabel("温度(℃)")
ax[1].legend(['最低温度', '最高温度'])


# 定义函数设置每 10 天一个刻度
def set_10_day_ticks(ax, df):
    # 获取日期数据
    dates = df['date'].dt.strftime("%m-%d").tolist()
    # 每 10 天选取一个日期
    tick_indices = list(range(0, len(dates), 10))
    tick_labels = [dates[i] for i in tick_indices]
    # 设置 x 轴刻度和标签
    ax.set_xticks(tick_indices)
    ax.set_xticklabels(tick_labels, rotation=45)


# 为两个子图设置刻度
set_10_day_ticks(ax[0], df_2014)
set_10_day_ticks(ax[1], df_2015)

plt.suptitle("2014年至2015年北京天气")
plt.show()
