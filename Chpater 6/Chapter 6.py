#6-1

godness = {'name':'冬馬かずさ',
           'age':17,
           'city':'fengcheng',
           }
print('Name is: ' + godness['name'])
print('Age is: ' + str(godness['age']))
print('City is: ' + godness['city'])

#6-2

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


for key,value in list.items():
    print(key +"'s meaning is " + value + '.')

#6-5


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
