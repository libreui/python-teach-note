import requests
from bs4 import BeautifulSoup

# url = "https://baike.baidu.com/item/%E5%BA%86%E4%BD%99%E5%B9%B4/9592679"
url = "http://www.crazyant.net/"
response = requests.get(url)

# 网页解析器
soup = BeautifulSoup(response.text, 'html.parser')
# <a href="http://www.crazyant.net/3567.html" rel="bookmark">Python怎样将PDF拆分成多个文件</a>
articles = soup.find_all('a', attrs={'rel': 'bookmark'})

for article in articles:
    if 'entry-title' in article.parent.attrs['class']:
        print(article.name, article['href'], article.get_text())
