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