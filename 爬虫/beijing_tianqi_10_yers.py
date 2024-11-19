from io import StringIO
import requests
import pandas as pd
import time

url = "http://tianqi.2345.com/Pc/GetHistory"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
    "referer": "http://tianqi.2345.com/wea_history/54511.htm"
}


def craw_table(year, month):
    """
    爬取指定年份和月份的天气数据
    :param year: 年份
    :param month: 月份
    :return: DataFrame
    """
    params = {
        "areaInfo[areaId]": 54511,
        "areaInfo[areaType]": 2,
        "date[year]": year,
        "date[month]": month
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()['data']
    html = pd.read_html(StringIO(data))
    return html[0]


df_list = []
for year in range(2014, 2024):
    for month in range(1, 13):
        print(f"正在爬取{year}年{month}月的数据")
        df = craw_table(year, month)
        df_list.append(df)

pd.concat(df_list).to_csv("./data/beijing_tianqi_10_yers.csv", index=False)
print("爬取完成")
