def stripfile(): 
    while 1:
     
     file = open('myFile.txt', 'r')
     char = file.read().strip()         
     if not char:
       break
     return len(char)         
     file.close()

print("Total letters are " + str(stripfile()))