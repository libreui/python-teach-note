# 统计2023年日间天气情况比例，夜间天气情况比例
# 饼图练习
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../db/beijing_tianqi.csv')
df['date'] = pd.to_datetime(df['date'], format='%Y年%m月%d日')
df = df[df['date'].dt.year == 2023].copy()
# 统计2023年日间天气情况比例，夜间天气情况比例
weather_day_df = df.groupby('weatherDay').size()
weather_night_df = df.groupby('weatherNight').size()

plt.rcParams['font.sans-serif'] = ['SimSong']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(1, 2)
fig.set_size_inches(12, 8)
# 子图间距
plt.subplots_adjust(wspace=0.5)
fig.suptitle('2023年 天气情况比例', fontsize=16)


# 定义过滤小占比的函数
def filter_small_percentages(data, threshold=2):
    percentages = data / data.sum() * 100
    small_data = data[percentages < threshold]
    large_data = data[percentages >= threshold]
    if not small_data.empty:
        large_data = pd.concat([large_data, pd.Series(small_data.sum(), index=['其他'])])
    return large_data


# 过滤小占比数据
weather_day_filtered = filter_small_percentages(weather_day_df)
weather_night_filtered = filter_small_percentages(weather_night_df)

# 设置饼图参数
pctdistance = 0.8
labeldistance = 1.1
explode = [0.02] * len(weather_day_filtered)
wedgeprops = {'linewidth': 1, 'edgecolor': 'black'}

# 绘制日间天气饼图
patches, texts, autotexts = ax[0].pie(
    weather_day_filtered,
    labels=weather_day_filtered.index,
    autopct='%1.1f%%',
    pctdistance=pctdistance,
    labeldistance=labeldistance,
    explode=explode,
    wedgeprops=wedgeprops
)
# 设置日间天气饼图文字大小
for text in texts + autotexts:
    text.set_fontsize(8)

# 绘制夜间天气饼图
patches, texts, autotexts = ax[1].pie(
    weather_night_filtered,
    labels=weather_night_filtered.index,
    autopct='%1.1f%%',
    pctdistance=pctdistance,
    labeldistance=labeldistance,
    explode=explode,
    wedgeprops=wedgeprops
)
# 设置夜间天气饼图文字大小
for text in texts + autotexts:
    text.set_fontsize(8)

ax[0].set_title('2023年 日间天气情况比例', fontsize=12)
ax[1].set_title('2023年 夜间天气情况比例', fontsize=12)

plt.show()
