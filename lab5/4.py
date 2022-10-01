beg = int(input("Enter a beginning Celcius value: "))
end = int(input("Enter a ending Clelcius value: "))

name_file = "multiply.txt"
def multiply(beg,end):
 f = open(name_file,'w')
 for i in range(beg,end):
    f.write("{} Celcius = {:.2f} Farenheit. \n".format(i,(i * 1.8) + 32))
 f.close()

multiply(beg,end)