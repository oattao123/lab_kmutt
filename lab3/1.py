name_list = ["jeff","jack","jim"]
name_in = input("What is you name?:")
def hello(name):
    if name.lower() in name_list:
        print("Hello, " + name.capitalize() + ". Good morning my friend")
    else:
        print("Who are you?")
        print("Nice to meet you anyway ..." + name.lower().capitalize() + " :).")

hello(name_in)