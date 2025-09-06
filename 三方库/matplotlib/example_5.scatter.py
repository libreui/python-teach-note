import matplotlib.pyplot as plt
import pandas as pd


file_name = '../db/beijing_tianqi.csv'
df = pd.read_csv(file_name)
df['date'] = pd.to_datetime(df['date'], format="%Y年%m月%d日")
df = df[(df['date'].dt.year == 2014) & (df['date'].dt.month == 5)]
x = []
y = []
for row in df.iterrows():
    # 5-1
    dt = row[1]['date'].strftime("%m-%d")
    # 最高温度
    max_temp = row[1]['maxTemp']
    x.append(dt)
    y.append(max_temp)
for row in df.iterrows():
    # 5-1
    dt = row[1]['date'].strftime("%m-%d")
    # 最高温度
    max_temp = row[1]['minTemp']
    x.append(dt)
    y.append(max_temp)

plt.scatter(x, y)
plt.show()

