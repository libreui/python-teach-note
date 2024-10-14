class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def set_number_served(self, number_served):
        self.number_served = number_served


    def increment_number_served(self, number_served):
        self.number_served += number_served

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name} and the cuisine type is {self.cuisine_type}")


    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open")


restaurant1 = Restaurant('KFC', 'fast food')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant1.set_number_served(79)
restaurant1.increment_number_served(10)
print(restaurant1.number_served)




class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0


    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print(f"The user name is {self.first_name} {self.last_name}")


    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, welcome to our website")


user1 = User('Tom', 'Jerry')
user1.describe_user()
user1.greet_user()
