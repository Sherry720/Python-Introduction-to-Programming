#7-1

print(input("What's car you want? " ) + "\nLet me see if I can find you a Subaru")

#7-2

x = input("How much people are ready to have lunch? ")
print(x)
if int(x) > 8:
    print("We don't have more tables.")
else:
    print("We  have more tables.")

#7-3
。 
x = input()
if int(x) % 10 == 0:
    print("\nThis number can be divid by 10.")
else:
    print("\nThis number can't be divid by 10.")

#7-4

active = True
while active:
    x = input("Please input some food: ")
    if x == 'quit':
        active = False
    else:
        print(x)

#7-5

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


sandwich_orders = ['white','blue','red']
finished_sandwiches = []
for x in sandwich_orders[:]:
    print("I made your " + x + " sandwich.")
    finished_sandwiches.append(x)
print("I have made the white,blu,red sandwiches.")

#7-9


print("Pastrami have seld out.")
sandwich_orders = ['white','blue','red','pastrami','pastrami','pastrami']
print(sandwich_orders)
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

#7-10

active = True
places = []
while active:
    x = input("If you could visit one place in the world, where would you go: ")
    places.append(x)
    again = input("If you like to invite others to fill this? (Yes/No) ")
    if again == 'no':
        active = False
print(places)

