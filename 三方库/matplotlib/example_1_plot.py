import matplotlib.pyplot as plt
import pandas as pd

start_year = 2014
end_year = 2024
file_name = "../db/beijing_tianqi.csv"
df = pd.read_csv(file_name)
df['date'] = pd.to_datetime(df['date'], format="%Y年%m月%d日")
df['year'] = df['date'].dt.year
# 每年最高气温平均值计算
filter_df = df[(df['date'].dt.year >= start_year) & (df['date'].dt.year <= end_year)]
avg_min_temp = filter_df.groupby('year')['minTemp'].mean().round(2)
avg_max_temp = filter_df.groupby('year')['maxTemp'].mean().round(2)


plt.rcParams['font.family'] = ['SimSong']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots()
fig.set_size_inches((10, 6))
ax.plot(avg_min_temp, 'b.-')
ax.plot(avg_max_temp, 'r.-')
ax.set_xticks(avg_min_temp.index)

ax.set_title(f"{start_year}年至{end_year}年北京天气")
ax.set_xlabel("年份")
ax.set_ylabel("温度(℃)")
ax.legend(['最低平均温度', '最高平均温度'])
plt.grid(alpha=0.3)
plt.show()
