                                                Introducing Lists
# use [] as list

#3-1  #访问列表元素

name = ["Mikoto Misaka","Tom","Jerry"]
print(name[0])
print(name[1])
print(name[2])# same as print(name[-1])

#3-2 for in

#3-4

name = ['Mikoto Misaka','Ogiso Setsuna','Tōma Kazusa','Mizusawa Io']
print("Hello,"+ name[0] + "," + "I would like to invite you to have a dinner with me")
print("Hello,"+ name[1] + "," + "I would like to invite you to have a dinner with me")
print("Hello,"+ name[2] + "," + "I would like to invite you to have a dinner with me")
print("Hello,"+ name[3] + "," + "I would like to invite you to have a dinner with me")

#3-5

print("I just konw that",name[-1] + " " + "can't come because she have a practice.")
name[-1] = "和泉千晶"   #izumi chiaki  #修改元素值
print("Hello,"+ name[0] + "," + "I would like to invite you to have a dinner with me")
print("Hello,"+ name[1] + "," + "I would like to invite you to have a dinner with me")
print("Hello,"+ name[2] + "," + "I would like to invite you to have a dinner with me")
print("Hello,"+ name[3] + "," + "I would like to invite you to have a dinner with me")

#3-6

print("I find a bigger table that can contain more people.")
name.insert(0,"涼宮春日")  #　suzumiya haruhi  insert任意位置插入
name.insert(2,"長門有希")   #　nagato yuki
name.append("朝比奈みくる") #　asahina mikuru  append添加至列表末尾
x = name[:]
print("Hello,"+ name[0] + "," + "I would like to invite you to have a dinner with me")
print("Hello,"+ name[1] + "," + "I would like to invite you to have a dinner with me")
print("Hello,"+ name[2] + "," + "I would like to invite you to have a dinner with me")
print("Hello,"+ name[3] + "," + "I would like to invite you to have a dinner with me")
print("Hello,"+ name[4] + "," + "I would like to invite you to have a dinner with me")
print("Hello,"+ name[5] + "," + "I would like to invite you to have a dinner with me")
print("Hello,"+ name[6] + "," + "I would like to invite you to have a dinner with me")

#3-7  #删除元素

print("I'm sorry to tell you that wo can only invite two of you because the table is on the way.")
print("I'm sorry that you can't come with us for dinner,sorry" + " " + name.pop() + "." ) #pop删除末尾值，并使用这个值
print("I'm sorry that you can't come with us for dinner,sorry" + " " + name.pop() + "." ) #pop也可删除任意位置，如name.pop(-1)
print("I'm sorry that you can't come with us for dinner,sorry" + " " + name.pop() + "." )
print("I'm sorry that you can't come with us for dinner,sorry" + " " + name.pop() + "." )
print("I'm sorry that you can't come with us for dinner,sorry" + " " + name.pop() + "." )
print("I'm glad that you can come with us for dinner," +  name[0] + "." )
print("I'm glad that you can come with us for dinner," +  name[1]+ "." )
print(name)
name.remove('涼宮春日') #del name[0]效果一样
name.remove('Mikoto Misaka')  #remove是根据值来删除，与位置无关
print(name)

#3-8

places = ['los_Angeles','london','firenze','changbai_Mountains','kyoto']  #kyoto　京都
print(places)
print(sorted(places))   #顺序排列
print(places)   #检验，sorted不改变原列表值，sort永久性改变
print(sorted(places,reverse = True))    #反转排列
print(places)
places.reverse()    #反转排列，改变places的值，此时将66-67合并成 print(places.reverse())则返回值为NONE
print(places)
places.reverse()    #再反转则变回来了，reverse跟首字母顺序无关，就是反转元素原来排列顺序
print(places)
places.sort()
print(places)   # 同上，合并成print(places.sort())则返回值为none
places.sort(reverse = True) #按反序排列
print(places)   #sort跟sorted用法不同

#3-9

print(len(x)) #len()获得列表长度
