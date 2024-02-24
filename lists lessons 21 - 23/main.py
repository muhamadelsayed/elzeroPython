# list lesson 1
myList = ["one","two","one",True,100.5]
# print(myList)
# print(myList[-2])
# # myList = myList[1:-1]
# myList = myList[1:] #same
# print(myList)
# print(myList[::2])
# myList[0] = "edited"
# print(myList)
# myList[0:2] = ["a","b","c"]
# myList[0:-1] = []
# print(myList)

# list methods 1
# list.append(any)
# myList.append("newman")
# print(myList)
# myList.append(["newman2",3])
# print(myList[-1][-1])

# # list.extend(any)
# a = [1,2,3]
# b = [4,5,6]
# a.extend(b)
# print(a)

# # remove() removes first element in ()
# x = [1,1,1,2,3,4,5]
# x.remove(1)
# print(x)

# sort()
# y = [-7,9000,-10]
# y.sort()
# print(y)
# y.sort(reverse=True)
# print(y)

# reverse() just reverse the list
# z = [1,2,1,3]
# z.reverse()
# print(z)

# list methods part 2

# clear() clears list
# a = [1,2,3,4,5]
# a.clear()
# print(a)

# # copy()
# b = [1,2,3,4,5,6]
# c = b.copy()
# print(c)
# c.append(a) #its cleared :D
# print(c)

# count(etc) count how many times etc occured in the list
# d = [1,1,1,1,1,1,1,1,1,1,1,1,2,3]
# print(d.count(1))

# list.index(etc) its like indexOf in js

# insert(num to insert before it , value)
# f = [1,2,3,4]
# f.insert(0,"one")
# print(f)

# pop(index)
a = [1,2,3,4]
print(a.pop(0))
# deleted
print(a)