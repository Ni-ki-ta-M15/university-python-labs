import datetime

mother_birthday = datetime.datetime(1979, 1, 7) # birthday my mother
my_birthday = datetime.datetime(2005, 5, 15) #my birthday
dif = my_birthday - mother_birthday
dif = dif.days
year = 0
month = 0
day = 0
also_day = int(dif)
while also_day >= 365:
    if also_day >= 365:
        year += 1
        also_day -= 365

while also_day >= 31 and also_day < 365:
    if also_day >= 31 and also_day < 365:       # We're calculating the difference
        month += 1
        also_day -= 31
while also_day > 1 and also_day < 31:
    if also_day > 1 and also_day < 31:
        day += also_day
        also_day -= also_day


print('Variance in', year, 'years', 'and also', month, 'month', 'and', day, 'day') # print result

#print('I was born when my mom was', year, 'year', month, 'month and', day, 'day')
