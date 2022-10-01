#1
celsius = float(input("Please enter the temperature in Celsius: "));fahrenheit = (celsius * 1.8) + 32 ;celsiuss = str(celsius);fahrenheits = str(fahrenheit);print(f"The {celsiuss} Celcius = {fahrenheits} Farenhite");
#2
number =  int(input("Enter number "))
total = 0
for value in range(1,number + 1):
 total = total + value
print("Summation of numbers from 1 to {0} is {1}".format(value,total))
#3
mult = int(input("Enter a number to to make a multilication table:"))
for i in range(1,13):
    print(str(mult)+" x "+str(i)+" = "+str(mult*i))
#4
score = int(input("Please enter your score:"))
if score>=80 and score<=100:
    print("You got A")
elif score>=75 and score<79:
    print("You got B+")
elif score>=70 and score<74:
    print("You got B")
elif score>=65 and score<69:
    print("You got C+")
elif score>=60 and score<64:
    print("You got C")
elif score>=55 and score<59:
    print("You got D+")
elif score>=50 and score<54:
    print("You got D")
elif score <= 50:
    print("You got F")
else:
    print("Invalid Input!")
#5
star = int(input("Please enter a staring number:"))
end = int(input("Please enter an ending number:"))

for x in range(star,end):
 for y in range(2,x):
  if x%y==0:break
 else:
  print (x,sep=' ')