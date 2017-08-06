#8-1


def display_message():
    print("This partion I learn the function.")
display_message()

#8-2

def favorite_book(title):
    print("One of my favorite books is " + title.title() )
favorite_book('ailce in wonderland')

#8-3

def make_shirt(size,type):
    print("This t-shirt is " + 
          size.title() +
          ",and there is some letters above it: " + 
          type.title()
          )
make_shirt('samll','\tgod bless you\n')
make_shirt(size = 'small',type = '\tgod bless you')

#8-4

def make_shirt(size,type = 'I love Python'):
    print("This t-shirt is " + 
          size.title() +
          ",and there is some letters above it: " + 
          type.title()
          )
make_shirt('big')
make_shirt(size = 'meidum')
make_shirt(size = 'samll', type = 'Fuck you!')

#8-5

def describe_city(city,coutry = 'china'):
    print(city +
          " is in " + 
          coutry
          )
describe_city('chengdu')
describe_city('shagnhai')
describe_city('kyoto','japan')

#8-6

def city_country(city,country = 'china'):
    x = "The city:" + city.title() + "" +  " is in " + country.title()
    return x
while True:
    a = input("The city: ")
    b = input("The country: ")
    if a == 'q':
        break
    print(city_country(a,b))

#8-7

def make_album(singer_name,album_name):
    x = "The singer's name is: " + singer_name.title() + "" +  " is in " + album_name.title()
    return x
while True:
    a = input("The singer's name is: ")
    b = input("The album's name is: ")
    if a == 'q':
        break
    print(make_album(a,b))


#8-10

def show_magicians(names):
    print("The magicican's name is: ")
    for name in names[:]:
        print( name + "." )
x = ['Tom','Mary','John']
show_magicians(x)

#8-11

x = ['Tom','Mary','John']
a = ''
def make_great(x):
    for i in x[:]:
        a = "the great " + i
        print(a)
make_great(x)

#8-12

def sandwiches(food):
    print("add this food:\n " +  "-" + i + "\n")
x = ['water','beef','egg']
for i in x[:]:
    sandwiches(i)

#8-13

def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('anita','hailey',
                             location = 'chengdu',
                             field = 'student',
                             interst = 'comic',
                             )
print(user_profile) 

#8-14

def make_car(maker,type,**information):
    a ={}
    a[maker] = "The maker of the car is:\n" + "-" + maker.title() + "."
    a[type] = "The type of the car is:\n" + "-" + type.title() + "."
    for key,value in information.items():
        a['information'] = "The " + key + "is:\n" + "-" + value + "."
    return a 

car = make_car('subaru', 'outback', color = 'blue', tow_package = 'what')
print(car)





    
