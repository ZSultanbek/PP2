import datetime

#1___________________________
print("#1____________________")
def SubstractDate(date, dayssub = 5):
    d = date.today() - datetime.timedelta(days = dayssub)
    return d

current = datetime.datetime.today()

current = SubstractDate(current)
print(current)



#2___________________________
print("#2____________________")
def yesterday():
    day = datetime.datetime.today()
    day = day.today() - datetime.timedelta(days = 1)
    print(day)
def tommorow():
    day = datetime.datetime.today()
    day = day.today() + datetime.timedelta(days = 1)
    print(day)
def today():
    day = datetime.datetime.today()
    print(day)


yesterday()
today()
tommorow()

#3___________________________
print("#3____________________")
x = datetime.datetime.now()
print(x.microsecond)


#4___________________________
print("#4____________________")

date1 = datetime.datetime(2024, 2, 15, 12, 0, 0)
date2 = datetime.datetime(2024, 2, 20, 14, 30, 15)

time_difference = date2 - date1

difference_in_seconds = time_difference.total_seconds()
print(difference_in_seconds)