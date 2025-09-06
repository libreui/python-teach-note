# 统计 2014-2024年 每年 气温在30度以上的天数
# 统计 2014-2024年 每年 气温在-10度以下的天数
# 放置到两张柱状图上
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../db/beijing_tianqi.csv')
df['date'] = pd.to_datetime(df['date'], format='%Y年%m月%d日')
df['year'] = df['date'].dt.year
max_temp_count = df[df['maxTemp'] > 30].groupby('year').size()
min_temp_count = df[df['minTemp'] < -10].groupby('year').size()

# 保持max_temp_count和min_temp_count的索引一致
max_temp_count = max_temp_count.reindex(range(2014, 2025), fill_value=0)
min_temp_count = min_temp_count.reindex(range(2014, 2025), fill_value=0)

plt.rcParams['font.sans-serif'] = ['SimSong']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(2, 1)
fig.set_size_inches(10, 6)
# 子图间距
plt.subplots_adjust(hspace=0.5)
# 子图标题
fig.suptitle('2014-2024年 气温在30度以上和-10度以下的天数')
ax[0].bar(max_temp_count.index, max_temp_count.values)
ax[1].bar(min_temp_count.index, min_temp_count.values)
ax[0].set_title('2014-2024年 气温在30度以上的天数')
ax[1].set_title('2014-2024年 气温在-10度以下的天数')
ax[0].set_xlabel('年份')
ax[1].set_xlabel('年份')
ax[0].set_ylabel('天数')
ax[1].set_ylabel('天数')

# 年份刻度
ax[0].set_xticks(max_temp_count.index)
ax[1].set_xticks(min_temp_count.index)
# 年份刻度标签
ax[0].set_xticklabels(max_temp_count.index)
ax[1].set_xticklabels(min_temp_count.index)
plt.show()
