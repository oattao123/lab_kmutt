def Hi(name,last):
    def namess():
        print(f"Hi, " + name + " "+ last + "!")
    namess()

name_in = input("What is you name?: ")
last_in = input("What is you last name?: ")
Hi(name_in,last_in)