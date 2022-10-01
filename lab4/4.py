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