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