import requests
from bs4 import BeautifulSoup

domain = "https://ysbo.net"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}


def get_novel_chapters():
    """获取章节所有链接"""
    root = "https://ysbo.net/book/6700.html"
    response = requests.get(root, headers=headers)
    response.encoding = "utf-8"
    if response.status_code != 200:
        raise Exception("请求失败")
    soup = BeautifulSoup(response.text, 'html.parser')
    urls = []
    for url in soup.find('ul', class_='three').find_all('a'):
        urls.append((domain + url.get('href'), url.text))
    return urls


def get_chapter_content(url):
    """获取章节内容"""
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"
    if response.status_code != 200:
        raise Exception("请求失败")
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find('article', class_='article-content').text


for url, title in get_novel_chapters():
    print(f"正在爬取章节：{title}, 链接：{url}")
    with open(f"./data/chapter/{title}.txt", "w", encoding="utf-8") as f:
        f.write(get_chapter_content(url))

print("爬取完成")
