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