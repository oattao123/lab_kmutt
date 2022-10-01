#1
name_list = ["jeff","jack","jim"]
name_in = input("What is you name?:")
def hello(name):
    if name.lower() in name_list:
        print("Hello, " + name.capitalize() + ". Good morning my friend")
    else:
        print("Who are you?")
        print("Nice to meet you anyway ..." + name.lower().capitalize() + " :).")

hello(name_in)

#2
week = int(input("How many hours did you work last week?"))
hour = int(input("What is your pay rate per hor(between 10-25)"))

def rate(week,hour):
    if week <= 40 :
        pay = week*hour
    elif week > 40:
        pay = 40 * hour
        pay += (week - 40) * 1.5 * hour
    return pay

print(rate(week,hour))

#3
num = int(input("Enter a number tp test:"))
flag = False 
def is_prime(num):
  if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
if flag:
    print("This is not a prime number")
else:
    print("This is a prime number")

is_prime(num)

#4
list = []

num = int(input("Enter number of elements :"))
def cta(num):
    for i in range  (0, num):
        ele = int(input())
        list.append(ele)
cta(num)
print("The entered" + str(list))
print("The maxium number emtered is " + str(max(list)))
print("The minimum number emtered is " + str(min(list)))

#5
import math
print("Please enter a choice for your selection")
print("Enter 1 if you want to calculate the area of a tringle.")
print("Enter 2 if you want to calculate the volumn of a cubluc.")
print("Enter 3 if you want to calculate the volumn of a cone.")

choice = int(input("Enter you choce here:"))
def triangle():
    length = float(input("Enter enter base length:"))
    height = float(input("Enter enter the height:"))
    print(f"The are of the triangle with base = {length} and height = {height} is {0.5 * length * height}")
def cubic():
    width = int(input("Enter enter base width:"))
    length = int(input("Enter enter the length: "))
    height = int(input("Enter enter the height:"))
    print(f"The cubic volumn of width = {width} length = {length} and height = {height} is  {width * height * length}")
def conic():
    diameter = int(input("Enter enter the diameter :"))
    height = int(input("Enter enter the height:"))
    print(f"The connical volumn of diameter = {diameter} and height = {height} is {(22/7) * ((diameter / 2) ** 2) * (height / 3)}")


match choice:
    case 1:
        triangle()
    case 2:
        cubic()
    case 3:
        conic()
    case _:
        print("Invalid Choice")
