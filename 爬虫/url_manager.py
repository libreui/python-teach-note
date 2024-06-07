class Url_Manager(object):
    """
    url管理器
    """

    def __init__(self):
        self.new_url = set()
        self.old_url = set()
        pass

    def add_new_url(self, url):
        """添加一个URL到集合中"""
        if url is None or len(url) == 0:
            return
        if url in self.new_url or url in self.old_url:
            return
        self.new_url.add(url)

    def add_new_urls(self, urls):
        """添加多个URL到集合中"""
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def get_url(self):
        """从集合中获取一个URL"""
        if self.has_new_url():
            url = self.new_url.pop()
            self.old_url.add(url)
            return url

        return None


    def has_new_url(self):
        """判断集合中是否有新的URL"""
        return len(self.new_url) > 0


if __name__ == '__main__':
    # 测试代码
    url_manager = Url_Manager()
    url_manager.add_new_url('http://www.baidu.com')
    print(url_manager.new_url, url_manager.old_url)
    url_manager.add_new_url('http://www.sina.com')
    print(url_manager.new_url, url_manager.old_url)
    url_manager.add_new_url('http://www.qq.com')
    print(url_manager.new_url, url_manager.old_url)

    print(url_manager.get_url())
    print(url_manager.new_url, url_manager.old_url)
    print(url_manager.get_url())
    print(url_manager.new_url, url_manager.old_url)
    print(url_manager.get_url())
    print(url_manager.new_url, url_manager.old_url)




