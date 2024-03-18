# built in functions part 3
# abs(num) same abs |num|
# pow() => power
# print(pow(2,5,10)) # 2^5%10

# # min(items,iterator)
# print(min(0,12,558486,85))
# print(min("a","b","c"))
# max()
# # slice()
# a = [1,2,3,4,5,6,7,8]
# print(a[2:5])
# print(a[slice(2,5)]) 

# map

# def formatText(text):

#     return f"- {text} -"

# myText = [1,2,3,4,5,6,7]

# myFormatData = map(formatText,myText)

# print(myFormatData)

# for name in myFormatData:
#     print(name)
# print(list(map(lambda text : f"- {text} -",myText)))
# for name in list(map(lambda text : f"- {text} -",myText)):
#     print(name)

# filter
# arr = [1,2,3,4,5,6]

# def checkNum(num):
#     return num < 5
    
# myResault = filter(checkNum,arr)
# for num in myResault:
#     print(num)

# def names(names):
#     return len(names) > 4
# resault = filter(names,["jggf","gr","Grgeter"])
# print(list(resault))


# resault = filter(lambda names:len(names) > 4 ,["jggf","gr","Grgeter"])
# print(list(resault))

# reduce()

# from functools import reduce


# # def sumAll(num1,num2):
# #     return num1 + num2

# numbers = [1,2,3,4,5,6,7,8,9]


# # result = reduce(sumAll,numbers)
# # print(result)
# result = reduce(lambda num1,num2: num1 + num2,numbers)
# print(result)


# enumerate(iterable,[option start])
# mySkills = ['html','css','js','nodejs']

# counter = list(enumerate(mySkills,50))
# print(counter)

# from functools import reduce


# print(help(help))

# reversed
# print(list(reversed([1,2,3])))