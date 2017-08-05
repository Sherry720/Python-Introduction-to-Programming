# 列表

#3-1
#姓名： 将一些朋友的姓名存储在一个列表中，并将其命名为names 。依次访问该列表中的每个元素，从而将每个朋友的姓名都打印出来。

name = ["Mikoto Misaka","Tom","Jerry"]
print(name[0])
print(name[1])
print(name[2])# same as print(name[-1])

#3-2 for in
#问候语： 继续使用练习3-1中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名.
#message = "Hey,",guys,"how's it going?"  
#print(guys)

#3-3
#自己的列表： 想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。根据该列表打印一系列有关这些通勤方式的宣言，如“I would like to own a Honda motorcycle”。
#   there is no translation for me

#3-4
#嘉宾名单 ：如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），你会邀请哪些人？请创建一个列表，其中包含至少3个你想邀请的人；然后，使用 这个列表打印消息，邀请这些人来与你共进晚餐。

name = ['Mikoto Misaka','Ogiso Setsuna','Tōma Kazusa','Mizusawa Io']
print("Hello,"+ name[0] + "," + "I would like to invite you to have a dinner with me")
print("Hello,"+ name[1] + "," + "I would like to invite you to have a dinner with me")
print("Hello,"+ name[2] + "," + "I would like to invite you to have a dinner with me")
print("Hello,"+ name[3] + "," + "I would like to invite you to have a dinner with me")

#3-5
#修改嘉宾名单 ：你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。 
#以完成练习3-4时编写的程序为基础，在程序末尾添加一条print 语句，指出哪位嘉宾无法赴约。 
#修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。 
#再次打印一系列消息，向名单中的每位嘉宾发出邀请。

print("I just konw that",name[-1] + " " + "can't come because she have a practice.")
name[-1] = "和泉千晶"   #izumi chiaki
print("Hello,"+ name[0] + "," + "I would like to invite you to have a dinner with me")
print("Hello,"+ name[1] + "," + "I would like to invite you to have a dinner with me")
print("Hello,"+ name[2] + "," + "I would like to invite you to have a dinner with me")
print("Hello,"+ name[3] + "," + "I would like to invite you to have a dinner with me")

#3-6
#添加嘉宾 ：你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。 
#以完成练习3-4或练习3-5时编写的程序为基础，在程序末尾添加一条print 语句，指出你找到了一个更大的餐桌。
# 使用insert() 将一位新嘉宾添加到名单开头。 
# 使用insert() 将另一位新嘉宾添加到名单中间。 
# 使用append() 将最后一位新嘉宾添加到名单末尾。 
# 打印一系列消息，向名单中的每位嘉宾发出邀请。

print("I find a bigger table that can contain more people.")
name.insert(0,"涼宮春日")  #　suzumiya haruhi
name.insert(2,"長門有希")   #　nagato yuki
name.append("朝比奈みくる") #　asahina mikuru  append不返回值
x = name[:]
print("Hello,"+ name[0] + "," + "I would like to invite you to have a dinner with me")
print("Hello,"+ name[1] + "," + "I would like to invite you to have a dinner with me")
print("Hello,"+ name[2] + "," + "I would like to invite you to have a dinner with me")
print("Hello,"+ name[3] + "," + "I would like to invite you to have a dinner with me")
print("Hello,"+ name[4] + "," + "I would like to invite you to have a dinner with me")
print("Hello,"+ name[5] + "," + "I would like to invite you to have a dinner with me")
print("Hello,"+ name[6] + "," + "I would like to invite you to have a dinner with me")

#3-7
#缩减名单 ：你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。 
#以完成练习3-6时编写的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。 使用pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为止。
#每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进 晚餐。 
#对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。 
#使用del 将最后两位嘉宾从名单中删除，让名单变成空的。
#打印该名单，核实程序结束时名单确实是空的。 

print("I'm sorry to tell you that wo can only invite two of you because the table is on the way.")
print("I'm sorry that you can't come with us for dinner,sorry" + " " + name.pop() + "." )
print("I'm sorry that you can't come with us for dinner,sorry" + " " + name.pop() + "." )
print("I'm sorry that you can't come with us for dinner,sorry" + " " + name.pop() + "." )
print("I'm sorry that you can't come with us for dinner,sorry" + " " + name.pop() + "." )
print("I'm sorry that you can't come with us for dinner,sorry" + " " + name.pop() + "." )
print("I'm glad that you can come with us for dinner," +  name[0] + "." )
print("I'm glad that you can come with us for dinner," +  name[1]+ "." )
print(name)
name.remove('涼宮春日')
name.remove('Mikoto Misaka')
print(name)

#3-8
#放眼世界 放眼世界 ：想出至少5个你渴望去旅游的地方。 
#将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。 
#按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始Python列表。
#使用sorted() 按字母顺序打印这个列表，同时不要修改它。 
#再次打印该列表，核实排列顺序未变。 
#使用sorted() 按与字母顺序相反的顺序打印这个列表，同时不要修改它。
#再次打印该列表，核实排列顺序未变。 
#使用reverse() 修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。 
#使用reverse() 再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。 
#使用sort() 修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。 
#使用sort() 修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。

places = ['los_Angeles','london','firenze','changbai_Mountains','kyoto']  #kyoto　京都
print(places)
print(sorted(places))   #顺序排列
print(places)   #检验，sorted不改变原列表值
print(sorted(places,reverse = True))    #反转排列
print(places)
places.reverse()    #反转排列，改变places的值，此时将66-67合并成 print(places.reverse())则返回值为NONE
print(places)
places.reverse()    #再反转则变回来了
print(places)
places.sort()
print(places)   # 同上，合并成print(places.sort())则返回值为none
places.sort(reverse = True)
print(places)   #sort跟sorted用法不同

#3-9
#晚餐嘉宾 ：在完成练习3-4~练习3-7时编写的程序之一中，使用len() 打印一条消息，指出你邀请了多少位嘉宾.

print(len(x))

#3-10
#尝试使用各个函数 ：想想可存储到列表中的东西，如山岳、河流、国家、城市、语言或你喜欢的任何东西。编写一个程序，在其中创建一个包含这些元素的列 表，然后，对于本章介绍的每个函数，都至少使用一次来处理这个列表。

#3-11
#有意引发错误 ：如果你还没有在程序中遇到过索引错误，就尝试引发一个这种错误。在你的一个程序中，修改其中的索引，以引发索引错误。关闭程序前，务 必消除这个错误。 
