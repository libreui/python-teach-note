# 创建类Dog
import random


class Dog:
    def __init__(self, name, age):
        """ 初始化属性name和age """
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下 """
        print(f"{self.name} is sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚 """
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"My dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()

