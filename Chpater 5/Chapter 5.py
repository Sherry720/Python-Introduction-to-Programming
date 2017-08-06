#5-1

number = range(1,11)
double = range(0,11,2)
for value in number[:]:
    if value in double:
        print("Is value in double? \nI predict True." + str(value) )
    else:
        print("\nIs value in double? \nI predict False." + str(value))

#5-2

Z = ["ONE",'TWO']
for x in Z[:]:
    if x == 'two':
        print( x.lower() + "==" + 'two' )
    else:
        print( x.lower() + " != " + 'two' )

a= str(2)
b = str(3)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print(a == b)

list_0 = range(1,11)
list_1 = range(1,21,3)
list_2 = range(0,15,2)
for x in list_0:
    if (x in list_1) and (x in list_2):
        print("it is in the list_1")
    if(x in list_1) or (x in list_2):
        print("it isn't in the list_1")

#5-3

color = ['green','yellow','red']
for alien_color in color[:-1]:
    if alien_color == "green":
        print('You have gained 5 points.')

#5-4

color = ['green','yellow','red']
for alien_color in color[:-1]:
    if alien_color == "green":
        print('You have gained 5 points.')
    else:
        print('You have gained 10 points.')

#5-5

color = ['green','yellow','red']
for alien_color in color[:]:
    if alien_color == "green":
        print('You have gained 5 points.')
    elif alien_color == 'yellow':
        print('You have gained 10 points.')
    else:
        print('You have gained 15 points.')
 
#5-6

ages = range(1,101)
for age in ages:
    if age < 2 :
        print("He is a baby.")
    if age in range(2,4):
        print("He is learn to walk.")
    if age in range(4,13):
        print("He is a chindren.")
    if age in range(13,20):
        print("He is a teenager.")
    if age in range(20,65):
        print("He is a adult.")
    if age in range(65,101):
        print("He is a older.")

#5-7

favorite_friuts = ['apple','banana','peach']
fruit = ['apple','grape','banana','cherry','peach']
for x in fruit[:]:
    if x in favorite_friuts:
        print("You really like " + x )

#5-8
        
name = ('Bob','Tom','Sherry','admin','Jerry')
for x in name[:]:
    if x == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print('Hello,' + x , ' thank you for logging in again.')

#5-9

name = ('Bob','Tom','Sherry','admin','Jerry')
if name:
    for x in name[:]:
        if x == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello,' + x , ' thank you for logging in again.')
else:
    print('We need to find some users!')

name = ()
if name:
    for x in name[:]:
        if x == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello,' + x , ' thank you for logging in again.')
else:
    print('We need to find some users!')

#5-10

current_users = ['Bob','Tom','Sherry','admin','Jerry']

new = []    #把current_users小写
for a in current_users[:]:
    b = a.lower()
    new.append(b)

new_users = ('Jack','Mary','Sherry','admin','John')
for x in new_users[:]:
    if x.lower() in new:  # str.lower()只能直接作用与字符串
        print(x + ',You need to input a another name.')
    else:
        print(x + ",This name is availiable.")

#5-11

list = range(1,10)
for x in list[:]:
    if x == 1:
        print('1st')
    elif x == 2:
        print('2nd')
    elif x == 3:
        print('3rd')
    else:
        print(x,"th")   # "," 必须
       
