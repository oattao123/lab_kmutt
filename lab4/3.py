def mult_table(num,mult = 1):
    print(f"{num} X {mult} = {num * mult}")
    if mult >= 12: return
    else:
        return mult_table(num,mult+1)
    return mult_table(num,mult) 
num = int(input("Enter a number:"))
print(f"Multiplication Table of {num} is:")
mult_table(num)