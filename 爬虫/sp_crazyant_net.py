
import requests
import re
from bs4 import BeautifulSoup
import url_manager

# 目标网站的URL
url = 'http://www.crazyant.net/'
# 文章列表页的URL
# article_list_url = 'http://www.crazyant.net/2261.html'

# 定义URL管理器
url_manager = url_manager.UrlManager()
url_manager.add_new_url(url)

# 打开一个文件名字叫做craw_all_pages.txt
fileOut = open("./data/craw_all_pages.txt", "w", encoding="utf-8")
# 取出等待爬取的url
while url_manager.has_new_url():
    curr_url = url_manager.get_url()
    response = requests.get(curr_url, timeout=3)
    if response.status_code != 200:
        print("请求失败，状态码：", response.status_code, curr_url)
        continue
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string
    fileOut.write(f"{curr_url}\t{title}\n")
    fileOut.flush()
    print(f"爬取成功：{curr_url}, 标题：{title}, 连接数量：{len(url_manager.new_urls)}")

    # 把页面所有链接放入URL管理器
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href is None:
            continue
        pattern = r'^http://www.crazyant.net/\d+.html$'
        if re.match(pattern, href):
            url_manager.add_new_url(href)

fileOut.close()

# 定义cookies字典
cookies = {
    "captchaKey": "14a54079a1",
    "captchaExpire": "1548852352",
}
# response = requests.get(, cookies=cookies)
