import requests
from bs4 import BeautifulSoup
import pandas as pd
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/88.0.4324.104 Safari/537.36',
    'Cookie': 'bid=2OXOUlk8z6A; douban-fav-remind=1; __utmz=30149280.1721792513.1.1.utmcsr=baidu|utmccn=('
              'organic)|utmcmd=organic; ap_v=0,6.0; _pk_id.100001.4cf6=8c535ae428a78eef.1730956884.; __utmc=30149280; '
              '__utmc=223695111; ll="118145"; __utma=30149280.351232312.1721792513.1730956885.1730960292.3; __utmt=1; '
              '__utmb=30149280.1.10.1730960292; dbcl2="132982081:Ja5zRpRRWzE"; ck=1htc; '
              '__utma=223695111.1707810684.1730956885.1730956885.1730960347.2; __utmb=223695111.0.10.1730960347; '
              '__utmz=223695111.1730960347.2.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; '
              '_pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1730960347%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; '
              '_pk_ses.100001.4cf6=1; push_noty_num=0; push_doumail_num=0; '
              '_vwo_uuid_v2=D25DFC4414F621F18B9C36B6A2C3BE2D1|22c0a2e0fe011d78aa6bd1820d575ecc; '
              'frodotk_db="821d2d5a15ee074f8657880e41ca15ed"'
}
htmls = []
for page in range(0, 226, 25):
    url = 'https://movie.douban.com/top250?start=' + str(page) + '&filter='
    print(f"正在爬取{url}")
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"请求失败: {response.status_code} {url}")
    htmls.append(response.text)


data = []
for html in htmls:
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all("div", class_="item")
    for item in items:
        try:
            row = {
                "rank": item.find("em").text,
                "title": item.find("span", class_="title").text,
                "score": item.find("span", class_="rating_num").text,
                "comments": item.find("div", class_="star").find_all("span")[-1].text.replace("人评价", ""),
                "quote": item.find("span", class_="inq").text
            }
            data.append(row)
        except AttributeError:
            pass

df = pd.DataFrame(data)
df.to_csv("./data/douban_top_250.csv", index=False, encoding='utf-8-sig')
