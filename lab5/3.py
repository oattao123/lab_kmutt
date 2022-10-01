sum = 0
name_file = "myFile.txt"

def splitfile(file):
    sum = 0
    read = open(file,'r').read().split()
    for i in read:
        sum = sum + 1
    return sum

print('Total word are ' + str(splitfile(name_file)))
