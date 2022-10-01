import math

x = 3
x_1 = math.sqrt(x)
x_float = "{:.3f}".format(x_1)

y = 8
y_1 = y ** (1./3.)
y_float = "{:.3f}".format(y_1)
print("The square root of 3.00 is " + x_float)
print("The square root of 8.00 is " + str(y_float))