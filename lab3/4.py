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