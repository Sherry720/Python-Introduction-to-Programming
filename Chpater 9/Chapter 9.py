#9-1
class Restaurant():
    def __init__(self, restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("The name of this restaurant is: " +
              self.restaurant_name.title() +
              "\t,and the type of it is:" +
              self.cuisine_type.title() +
              ".\n"
              )
    def open_restaurant(self):
        print("This restaurant is working.")

restaurant = Restaurant("anita_hailey",'chuancai')
restaurant.describe_restaurant()
restaurant.open_restaurant()

#9-2
restaurant_1 = Restaurant('haruhi','sweet')
restaurant_1.describe_restaurant()
restaurant_2 = Restaurant('misaka','poper')
restaurant_2.describe_restaurant()
restaurant_3 = Restaurant('kazusa','love')
restaurant_3.describe_restaurant()

#9-3
class User():
    def __init__(self,first_name,last_name,age,heart):
       self.first_name = first_name
       self.last_name = last_name
       self.age = age
       self.heart = heart
    def describe_user(self):
        print("The full name is:\n" +
            "-" +
            self.first_name.title() +
            " " + 
            self.last_name.title() +
            "." 
            )
        exs = [self.age,self.heart]
        for i in exs[:]:
            print("The " +
                  self.first_name.title() +
                  " " +
                  self.last_name.title() +
                  " is:\n" +
                  i
                  ) 
    def great_user(self):
        print("Hello," +
              self.first_name.title() +
                  " " +
                  self.last_name.title()
                  )
user_0 = User('anita','hailey','18','tall')
user_0.describe_user()
user_0.great_user()

user_1 = User('misaka','lover','16','sweet')
user_1.describe_user()
user_1.great_user()

user_2 = User('haruhi','lover','16','brave')
user_2.describe_user()
user_2.great_user()

#9-4
class Restaurant():
    def __init__(self, restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print("The name of this restaurant is: " +
              self.restaurant_name.title() +
              "\t,and the type of it is:" +
              self.cuisine_type.title() +
              ".\n"
              )
    def open_restaurant(self):
        print("This restaurant is working.")

    def set_number_served(self,number):
        self.number_served += number

    def increase_number_served(self,number):
        self.number_served += number

    def visit_number(self):
        print("There are totally " +
              str(self.number_served) +
              " poeple visit this restaurant."
              )

restaurant = Restaurant("anita_hailey",'chuancai')
restaurant.set_number_served(20)
restaurant.increase_number_served(1030)
restaurant.visit_number()

#9-5
class User():
    def __init__(self,first_name,last_name,age,heart):
       self.first_name = first_name
       self.last_name = last_name
       self.age = age
       self.heart = heart
       self.login_attempts = 0
    def increase_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print("The full name is:\n" +
            "-" +
            self.first_name.title() +
            " " + 
            self.last_name.title() +
            "." 
            )
        exs = [self.age,self.heart]
        for i in exs[:]:
            print("The " +
                  self.first_name.title() +
                  " " +
                  self.last_name.title() +
                  " is:\n" +
                  i
                  ) 
    def great_user(self):
        print("Hello," +
              self.first_name.title() +
                  " " +
                  self.last_name.title()
                  )
user_0 = User('anita','hailey','18','tall')
#user_0.describe_user()
#user_0.great_user()
user_0.increase_login_attempts()
user_0.increase_login_attempts()
user_0.increase_login_attempts()
print(user_0.increase_login_attempts())
user_0.reset_login_attempts()
print(user_0.increase_login_attempts())

#9-6
class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served


class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""

    def __init__(self, name, cuisine_type='ice_cream'):
        """Initialize an ice cream stand."""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())


big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.show_flavors()

#9-7
class User():
    def __init__(self,first_name,last_name,age,heart):
       self.first_name = first_name
       self.last_name = last_name
       self.age = age
       self.heart = heart
       self.login_attempts = 0
    def increase_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print("The full name is:\n" +
            "-" +
            self.first_name.title() +
            " " + 
            self.last_name.title() +
            "." 
            )
        exs = [self.age,self.heart]
        for i in exs[:]:
            print("The " +
                  self.first_name.title() +
                  " " +
                  self.last_name.title() +
                  " is:\n" +
                  i
                  ) 
    def great_user(self):
        print("Hello," +
              self.first_name.title() +
                  " " +
                  self.last_name.title()
                  )
user_0 = User('anita','hailey','18','tall')

class Admin(User):
    def _int_(self,first_name,last_name,age,heart):
        super()._init_(first_name,last_name,age,heart)
        self.privileages = []   # 254行得放类的下面
    def show_privileages(self):
        for privileage in self.privileages:
            print("Admin can :" +
                  "\n-" +
                  privileage
                  )


user_9 = Admin('anita','hailey','18','tall')
user_9.privileages = ['add_the_post',
                            'delete_the_post',
                            'can_ban_user'
                            ]
user_9.show_privileages()

#9-8
class Car():
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=60):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """Upgrade the battery if possible."""
        if self.battery_size == 60:
            self.battery_size = 85
            print("Upgraded the battery to 85 kWh.")
        else:
            print("The battery is already upgraded.")
    
        
class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


print("Make an electric car, and check the battery:")
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()

print("\nUpgrade the battery, and check it again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

print("\nTry upgrading the battery a second time.")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

#9-10
from restaurant import Restaurant
restaurant_9 = Restaurant('anita','ice_cream')
restaurant_9.describe_restaurant()

#9-11
"""from user import User,Admin
user_72 = Admin('anita','hailey','18','tall')
user_72.privileages = ['add_the_post',
                            'delete_the_post',
                            'can_ban_user'
                            ]
user_72.show_privileages()"""

#9-12
from admin import Admin
user_108 = Admin('anita','hailey','18','tall')
user_108.privileages = ['add_the_post',
                            'delete_the_post',
                            'can_ban_user'
                            ]
user_108.show_privileages()

#9-13
from collections import OrderedDict
explain = OrderedDict()
explain['if'] = '循环'
explain['print'] = '输出'
explain['for_in'] = '循环'
explain['lower()'] = '小写'
explain['range'] = '排列'
for key,value in explain.items():
    print(key +"'s meaning is " + value + '.')

#9-14
class Die:
    def __init__(self, sides = '6'):
        self.sides = sides
    def roll_die(self):
        i = 1
        while i <= 10:
            i += 1
            from random import randint
            number = randint(1,self.sides)
            print("The number is :\n" +
                  "-" +
                  str(number) +
                  "\n" 
                  )
number_72 = Die (10)
number_72.roll_die()


       
