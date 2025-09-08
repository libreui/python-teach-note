import matplotlib.pyplot as plt
import pandas as pd


file_name = '../db/beijing_tianqi.csv'
df = pd.read_csv(file_name)
df['date'] = pd.to_datetime(df['date'], format="%Y年%m月%d日")
df = df[(df['date'].dt.year == 2014) & (df['date'].dt.month == 5)]

# 最低温度和最高温度之间的中位数
df['temp_median'] = df[['maxTemp', 'minTemp']].median(axis=1)



# 把最高气温和最低气温混合为一个Series类似
# 类似[[2014-5-1, 14],[2014-5-1,26],[2014-5-2,15],[2014-5-2, 28]...]
# 使用 melt 方法将最高气温和最低气温转换为长格式
melted_df = df.melt(id_vars=['date'], value_vars=['maxTemp', 'minTemp'], var_name='temp_type', value_name='temp')


plt.rcParams['font.sans-serif'] = ['SimSong']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots()
fig.set_size_inches(10, 6)
colors = melted_df['temp']

sc1 = ax.scatter(melted_df['date'], melted_df['temp'], c=colors, cmap='spring')
ax.plot(df['date'], df['temp_median'], alpha=0.3)
ax.set_title('2014年5月北京天气')
ax.set_xlabel('日期')
ax.set_ylabel('最高温度')
ax.set_xticks(df['date'])
ax.set_xticklabels(df['date'].dt.strftime("%m-%d"), rotation=45)

plt.colorbar(sc1, label='气温色谱')
plt.grid(alpha=0.2)
plt.show()
