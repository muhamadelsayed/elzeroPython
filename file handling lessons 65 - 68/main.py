# lesson one
# import os = operating system
# import os
# print(os.getcwd()) #current working directory
# print(os.path.abspath(__file__)) # returns aabsoulute path for the file
# print(os.path.dirname(os.path.abspath(__file__)))

# # change current directory
# os.chdir(f"{os.getcwd()}/new directory")


# print(os.getcwd()) #current working directory
# # file = open("txt.txt")

# read method
# myFile = open("txt.txt","r")
# print(myFile)
# print(myFile.read())
# print("______"*10)
# print(myFile.read(5)) # first five charcters

# print(myFile.readline(5)) # read first five charcters from line 1
# print(myFile.readline()) # read last charcters in line 1
# print(myFile.readline()) # read line two
# print(myFile.readlines()) # give list with every line

# for line in myFile:
#     print(line)
#     if line.startswith("te5"):
#         break

# now close the file it is best practice
# myFile.close()
# print(myFile.read()) # ValueError: I/O operation on closed file.
# write and append in files

# if file not in "w" make one
# it deletes old and make new
# writeFile = open("I'haveWritten","w") 
# writeFile.write("hello from python\n")
# writeFile.write("sec line hello from python\n")

# myList = ["1\n","2\n","3\n","4\n","5\n"]
# writeFile.writelines(myList)

# "a" for append
# it also make file if its not excuted
# appendFile = open("append.txt","a")
# appendFile.write("appended not deleted \n")
# appendFile.write("Testing position \n")
# appendFile.truncate(10) # make it like write method "w"

# last lesson notes
lastTry = open("I'haveWritten.txt","r")
# lastTry.write("etc\n")
lastTry.seek(7) # start from any index
print(lastTry.read())
# print(lastTry.tell()) # where is cursor
# import os
# os.remove("") path to file


