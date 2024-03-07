# lesson one
# import os = operating system
import os
print(os.getcwd()) #current working directory
print(os.path.abspath(__file__)) # returns aabsoulute path for the file
print(os.path.dirname(os.path.abspath(__file__)))

# change current directory
os.chdir(f"{os.getcwd()}/new directory")


print(os.getcwd()) #current working directory
# file = open("txt.txt")