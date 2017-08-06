#4-1

x = pizza[:]
for name in  pizza:
    #print(name)
    print("I don't like" + name + "," + "I like pepperoni pizza!")
print("I really love pizza,")

#4-2

animal = ['cat','dog','beer']
for food in animal:
        #print(food)
        print("A " + food + " " + "would make a great pet.")
print("Any of these animals would make a great pet!")

#4-3

number = [value for value in range(1,21,1)]
print(number)

#4-4

number = [value for value in range(1,1000001)]
print(number)

#4-5

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

number = [value ** 3 for value in range(1,11)]
print(number)

#4-9

list(range(1,1001))

#4-10

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
friend_foods = my_foods[:]
print("My favorite foods are:")
for value in my_foods:
    print(value[:])
print("\nMy friend's favorite foods are:")
for value in friend_foods:
    print(value[:])

#4-13

restaurant = ('water','rice','meat','vegetables','milk')
for value in restaurant:
    print(value)
# restaurant[2]= 'boom'
restaurant = ('water','rice','leaf','vegetables','noddles')
for value in restaurant:
    print(value)
