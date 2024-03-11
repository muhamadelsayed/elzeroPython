# # i just added new
# def my_function(*kids):
#   print(kids)
#   print(type(kids)) # returns a tuple in *arguments

# my_function("Emil", "Tobias", "Linus")

# way to add without order 
# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# def my_function(**kid):
#   print("His last name is " + kid["lname"])
#   print(kid)
#   print(type(kid)) #obj

# same default val 

# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()

# same return
# def my_function(x):
#   return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

# if a func is empty add pass to stop error
# def myfunction():
#   pass 

# You can combine the two argument types in the same function.

# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
# def my_function(a, b, /, *, c, d):
#   print(a + b + c + d)

# my_function(5, 6, c = 7, d = 8)

# next is rescurtion andlabda

