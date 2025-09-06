import pandas as pd

file_name = "../db/beijing_tianqi.csv"
df = pd.read_csv(file_name)
# min_temp = df['minTemp']
# max_temp = df['maxTemp']
# df['date'] = pd.to_datetime(df['date'], format="%Y年%m月%d日")
# df = df[(df['date'].dt.year == 2024) & (df['date'].dt.month == 12)]
# 将maxTemp列
df['maxTemp'] = df['maxTemp'].astype(str) + "C"

# 将maxTemp列中所有的C替换为空字符串
df['maxTemp'] = df['maxTemp'].replace("C", "", regex=True).astype(int)


print(df.head())


