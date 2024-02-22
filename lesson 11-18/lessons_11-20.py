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
# print("muhammed".startswith("m",4))
# print("muhammed".endswith("dX"))
# #  index like not same same is find indexof js search word,serch start ,search end 
# print("muhammed".index("m"))
# # print("muhammed".index("x")) # gives error
# # find same index of
# print("muhammed".index("x"))
# splitlinesvar = """line 1
# line 2
# line3"""
# print(splitlinesvar.splitlines())
# one = "I love python"
# two = "I Love Python"
# # is title
# print(one.istitle())
# print(two.istitle())
# # smae isspace
# # same islower() isupper()
# alpha = "asalkfjgohdsohfu"
# print(alpha.isalpha()) 
# also isalnum() checks that has nums or str

# replace
# a = "hello js"
# a.replace("js","python","num of times to replace opitinal")
# a = a.replace("js","python")
# print(a)
# # join arr to str "empty or separator".join(var)
# joinmethod = ["etc1","2","3","4"]
# print("-".join(joinmethod))
# name = "name"
# age = "age"
# # you cannot print (name + "str" + age) you get error
# # thus we need formatting in python
# print("myname is %s" % name) # %s add what after % in its place
# print("my name is %s and my age is %s" % (name,age)) # %d for digits %f for float also %.num of floats f
# n = "name"
# # l = "python"
# y = 10
# # # print("my name is %s and iam a %s develeper and ex is %d" % (n,l,y))
# # # print("etc %.2f" %(y))
# # # also %.numofindexes s
# # print("name is %.3s" % n)
# # last lesson 18 new formatting
# print("name : {:s} and float {:f} and digit {}".format(n,y,y)) # in {opetional}
# mymoney = 7646969439385874365987695869386879
# print("my money is i mean separate digits {:_}".format(mymoney))
# a,b,c = "one","two","three"
# # while {} inside it is opitional we can add indexes into it 
# print("try {2} {0} {1}".format(a,b,c)) # {2:.3f}
# like js
# just add f before "" 
# myName = "muhammed"
# age = 17
# print(f"myname is {myName} and my age is {age}") 
