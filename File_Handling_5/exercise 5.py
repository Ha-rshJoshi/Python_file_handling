
# Question 1
filename=input("Enter file name: ")
with open(filename, 'r') as f:
    data=f.read()
print("The content of the file is")
print(data)

# Question 2

import mymod
mymod.countline("file.txt")
mymod.countchar("file.txt")
mymod.test("file.txt")

# Question 3
from mymod import countline,countchar,test
countchar("file.txt")
countline("file.txt")
test("file.txt")
from mymod import *
countline("file.txt")
countchar("file.txt")
test("file.txt")

# Question 4
def countline(name):
    count = 0
    with open(name,'r') as f:
        for line in f:
            count += 1
    print("total number of lines present: ",count)
def countchar(name):
    count = 0
    with open(name,'r') as f:
        for line in f:
            count+=len(line)
    print("total number of characters present: ",count)
def test(name):
    countline(name)
    countchar(name)

if __name__ == '__main__':
    filename= input("Enter file name: ")
    test(filename)

# Question 5
import mymod
filename= input("enter file name: ")
mymod.countline(filename)
mymod.countchar(filename)
mymod.test(filename)

from mymod import countchar,countline
filename= input("Enter file name: ")
countchar(filename)
countline(filename)

# Question 6
import File_Handling_5.mymod
File_Handling_5.mymod.test("file.txt")

# Question 7
import changer
changer.message()
def message1():
    print("Message is changed now")
import importlib
importlib.reload(changer)
changer.message1()

