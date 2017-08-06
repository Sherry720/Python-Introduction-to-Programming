#10-1

file_name = 'C:\\Users\\pengc\\Documents\\Visual Studio 2017\\Projects\\files\\files\\learning Python.txt'
with open(file_name,'r') as file_object:
    contentt = file_object.read()
    print(contentt.strip())
with open(file_name) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.strip())

#10-2

for line in lines:
    print(line.strip().replace('python','C'))

#10-3


file_name = 'guest.txt'
with open(file_name,'w') as file_object:
    file_object.write(input("Please input your name here:\n" + "-").title())


file_name = 'guest_book.txt'
with open(file_name,'w') as file_object:
        active = True
        while active:
            name = input("Please input your name here:\n" + "-").title()
            if name == 'Q':
                break
            else:
                file_object.write(name + '\n')
                print("glad to see you")

#10-4
file_name = 'reason.txt'
with open(file_name,'w') as file_object:
        active = True
        while active:
            name = input("Please input your reason that why you like to programing :\n" + "-").title()
            if name == 'Q':
                break
            else:
                file_object.write(name + '\n')
      
                
#10-6
a = input()
b = input()
try:
    a = int(a)
    b = int(b)
    sum = a + b
except ValueError:
    print("we need the number.")
else:
    print(sum)
    
#10-7
while True:
    a = input()
    if a == 'q':
        break
    b = input()
    try:
        a = int(a)
        b = int(b)
        sum = a + b
    except ValueError:
        pass
    else:
        print(sum)
        
#10-8
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print("\nReading file: " + filename)
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print("  Sorry, I can't find that file.")

#10-9
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print("\nReading file: " + filename)
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        pass
    else:
        print("  Sorry, I can't find that file.")
        

#10-10
filename = 'F:\\日常\\书籍\\Harry potter\\.txt'
with  open(filename) as files:
    contents = files.read()
    i = contents.count('你')
    print(i)

#10-11

import json
number = input("What's your favorite number:\n" + "-")
file = 'number.json'

with open(file,'w') as f:
    json.dump(number,f)

with open(file) as f1:
    saved = json.load(f1)
    print("I konw your favorite number,it's:" 
          + "-" 
          + saved
          )
    
#10-12

import json
file = 'number.json'

try:
    with open(file) as f1:
        saved = json.load(f1)
        print("I konw your favorite number,it's:\n" 
              + "-" 
              + saved
              )
except FileNotFoundError:
    number = input("What's your favorite number:\n" + 
                   "-"
                   )
    with open(file,'w') as f:
        json.dump(number,f)
        print("I remember your favorite number is:\n" +
              "-" +
              number
              )
else:
    print("Welcome back!")
    
#10-13

import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        correct = input("Are you " + username + "? (y/n) ")
        if correct == 'y':
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()
