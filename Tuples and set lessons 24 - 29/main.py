# Tuples #24

# () or without
# myTuble1 = (1,2,3)
# myTuble2 = 1,2,3
# print(type(myTuble1))
# print(type(myTuble2))
# myTuble3 = (1,2,3,4,5)
# print(myTuble3[0])
# print(myTuble3[-1])
# you  can't edit in it
# myTuble3[0] = "one"
# print(myTuble3) #error

# tuble lesson two

# if one element and no () add ,
# myTuble5 = 1,
# print(type(myTuble5))

# a = (1,2,3,4,5,5,5)
# b = (5,6,7)
# c = a + b
# print(c)
# d = "mo"
# e = [1,2]
# f = ("a","b")
# print(d * 6)
# print(e * 6)
# print(f * 6)

# count()
# print(a.count(5))
# index() same indexof js

# tuple destruct 
# a = (1,2,3)
# x,y,z = a
# print(x)
# print(y)
# print(z)
# if there is more just  add _, in its place and it must be spicific in the places to declare
# b = (1,2,3,"ignore",4)
# x,_,y,_,z = b
# print(x)
# print(y)
# print(z)

# set lesson 1 
# {}
# no order thus no indexing and no slicing
# no list or dictionary in it
# set is unque like js
# setone = {"one",1,2,True}
# print(setone)
# uniqueSet = {1,1,1,1,1,1,1,1,1,21,2,2}
# print(uniqueSet)

# set lesson 2

# clear() same

# union()
# b = {1,2,3}
# c = {4,5,6}
# d = {"cool"}
# print(b | c)
# print(b.union(c,d))

# add()
# f = {"etc"}
# f.add("etc2")
# f.add("etc3")
# print(f)

# copy() same

# remove() same error if not found
# discard() remove but doesn't give error if not found

# pop() get random element in the tuble or any type of data
# print(f.pop())

# update() adds new tuple
# g = {1,2,3,4}
# f.update(g)
# print(f)

# set lesson 3

# difference() get elements in set one that doesnot in set 2

# a = {1,2,3,5}
# b = {5,3,"one"}
# # print(a.difference(b)) 
# # # same in a- b
# # print(a - b)

# # difference_update it updates other one didn't
# a.difference_update(b)
# print(a)

# print("=" * 40)

# intersection() get elements that is in both tuples
# e = {1,2,3,4,5,"x",8}
# f = {"x",2,6,7}
# print(e.intersection(f)) #e & f
# # e.intersection(f) # no change
# # print(e) 
# # e.intersection_update(f)
# # intersection_update()
# print(e)
# # symmitric_differnce gets elements that not shared in both
# print(e ^ f) # shortcut
# print(e.symmetric_difference(f))
# # symmetric_difference_update()
# e.symmetric_difference_update(f)
# print(e)

# set lesson 4 

# issuperset(set2) checks if the set2 is all in the set1 and returns boolean
a = {1,2,3,"etc",4}
b = {1,2}
c = {6,7}
# print(a.issuperset(b))
# print(a.issuperset(c))

# issubset(set2) check if all set1 elements in set2 and returns boolean
print(a.issubset(b))
print(b.issubset(a))

# isdisjoint() check is separated