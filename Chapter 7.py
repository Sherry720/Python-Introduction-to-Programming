#7-1
#汽车租赁:编写一个程序，询问用户要租赁什么样的汽车，并打印一条消息，如“Let me see if I can find you a Subaru”
print(input("What's car you want? " ) + "\nLet me see if I can find you a Subaru")

#7-2
#餐馆订位：编写一个程序，询问用户有多少人用餐。如果超过8人，就打印一条消息，指出没有空桌；否则指出有空桌。
x = input("How much people are ready to have lunch? ")
print(x)
if int(x) > 8:
    print("We don't have more tables.")
else:
    print("We  have more tables.")

#7-3
#10的整数倍：让用户输入一个数字，并指出这个数字是否是10的整数倍。 
x = input()
if int(x) % 10 == 0:
    print("\nThis number can be divid by 10.")
else:
    print("\nThis number can't be divid by 10.")

#7-4
# 比萨配料：编写一个循环，提示用户输入一系列的比萨配料，并在用户输入'quit' 时结束循环。
# 每当用户输入一种配料后，都打印一条消息，说我们会在比萨 中添加这种配料。
active = True
while active:
    x = input("Please input some food: ")
    if x == 'quit':
        active = False
    else:
        print(x)

#7-5
#电影票：有家电影院根据观众的年龄收取不同的票价：
#不到3岁的观众免费；
#3~12岁的观众为10美元；
#超过12岁的观众为15美元。
#请编写一个循环，在其中询问用户的年龄，并指出其票价。

x = input("Please tell us your age: ")
while int(x) < 3:
    print("you are free!\n")
    break
while  3 < int(x) < 12:
    print("you need to pay 10$.\n")
    break
while  int(x) > 12:
    print("you need to pay 15$.\n")
    break

#7-6
#三个出口 ：以另一种方式完成练习7-4或练习7-5，在程序中采取如下所有做法。 
#在while 循环中使用条件测试来结束循环。 
#使用变量active 来控制循环结束的时机。 
#使用break 语句在用户输入'quit' 时退出循环。

active =True
while active:
    x = input("Please tell us your age: ")
    while int(x) < 3:
        print("you are free!\n")
        break
    while  3 < int(x) < 12:
        print("you need to pay 10$.\n")
        break
    while  int(x) > 12:
        print("you need to pay 15$.\n")
        active = False
        break

#7-7
#无限循环 ：编写一个没完没了的循环，并运行它（要结束该循环，可按Ctrl +C，也可关闭显示输出的窗口）。
#while True:
#    print(input(" ^_^ "))
  
#7-8
#熟食店 ：创建一个名为sandwich_orders 的列表，在其中包含各种三明治的名字；
#再创建一个名为finished_sandwiches 的空列表。
#遍历列表sandwich_orders,对于其中的每种三明治,都打印一条消息,如I made your tuna sandwich,并将其移到列表finished_sandwiches.
#所有三明治都制作好后，打印一条消息，将这些三明治列出来。

sandwich_orders = ['white','blue','red']
finished_sandwiches = []
for x in sandwich_orders[:]:
    print("I made your " + x + " sandwich.")
    finished_sandwiches.append(x)
print("I have made the white,blu,red sandwiches.")

#7-9
#五香烟熏牛肉（pastrami）卖完了：使用为完成练习7-8而创建的列表sandwich_orders ，并确保'pastrami' 在其中至少出现了三次。
#在程序开头附近添加 这样的代码：打印一条消息，指出熟食店的五香烟熏牛肉卖完了；
#再使用一个while 循环将列表sandwich_orders 中的'pastrami' 都删除。
#确认最终的列 表finished_sandwiches 中不包含'pastrami' 。

print("Pastrami have seld out.")
sandwich_orders = ['white','blue','red','pastrami','pastrami','pastrami']
print(sandwich_orders)
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

#7-10
# 梦想的度假胜地：编写一个程序，调查用户梦想的度假胜地。
# 使用类似于“If you could visit one place in the world, where would you go?”的提示，并编写一个打印调查 结果的代码块。

active = True
places = []
while active:
    x = input("If you could visit one place in the world, where would you go: ")
    places.append(x)
    again = input("If you like to invite others to fill this? (Yes/No) ")
    if again == 'no':
        active = False
print(places)

