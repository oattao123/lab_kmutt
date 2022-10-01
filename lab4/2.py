def fahrenheit(celsius_beg,celsius_end):
    if celsius_beg > celsius_end: return
    else:return print("{} Celcius = {:.2f} Farenheit.".format(celsius_beg,(celsius_beg * 1.8) + 32.)) ,fahrenheit(celsius_beg+1,celsius_end)


celsius_beg = int(input("Enter a beginning Celcius value: "))
celsius_end = int(input("Enter a ending Celcius value: "))
fahrenheit(celsius_beg,celsius_end)