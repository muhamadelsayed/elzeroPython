# recursion function
# x = "wwwoooorrrldd"
# def cleanWord(word):
#     if len(word)==1:
#         return word
#     if word[0] == word[1]:
#         return cleanWord(word[1:])
#     return word[0] + cleanWord(word[1:])
    
# print(cleanWord(x))

# lambda arrow function

def say_hello(user):return print(f"Hello {user}")
say_hello("muhammed")

hello = lambda name,age : f"hello {name} and age is {age}"
print(hello("mo",45))
print(hello.__name__)

