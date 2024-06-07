import requests

url = "https://baike.baidu.com/item/%E5%BA%86%E4%BD%99%E5%B9%B4/9592679"
response = requests.get(url)
print(response.status_code)
print(response.headers)
