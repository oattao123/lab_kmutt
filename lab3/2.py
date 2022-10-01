week = int(input("How many hours did you work last week?"))
hour = int(input("What is your pay rate per hor(between 10-25)"))

def rate(week,hour):
    if week <= 40 :
        pay = week*hour
    elif week > 40:
        pay = 40 * hour
        pay += (week - 40) * 1.5 * hour
    return pay

print(rate(week,hour))
