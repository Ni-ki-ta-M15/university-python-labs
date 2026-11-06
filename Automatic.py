import datetime as dt
while True:
    todays_date = dt.date.today()
    dayNumber = todays_date.isoweekday()
    x = dt.datetime.now()
    num_week = x.strftime("%W")
    odd_even_week = int(num_week) % 2
    if odd_even_week == 1:
        print('1 week')
        if dayNumber == 1:
            print('Today is Monday')
            break
        if dayNumber == 2:
            print('Today is Tuesday')
            break
        if dayNumber == 3:
            print('Today is Wednesday')
            break
        if dayNumber == 4:
            print('Today is Thursday')
            break
        if dayNumber == 5:
            print('Today is Friday')
            break
        if dayNumber == 6:
            print('Today is Saturday')
            break
        if dayNumber == 7:
            print('Today is Sunday')
            break