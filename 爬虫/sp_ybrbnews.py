import json
import sys
from pprint import pprint

import requests
import pandas as pd
import os.path
from bs4 import BeautifulSoup

# 最大页码
MAX_PAGE = 10
# 数据表头
TABLE_HEADER = ['title', 'url', 'image']

# 网站域名 http://www.ybrbnews.cn/i/142.html
domain = "www.ybrbnews.cn"
host = f"http://{domain}"
path = "/i/142"
# 文件地址
url = [f"{host}{path}.html"]
url_list = url + [f"{host}{path}_{x}.html" for x in range(2, MAX_PAGE)]

# 当前文件根目录
root = os.path.dirname(__file__)
save_path = os.path.join(root, f'data/{domain}')

# 如果目录不存在我们要创建这个目录
if not os.path.exists(save_path):
    os.makedirs(save_path)


# 开始编写爬虫
def parse_html(text):
    """解析html"""
    articles = []
    # 实例化网页解析器
    soup = BeautifulSoup(text, 'html.parser')
    # 找到列表
    lst = soup.findAll('div', attrs={'class': 'wzt1'})
    for item in lst:
        # 找到标题
        image = item.find('img')['src']
        title = item.find('p', attrs={'class': 'title'}).get_text(strip=True)
        a = item.find('a')['href']
        # 创建一个字典
        dic = {
            'title': title,
            'image': image,
            'url': a
        }
        articles.append(dic)
    return articles


def save_to_csv(articles):
    """保存数据到CSV文件"""
    # 保存到CSV文件中
    df = pd.DataFrame(articles)
    df.to_csv(f'{save_path}/sz_news.csv', index=False, encoding='utf-8')
    print('保存成功')


def articles_parse_html(text, finename):
    """解析文正征文稿的html"""
    articles = {
        'title': '',
        'datetime': '',
        'source': '',
        'content': '',
        'image': []
    }
    soup = BeautifulSoup(text, 'html.parser')
    articles['title'] = soup.find('h1', attrs={'class': 'bt'}).get_text(strip=True)
    articles['datetime'] = soup.find('span', attrs={'class': 'ao1'}).get_text(strip=True)
    articles['source'] = soup.find('span', attrs={'class': 'ao2'}).get_text(strip=True)
    content = soup.find('div', attrs={'class': 'maincontent'})
    articles['content'] = content.get_text(strip=True)
    # 保存内容
    with open(f"{save_path}/data/{finename}", 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)
    pprint(articles)


def article_exist(filename):
    """判断是否采集过文章"""
    # TODO 如果采集过的话
    return os.path.exists(f"{save_path}/data/{filename}")


def requests_article(article_url):
    """请求文章正文内容"""

    # 定义文件名称
    filename = article_url.split('/')[-1].replace('.html', '.json')
    # 排除已经采集过的文章
    if article_exist(filename):
        print(f"文章：{filename} 已经采集过了!")
        return

    request = requests.get(article_url)
    request.encoding = "utf-8"
    if request.status_code == 200:
        # 解析HTML内容
        articles_parse_html(request.text, filename)
    else:
        print(f"文章正文爬取失败!")



def run_article_spider():
    """采集文章正文入口"""
    # 读取列表页内容CSV文件
    articles_list = pd.read_csv(f"{save_path}/sz_news.csv")
    for index, row in articles_list.iterrows():
        # 请求正文内容
        requests_article(row['url'])


def run_spider(urls):
    """爬虫运行入口"""
    for u in urls[:1]:
        # 请求网页内容
        request = requests.get(u)
        # 设置请求编码
        request.encoding = "utf-8"
        # 解析内容
        print(f"正在爬取：{u}")
        if request.status_code == 200:
            articles = parse_html(request.text)
            pprint(articles)
            # 保存到CSV文件中
            save_to_csv(articles)
            print('爬取列表页完成')
        else:
            print(f"网页爬取失败!")


if __name__ == "__main__":

    # 根据指令来选择执行哪个爬虫 -l 采集列表页 -a 采集文章正文
    # import sys
    # if len(sys.argv) > 1:
    #     if sys.argv[1] == '-l':
    #         run_spider(url_list)

    if len(sys.argv) > 1:
        if sys.argv[1] == '-l':
            run_spider(url_list)
        elif sys.argv[1] == '-a':
            run_article_spider()


    # 采集列表页
    # run_spider(url_list)
    # 采集文章正文
    # run_article_spider()
