"""
爬取汽车图片
url: https://pic.netbian.com/4kqiche/
"""
from pprint import pprint
import requests
from bs4 import BeautifulSoup
import os

domain = "https://pic.netbian.com"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


def get_all_urls():
    """爬取所有图片链接与缩略图地址"""
    pic_urls = []
    for page in range(2, 3):
        _page_url = f'{domain}/4kqiche/index_{page}.html'
        response = requests.get(_page_url, headers=headers)
        response.encoding = "gbk"
        if response.status_code != 200:
            raise Exception('请求失败')
        soup = BeautifulSoup(response.text, 'html.parser')
        ul = soup.find('ul', class_='clearfix')
        for dom in ul.find_all('li'):
            a = dom.find('a')
            img = dom.find('img')
            pic_urls.append((domain + a['href'], domain + img['src']))
    return pic_urls


for pic_url in get_all_urls():
    print(pic_url[1])
    img_name = os.path.basename(pic_url[1])
    with open(f'./data/images/{img_name}', 'wb') as f:
        f.write(requests.get(pic_url[1], headers=headers).content)
print('爬取完成')
