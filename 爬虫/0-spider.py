import random

import requests
import pandas as pd
import time
from pprint import pprint
from bs4 import BeautifulSoup

def download_html(url):
    # 保存html文件到本地
    response = requests.get(url)
    with open('douban.html', 'w', encoding='utf-8') as f:
        f.write(response.text)



def get_data(url):
    print(f"正在爬取：{url}")
    # 请求网页内容
    request = requests.get(url)
    if request.status_code != 200:
        print("网页爬取失败!")
    else:
        # 实例化网页解析器
        soup = BeautifulSoup(request.text, 'html.parser')
        # 查找节点
        # title = soup.find('h1').get_text(strip=True)
        # sub_title = soup.find('p').get_text(strip=True)
        # 批量查找
        titles = pd.DataFrame(columns=['title', 'url'])

        articles = soup.find_all('h2', attrs={'class': 'entry-title'})
        i = 0
        for article in articles:
            title = article.get_text(strip=True)
            url = article.findNext('a')['href']
            # 向DataFrame中添加数据
            titles.loc[i] = [title, url]
            i += 1
        # 获取通过url获取页码
        file_name = parse_file_name(url)
        titles.to_csv(f'./data/{file_name}', mode='a', index=False, encoding='utf-8')
        print("爬取完成!")


def parse_file_name(url):
    url_list = url.split('/')
    domain = url_list[2]
    page = 1
    # 如果不包含下划线
    if url.count('_') > 0:
        page = url_list[4].split('_')[1].split('.')[0]
    return f"{domain}_{page}.csv"

# 请求网页 GET POST
# GET https://movie.douban.com/chart
# url = 'https://www.weather.com.cn/weather/101251201.shtml'
url = ["http://www.crazyant.net/"]
url_list = url + [f"http://www.crazyant.net/page/{x}" for x in range(2, 3)]

for url in url_list:
    get_data(url)
    time.sleep(random.randint(3, 8))
