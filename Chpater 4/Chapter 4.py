                                                  Working with Lists
#4-1

for name in  pizza:     #for循环便利整个列表，pizza列表没想好填什么就空着
    #print(name)
    print("I don't like" + name + "," + "I like pepperoni pizza!")
print("I really love pizza,")

#4-2

animal = ['cat','dog','beer']
for food in animal: #for循环缩进很重要
        #print(food)
        print("A " + food + " " + "would make a great pet.")
print("Any of these animals would make a great pet!")

#4-3

number = [value for value in range(1,21,1)] #range（）生成一系列数字，从1开始，不断增加1，直到达到或超过21
print(number)   #所以number列表值从1到20，没有21

#4-4

number = [value for value in range(1,1000001)]  #不会从1到1000001，只会到1000000
print(number)


#4-5    #统计数字列表值

print(min(number))
print(max(number))
print(sum(number))


#4-6

number = [value for value in range(1,21,2)]
print(number)

#4-7

number = [value for value in range(3,31,3)]
print(number)

#4-8

number = [value ** 3 for value in range(1,11)]  #列表解析，将for循环和创建新元素代码合为一行，前面表达式value ** 3，后面是赋值，**乘方
print(number)   #number = [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

#4-9

list(range(1,1001)) #创建数字列表

#4-10
# 切片，列表的一部分
print("The first three items in the list are:" + str(number[0:3]) +".")
print("Three items from the middle of the list are:" + str(number[4:7]) +".")
print("The last three items in the list are:" + str(number[7:11]) +".")

#4-11

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

my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:]  #复制列表
print("My favorite foods are:")
for value in my_foods:
    print(value[:])
print("\nMy friend's favorite foods are:")
for value in friend_foods:
    print(value[:])

#4-13
# 元组，列表是可修改的，元组不可修改，元组是不可修改的列表，用()表示，元组不可修改，但是可以重新赋值
restaurant = ('water','rice','meat','vegetables','milk')
for value in restaurant:
    print(value)
# restaurant[2]= 'boom'
restaurant = ('water','rice','leaf','vegetables','noddles')
for value in restaurant:
    print(value)
