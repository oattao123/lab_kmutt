number =  int(input("Enter number "))
total = 0
for value in range(1,number + 1):
 total = total + value
print("Summation of numbers from 1 to {0} is {1}".format(value,total))