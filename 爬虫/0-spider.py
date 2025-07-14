import requests
import pandas as pd
from pprint import pprint
from bs4 import BeautifulSoup

# 请求网页 GET POST
# GET https://movie.douban.com/chart
# url = 'https://www.weather.com.cn/weather/101251201.shtml'
url = "http://www.crazyant.net/"
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
    print(titles)
    titles.to_csv('./data/0-spider.csv', index=False)
    print("爬取完成!")
