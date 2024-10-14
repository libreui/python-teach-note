class Computer:
    def __init__(self, screen_size, cpu, ram_size, storage_size):
        self.screen_size = screen_size
        self.cpu = cpu
        self.ram_size = ram_size
        self.storage_size = storage_size

    def display_info(self):
        print(f"屏幕尺寸: {self.screen_size}")
        print(f"CPU型号: {self.cpu}")
        print(f"内存大小: {self.ram_size}")
        print(f"存储大小: {self.storage_size}")
    def power_on(self):
        print("电脑已开机")
    def power_off(self):
        print("电脑已关机")
    def run_aplication(self, application):
        print(f"正在运行{application}")


# 创建一个Computer对象
my_computer = Computer("15.6英寸", "Intel Core i5", "8GB", "1TB")
my_computer.display_info()