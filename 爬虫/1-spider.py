import asyncio
import aiohttp

# 异步函数，用于发起 HTTP 请求并解析页面
async def fetch_page(session, url):
    try:
        # 异步发起 HTTP 请求
        async with session.get(url) as response:
            # 检查响应状态码
            if response.status == 200:
                # 异步读取响应内容
                html = await response.text()
                # 这里可以添加解析 HTML 的逻辑
                # 例如使用 BeautifulSoup 解析页面
                # soup = BeautifulSoup(html, 'html.parser')
                # 处理解析结果
                # process_data(soup)
                return html
            else:
                print(f"请求 {url} 失败，状态码: {response.status}")
    except Exception as e:
        print(f"请求 {url} 时出错: {e}")
    return None

# 异步函数，用于管理多个爬虫任务
async def run_spider(urls):
    async with aiohttp.ClientSession() as session:
        # 创建任务列表
        tasks = [fetch_page(session, url) for url in urls]
        # 并发执行所有任务
        results = await asyncio.gather(*tasks)
        return results

def main():
    # 要爬取的 URL 列表
    urls = [
        "http://example.com/page1",
        "http://example.com/page2",
        "http://example.com/page3"
    ]
    # 获取事件循环
    loop = asyncio.get_event_loop()
    try:
        # 运行异步任务
        results = loop.run_until_complete(run_spider(urls))
        # 处理所有页面的爬取结果
        for result in results:
            if result:
                print("爬取成功，部分内容:", result[:100])
    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        # 关闭事件循环
        loop.close()

if __name__ == "__main__":
    main()