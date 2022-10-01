#1
def Hi(name,last):
    def namess():
        print(f"Hi, " + name + " "+ last + "!")
    namess()

name_in = input("What is you name?: ")
last_in = input("What is you last name?: ")
Hi(name_in,last_in)
#2
def fahrenheit(celsius_beg,celsius_end):
    if celsius_beg > celsius_end: return
    else:return print("{} Celcius = {:.2f} Farenheit.".format(celsius_beg,(celsius_beg * 1.8) + 32.)) ,fahrenheit(celsius_beg+1,celsius_end)


celsius_beg = int(input("Enter a beginning Celcius value: "))
celsius_end = int(input("Enter a ending Celcius value: "))
fahrenheit(celsius_beg,celsius_end)
#3
def mult_table(num,mult = 1):
    print(f"{num} X {mult} = {num * mult}")
    if mult >= 12: return
    else:
        return mult_table(num,mult+1)
    return mult_table(num,mult) 
num = int(input("Enter a number:"))
print(f"Multiplication Table of {num} is:")
mult_table(num)
#4
def money(name,age):
 list_name = ["Tony", "Peter", "Mark", "Kim", "James", "Kenny"]
 names = name.capitalize()
 char = "Tick price for "
 if names in list_name and age < 15:
    print(char  + names + " " + "3.75")
 elif names in list_name and age > 15:
    print (char + names + " " + "7.5")
 elif not names in list_name and age < 15:
    print (char + names +" " + "7.5")
 elif not names in list_name and age > 15:
    print (char + names + " " + "15")


name = str(input("Plese enter your name: "))
age = int(input("Enter your age: "))
money(name,age)