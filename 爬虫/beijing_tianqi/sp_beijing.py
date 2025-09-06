import json
import random
import time

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

dataset = pd.DataFrame()

# url = https://www.tianqihoubao.com/lishi/beijing/month/201501.html

for year in range(2014, 2025):
    for month in range(1, 13):
        url = f"https://www.tianqihoubao.com/lishi/beijing/month/{year}{month:02d}.html"
        print(f"正在处理 {year} 年 {month} 月的数据......")
        response = requests.get(url)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "html.parser")
        html_content = str(soup)
        # 使用正则表达式获取内容
        pattern = r'<script>const weatherData = (.*?);<\/script>'
        match = re.search(pattern, html_content, re.DOTALL)
        if match:
            json_data = match.group(1).strip()
            # 将属性名添加双引号，转换为标准 JSON 格式
            json_data = re.sub(r'(\w+):', r'"\1":', json_data)
            try:
                # 将 JSON 字符串转换为 Python 列表
                data_list = json.loads(json_data)
                # 将数据添加到 DataFrame[{},{},{}]
                dataset = pd.concat([dataset, pd.DataFrame(data_list)], ignore_index=True)
            except json.JSONDecodeError as e:
                print(f"JSON 解析出错: {e}")
        else:
            print("未找到匹配的内容")
        print(f"{year} 年 {month} 月数据处理完成")
        time.sleep(random.randint(1, 5))

dataset.to_csv("beijing_tianqi.csv", index=False)
print(f"数据处理完成，已保存到 beijing_tianqi.csv 文件中")
