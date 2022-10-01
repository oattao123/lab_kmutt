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