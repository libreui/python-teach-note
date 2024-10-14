class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # 里程表读数


    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name


    def read_odometer(self): # 读取里程表
        """打印一条指出汽车里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")


    def update_odometer(self, mileage):
        """设置里程表读数, 不允许将里程表读数往回调"""
        if mileage >= self.odometer_reading: # 如果新的里程数大于或等于原来的里程数
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles


    def fill_gas_tank(self):
        """打印一条消息，指出汽车需要加油"""
        print("The gas tank is full!")


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size


    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")


    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car): # 继承
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery(75) # 添加新属性
        self.car = Car(make, model, year)


    def describe_battery(self): # 定义新方法
        """打印一条描述电瓶容量的消息"""
        self.battery.describe_battery()


    def fill_gas_tank(self):
        """电动车没有油箱"""
        print("This car doesn't need a gas tank!")


electric_car = ElectricCar('tesla', 'model s', 2019)
print(electric_car.get_descriptive_name())
electric_car.describe_battery()
electric_car.fill_gas_tank()
electric_car.battery.get_range()



# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
#
# # 修改属性
# my_new_car.update_odometer(24_000)
# my_new_car.read_odometer()
# my_new_car.increment_odometer(100)
# my_new_car.read_odometer()