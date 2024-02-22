# strings
# mystringone = "this is str"
# mystringtwo = "this is 'str'"
# print(mystringone)
# print(mystringtwo)
# mystringthree= '''
#     etc
# '''
# print(mystringthree)
# string indexing
# mystringone = "flask"
# print(mystringone[0])
# print(mystringone[2])
# print(mystringone[-1])
# # slice
# mystringtwo = "flask etc"
# print(mystringtwo[2:-1])
# print(mystringtwo[:3])
# print(mystringtwo[::3])
# # methods
# # len(variable) => returns variable.length also count spaces
# name = "  muhammed  "
# num = len(name)
# print(name,":",num)
# # var.strip() => removes spaces right and left , var.rstrip() for right , var.lstrip() => for left
# name2 = name.strip()
# print(name2)
# print(len(name2))
# name3 = "#$#$etc#$#$"
# print(name3.strip("#$#$"))
# var.title makes it first letter capital and letters after nums
# var.capitalize() it likes title but no for nums
# name = "muhammed".capitalize()
# print(name)
# var.zfill(num) => adds 00 before num like 00032
# a,b,c = "1","10","100"
# print(a.zfill(3),b.zfill(3),c)
# name = "moHaMeD"
# # upper and lower
# print(name.upper())
# print(name.lower())
# var.split() returns arr
# arr = "str srt ;orem lorem".split()
# print(arr)

# arr2 = "str srt ;orem lorem".split(" ",1)
# print(arr2)

# arr3 = "str srt ;orem lorem".rsplit(" ",2)
# print(arr3)
# print("str".center(10))
# print("str".center(10,"#")) # add ten # and center it

# count()
# countmethod = "js js js php flask".count("js",3)
# print(countmethod) 

# # swapcase()
# print("muhaMMED".swapcase())

# startswith()
# endswith()
print("muhammed".startswith("m",4))
print("muhammed".endswith("dX"))


