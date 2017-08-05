#6-1
#人：使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。
#该字典应包含键first_name 、last_name 、age 和city 。将存储在该字典中 的每项信息都打印出来。
godness = {'name':'冬馬かずさ',
           'age':17,
           'city':'fengcheng',
           }
print('Name is: ' + godness['name'])
print('Age is: ' + str(godness['age']))
print('City is: ' + godness['city'])

#6-2
#喜欢的数字 ：使用一个字典来存储一些人喜欢的数字。
#请想出5个人的名字，并将这些名字用作字典中的键；想出每个人喜欢的一个数字，并将这些数字作为值存 储在字典中。
#打印每个人的名字和喜欢的数字。为让这个程序更有趣，通过询问朋友确保数据是真实的。

number_5 = range(1,6)
leter = ['a','b','c','d','e']
numbers = {'a':'1',
           'b':'2',
           'c':'3',
           'd':'4',
           'e':'5',
           }
for x in leter[:]:
    print(numbers[x])

#6-3
#词汇表 ：Python字典可用于模拟现实生活中的字典，但为避免混淆，我们将后者称为词汇表。 
#想出你在前面学过的5个编程词汇，将它们用作词汇表中的键，并将它们的含义作为值存储在词汇表中。 
#以整洁的方式打印每个词汇及其含义。为此，你可以先打印词汇，在它后面加上一个冒号，再打印词汇的含义；
#也可在一行打印词汇，再使用换行符（\n ）插 入一个空行，然后在下一行以缩进的方式打印词汇的含义。 

list = {'if':'循环',
        'print':'输出',
        'for_in':'循环',
        'lower()':'小写',
        'range':'排列',
        }
program = ['if','print','for_in','lower()','range']
for x in program[:]:
    print(x + "'s meaning is " + list[x])

#6-4
#词汇表2:既然你知道了如何遍历字典,现在请整理你为完成练习6-3而编写的代码，
#将其中的一系列print 语句替换为一个遍历字典中的键和值的循环。
#确定该循环正确无误后，再在词汇表中添加5个Python术语。
#当你再次运行这个程序时，这些新术语及其含义将自动包含在输出中。 

for key,value in list.items():
    print(key +"'s meaning is " + value + '.')

#6-5
#河流:创建一个字典，在其中存储三条大河流及其流经的国家。其中一个键—值对可能是'nile': 'egypt' 。 
#使用循环为每条河流打印一条消息，如“The Nile runs through Egypt.”。 
#使用循环将该字典中每条河流的名字都打印出来。 
#使用循环将该字典包含的每个国家的名字都打印出来.

rivers = {'amazon_river':'brazil'',peru' ',bolivia' ',colombia',
          'nile_kagera':'ethiopia' ',egyth' ',south_sudan',
          'yangtze':'china',
          }
for key,value in set(rivers.items()):
    print("The " + 
          key.title() + 
          " runs through " +
          value.title()
          )
    print(key.title())
    print(value.title())

#6-6
#调查：在6.3.1节编写的程序favorite_languages.py中执行以下操作。 
#创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中。 
#遍历这个人员名单，对于已参与调查的人，打印一条消息表示感谢。
#对于还未参与调查的人，打印一条消息邀请他参与调查。

favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python',
                      } 
for name, language in favorite_languages.items():
    print(name.title() + 
          "'s favorite language is " +
          language.title() +
          "."
          ) 

name = ['jen','bob','tom','phil']
for x in (name[:]):
    if x in favorite_languages.keys():
        print("Hi,"+
            x +
            ",glad to see you like the program,\n"
            )
    else:
        print(x.title() + 
              ",would you like to complete this invite?\n"
              )

#6-7
#人:在为完成练习6-1而编写的程序中，再创建两个表示人的字典，然后将这三个字典都存储在一个名为people 的列表中。
#遍历这个列表，将其中每个人的所有 信息都打印出来。

godness_0 = {'name':'冬馬かずさ',
           'age':str(17),
           'city':'fengcheng',
           }
godness_1 = {'name':'涼宮春日',
           'age':str(17),
           'city':'fengcheng',
           }
godness_2 = {'name':'長門有希',
           'age':str(17),
           'city':'fengcheng',
           }
people = [godness_0,godness_1,godness_2]
for x in people[:]:
    for key,value in x.items():
        print(key.title() + 
              " is:" + 
              value +
              ".\n"
              )

#6-8
#宠物：创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名；
#在每个字典中，包含宠物的类型及其主人的名字。
#将这些字典存储在一个名为pets 的列表中，再遍历该列表，并将宠物的所有信息都打印出来。 

dog = {'name':'peter',
       'owner':'Tom',
       'type':'哈士奇'
       }
cat = {'name':'john',
       'owner':'marry',
       'type':'黑猫'
       }
pig = {'name':'bob',
       'owner':'sarch',
       'type':'猪八戒'
       }
pets = [dog,cat,pig]
for x in pets[:]:
    for key,value in x.items():
        print(key.title() + 
              " is:" + 
              value +
              ".\n"
              )

#6-9
#喜欢的地方：创建一个名为favorite_places 的字典。
#在这个字典中，将三个人的名字用作键；对于其中的每个人，都存储他喜欢的1~3个地方。
#为让这个练 习更有趣些，可让一些朋友指出他们喜欢的几个地方。
#遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。 

favorite_places = {'tom':['amercian','heaven','new_street'],
                   'bob':['brazil','peru','bolivia','colombia'],
                   'mary':['china'],
                   }
for keys,values in favorite_places.items():
    print(keys.title() +
          " loves these places:")
    for value in values:
        print("\t" + value.title())

#6-10
#喜欢的数字：修改为完成练习6-2而编写的程序，让每个人都可以有多个喜欢的数字
#然后将每个人的名字及其喜欢的数学打印出来。


number = {'a':range(1,11,2),
          'b':range(0,11,2),
          'c':range(1,21,3),
          'd':range(0,26,5),
          'e':range(1,73,8),
          }
for keys,values in number.items():
    print(keys.title() +
          " favorate number is:")
    for value in values:
        print("\t" + str(value))

#6-11
#城市：创建一个名为cities 的字典，其中将三个城市名用作键；
#对于每座城市，都创建一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该城市的事实。
#在表示每座城市的字典中，应包含country 、population 和fact 等键。
#将每座城市的名字以及有关它们的信息都打印出来。 

# chengdu_0 = {'contry':'china',
#           'population':'100millions',
 #          'fact':['its a  food city'],
  #         }
# new_york_0 = {'contry':'american',
   #        'population':'100millions',
    #       'fact':['its a  woderful city'],
     #      }
# kyoto_0 = {'contry':'japan',
      ##    'fact':['its a  beauty city'],
        #   }
cities = {
    "chengdu":{'contry':'china',
           'population':'100millions',
           'fact':"its a  food city",
           },
    "new_york":{'contry':'american',
           'population':'100millions',
           'fact':"its a  woderful city",
           },
    "kyoto":{'contry':'japan',
           'population':'100millions',
           'fact':"its a  beauty city",
           },
    }
for keys,values in cities.items():
    print(keys.title() +
          "'s information:"
          )
    print("\tCountry: " + 
          values["contry"].title())
    print("\tpopulation: " + 
          values['population'].title())
    print("\tkyoto: " + 
          values['fact'].title())