#1
import os.path
name_file = "myFile.txt"
def openfile(name_file):
    isExist = os.path.exists(name_file)
    if isExist == True:
        file = open(name_file,"r")
        print(f"{file.read()} \nSuccessfully print content in myFile.txt")
    elif isExist == False:
        print("Unable to open file myFile.txt")

openfile(name_file)
#2
def stripfile(): 
    while 1:
     
     file = open('myFile.txt', 'r')
     char = file.read().strip()         
     if not char:
       break
     return len(char)         
     file.close()

print("Total letters are " + str(stripfile()))
#3
sum = 0
name_file = "myFile.txt"

def splitfile(file):
    sum = 0
    read = open(file,'r').read().split()
    for i in read:
        sum = sum + 1
    return sum

print('Total word are ' + str(splitfile(name_file)))
#4
beg = int(input("Enter a beginning Celcius value: "))
end = int(input("Enter a ending Clelcius value: "))

name_file = "multiply.txt"
def multiply(beg,end):
 f = open(name_file,'w')
 for i in range(beg,end):
    f.write("{} Celcius = {:.2f} Farenheit. \n".format(i,(i * 1.8) + 32))
 f.close()

multiply(beg,end)