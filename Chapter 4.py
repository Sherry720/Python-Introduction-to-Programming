#4-1
#比萨 ：想出至少三种你喜欢的比萨，将其名称存储在一个列表中，再使用for 循环将每种比萨的名称都打印出来。
#修改这个for 循环，使其打印包含比萨名称的句子，而不仅仅是比萨的名称。对于每种比萨，都显示一行输出，如“I like pepperoni pizza”。 
#在程序末尾添加一行代码，它不在for 循环中，指出你有多喜欢比萨。输出应包含针对每种比萨的消息，还有一个总结性句子，如“I really love pizza!”

pizza = ['pizza_0','piaaz_1','pizza_2']
x = pizza[:]
for name in  pizza:
    #print(name)
    print("I don't like" + name + "," + "I like pepperoni pizza!")
print("I really love pizza,")

#4-2
#动物 ：想出至少三种有共同特征的动物，将这些动物的名称存储在一个列表中，再使用for 循环将每种动物的名称都打印出来。 
#修改这个程序，使其针对每种动物都打印一个句子，如“A dog would make a great pet”。 
#在程序末尾添加一行代码，指出这些动物的共同之处，如打印诸如“Any of these animals would make a great pet!”这样的句子。

animal = ['cat','dog','beer']
for food in animal:
        #print(food)
        print("A " + food + " " + "would make a great pet.")
print("Any of these animals would make a great pet!")

#4-3
#数到20 ：使用一个for 循环打印数字1~20.
number = [value for value in range(1,21,1)]
print(number)

#4-4
#一百万 ：创建一个列表，其中包含数字1~1 000 000，再使用一个for 循环将这些数字打印出来（如果输出的时间太长，按Ctrl + C停止输出，或关闭输出窗口）。
number = [value for value in range(1,1000001)]
print(number)

#4-5
#计算 计算1~1 000 000的总和 的总和 ：创建一个列表，其中包含数字1~1 000 000，再使用min() 和max() 核实该列表确实是从1开始，到1 000 000结束的。另外，对这个列表 调用函数sum() ，看看Python将一百万个数字相加需要多长时间。
print(min(number))
print(max(number))
print(sum(number))


#4-6
#奇数 ：通过给函数range() 指定第三个参数来创建一个列表，其中包含1~20的奇数；再使用一个for 循环将这些数字都打印出来。
number = [value for value in range(1,21,2)]
print(number)

#4-7
#3的倍数：创建一个列表，其中包含3~30内能被3整除的数字；再使用一个for 循环将这个列表中的数字都打印出来.
number = [value for value in range(3,31,3)]
print(number)

#4-8
#立方：将同一个数字乘三次称为立方。例如，在Python中，2的立方用2**3 表示。请创建一个列表，其中包含前10个整数（即1~10）的立方，再使用一个for 循 环将这些立方数都打印出来。 
number = [value ** 3 for value in range(1,11)]
print(number)

#4-9
#立方解析 ：使用列表解析生成一个列表，其中包含前10个整数的立方
list(range(1,1001))

#4-10
#切片：选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。 
#打印消息“The first three items in the list are:”，再使用切片来打印列表的前三个元素。 
#打印消息“Three items from the middle of the list are:”，再使用切片来打印列表中间的三个元素。 
#打印消息“The last three items in the list are:”，再使用切片来打印列表末尾的三个元素。 
print("The first three items in the list are:" + str(number[0:3]) +".")
print("Three items from the middle of the list are:" + str(number[4:7]) +".")
print("The last three items in the list are:" + str(number[7:11]) +".")

#4-11
#你的比萨和我的比萨：在你为完成练习4-1而编写的程序中，创建比萨列表的副本，并将其存储到变量friend_pizzas 中，再完成如下任务。
#在原来的比萨列表中添加一种比萨。 
#在列表friend_pizzas 中添加另一种比萨。 
#核实你有两个不同的列表。为此，打印消息“My favorite pizzas are:”，再使用一个for 循环来打印第一个列表；打印消息“My friend's favorite pizzas are:”，再使用一 个for 循环来打印第二个列表。核实新增的比萨被添加到了正确的列表中。 

friend_pizzas = x [:]
x.append('blue')
friend_pizzas.append('white')
print("My favorite pizzas are:\n")
for pizza in x:
    print(pizza[:])
print("My friend's favorite pizzas are:\n")
for pizza in friend_pizzas:
    print(pizza[:])

#4-12
#使用多个循环 ：在本节中，为节省篇幅，程序foods.py的每个版本都没有使用for 循环来打印列表。请选择一个版本的foods.py，在其中编写两个for 循环，将各 个食品列表都打印出来。
my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:]
print("My favorite foods are:")
for value in my_foods:
    print(value[:])
print("\nMy friend's favorite foods are:")
for value in friend_foods:
    print(value[:])

#4-13
#自助餐 ：有一家自助式餐馆，只提供五种简单的食品。请想出五种简单的食品，并将其存储在一个元组中。 
#使用一个for 循环将该餐馆提供的五种食品都打印出来。 
#尝试修改其中的一个元素，核实Python确实会拒绝你这样做。 
#餐馆调整了菜单，替换了它提供的其中两种食品。请编写一个这样的代码块：给元组变量赋值，并使用一个for 循环将新元组的每个元素都打印出来。

restaurant = ('water','rice','meat','vegetables','milk')
for value in restaurant:
    print(value)
# restaurant[2]= 'boom'
restaurant = ('water','rice','leaf','vegetables','noddles')
for value in restaurant:
    print(value)
