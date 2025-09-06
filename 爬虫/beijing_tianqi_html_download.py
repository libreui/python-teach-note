import time

import requests
# 下载网页import requests

# 创建请求头
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'Cookie': "UserId=17537511293247496; cityPy=yanbian; cityPy_expire=1754355929; Hm_lvt_ab6a683aa97a52202eab5b3a9042a8d2=1753751130; Hm_lpvt_ab6a683aa97a52202eab5b3a9042a8d2=1753751395; Hm_lvt_30606b57e40fddacb2c26d2b789efbcb=1753751469; Hm_lpvt_30606b57e40fddacb2c26d2b789efbcb=1753751469; HMACCOUNT=D06D28AA19EE5121; Hm_lvt_7c50c7060"
}
# url = 'https://lishi.tianqi.com/qingdao/201101.html'
# response = requests.get(url, headers=headers)
# print(response.text)
for i in range(2011, 2025):
    for j in range(1, 13):
        url = f'https://lishi.tianqi.com/qingdao/{i}{j:02d}.html'
        print(url)
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        # 保存html文件到本地
        with open(f'./html/beijing_tianqi/{i}{j:02d}.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
        # 打印日志
        print(f'已下载{i}年{j}月')
        # 暂停1秒
        time.sleep(1)

