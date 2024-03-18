# modules part one

# import random
# print(random.random())
# print(dir(random)) # dir(module) gets all functions and classes in the module 

# from random import randint , randrange
# print(randint(100,1000000))
# print(randrange(100,1000000))
# part two 
# import module as myModule
# import sys
# sys.path.append(r"D:\muhammad\programming\python\elzeroPython\modules")
# print(sys.path)
# print(myModule.say_hello("name"))

# from module import say_hello as sH
# print(sH("name"))

# part three install packages
# pip install 
# pip install packageone packagetwo packagethree etc
# pip install package==versionNum
# pip install package>=versionNum

import termcolor
import pyfiglet
print(dir(pyfiglet))

print(pyfiglet.figlet_format("MUHAMMED"),termcolor.colored("MUHAMMED",color="light_red"))