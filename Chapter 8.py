#8-1
#消息：编写一个名为display_message() 的函数，它打印一个句子，指出你在本章学的是什么。
#调用这个函数，确认显示的消息正确无误。

def display_message():
    print("This partion I learn the function.")
display_message()

#8-2
#喜欢的图书 ：编写一个名为favorite_book() 的函数，其中包含一个名为title 的形参。
#这个函数打印一条消息，如One of my favorite books is Alice in Wonderland 。
#调用这个函数，并将一本图书的名称作为实参传递给它。 

def favorite_book(title):
    print("One of my favorite books is " + title.title() )
favorite_book('ailce in wonderland')

#8-3
#T恤：编写一个名为make_shirt() 的函数，它接受一个尺码以及要印到T恤上的字样。
#这个函数应打印一个句子，概要地说明T恤的尺码和字样。 
#使用位置实参调用这个函数来制作一件T恤；
#再使用关键字实参来调用这个函数。

def make_shirt(size,type):
    print("This t-shirt is " + 
          size.title() +
          ",and there is some letters above it: " + 
          type.title()
          )
make_shirt('samll','\tgod bless you\n')
make_shirt(size = 'small',type = '\tgod bless you')

#8-4
#大号T恤：修改函数make_shirt() ，使其在默认情况下制作一件印有字样“I love Python”的大号T恤。
#调用这个函数来制作如下T恤：
#一件印有默认字样的大号T 恤、一件印有默认字样的中号T恤和一件印有其他字样的T恤（尺码无关紧要）。

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
#城市：编写一个名为describe_city() 的函数，它接受一座城市的名字以及该城市所属的国家。
#这个函数应打印一个简单的句子，如Reykjavik is in Iceland 。
#给用于存储国家的形参指定默认值。
#为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认国家。

def describe_city(city,coutry = 'china'):
    print(city +
          " is in " + 
          coutry
          )
describe_city('chengdu')
describe_city('shagnhai')
describe_city('kyoto','japan')

#8-6
# 城市名：编写一个名为city_country() 的函数，它接受城市的名称及其所属的国家。
# 这个函数应返回一个格式类似于下面这样的字符串："Santiago, Chile" 至少使用三个城市-国家对调用这个函数，并打印它返回的值。

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
#专辑：编写一个名为make_album() 的函数，它创建一个描述音乐专辑的字典。
#这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。
#使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。

def make_album(singer_name,album_name):
    x = "The singer's name is: " + singer_name.title() + "" +  " is in " + album_name.title()
    return x
while True:
    a = input("The singer's name is: ")
    b = input("The album's name is: ")
    if a == 'q':
        break
    print(make_album(a,b))

#8-9
#用户的专辑 ：在为完成练习8-7编写的程序中，编写一个while 循环，让用户输入一个专辑的歌手和名称。
#获取这些信息后，使用它们来调用函数make_album() ，并将创建的字典打印出来。
#在这个while 循环中，务必要提供退出途径。 

#8-10
#魔术师：创建一个包含魔术师名字的列表，并将其传递给一个名为show_magicians() 的函数，这个函数打印列表中每个魔术师的名字。

def show_magicians(names):
    print("The magicican's name is: ")
    for name in names[:]:
        print( name + "." )
x = ['Tom','Mary','John']
show_magicians(x)

#8-11
#了不起的魔术师:在你为完成练习8-9而编写的程序中，编写一个名为make_great() 的函数，
#对魔术师列表进行修改，在每个魔术师的名字中都加入字样“the Great”。
#调用函数show_magicians() ，确认魔术师列表确实变了。

x = ['Tom','Mary','John']
a = ''
def make_great(x):
    for i in x[:]:
        a = "the great " + i
        print(a)
make_great(x)

#8-12
#三明治 ：编写一个函数，它接受顾客要在三明治中添加的一系列食材。
#这个函数只有一个形参（它收集函数调用中提供的所有食材），并打印一条消息，对顾客 点的三明治进行概述。
#调用这个函数三次，每次都提供不同数量的实参。 

def sandwiches(food):
    print("add this food:\n " +  "-" + i + "\n")
x = ['water','beef','egg']
for i in x[:]:
    sandwiches(i)

#8-13
#用户简介 ：复制前面的程序user_profile.py，在其中调用build_profile() 来创建有关你的简介；
#调用这个函数时，指定你的名和姓，以及三个描述你的键-值对。 

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
# 汽车：编写一个函数，将一辆汽车的信息存储在一个字典中。
# 这个函数总是接受制造商和型号，还接受任意数量的关键字实参。
# 这样调用这个函数：提供必不可 少的信息，以及两个名称—值对，如颜色和选装配件。这个函数必须能够像下面这样进行调用：
#car = make_car('subaru', 'outback', color='blue', tow_package=True) 

def make_car(maker,type,**information):
    a ={}
    a[maker] = "The maker of the car is:\n" + "-" + maker.title() + "."
    a[type] = "The type of the car is:\n" + "-" + type.title() + "."
    for key,value in information.items():
        a['information'] = "The " + key + "is:\n" + "-" + value + "."
    return a 

car = make_car('subaru', 'outback', color = 'blue', tow_package = 'what')
print(car)





    