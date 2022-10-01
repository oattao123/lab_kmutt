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
