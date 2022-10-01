star = int(input("Please enter a staring number:"))
end = int(input("Please enter an ending number:"))

for x in range(star,end):
 for y in range(2,x):
  if x%y==0:break
 else:
  print (x,sep=' ')