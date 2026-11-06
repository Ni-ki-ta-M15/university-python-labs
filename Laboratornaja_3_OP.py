# Maly_Nikita_Mikhailovich_BDAY = 15052005
# Malaya_Yanina_Nikolayevna_MOM_BDAY = 1071979
#
# if Maly_Nikita_Mikhailovich_BDAY > 16052005 and Malaya_Yanina_Nikolayevna_MOM_BDAY == 1071979:
#     print(True)
# else:
#     print(False)
# if Malaya_Yanina_Nikolayevna_MOM_BDAY == 1071979 and Maly_Nikita_Mikhailovich_BDAY > 14052005:
#     print(True)
# else:
#     print(False)
#
# # Example 2 (c)
# if Maly_Nikita_Mikhailovich_BDAY > 16052005 or Malaya_Yanina_Nikolayevna_MOM_BDAY == 1071978:
#     print(True)
# else:
#     print(False)
# if Malaya_Yanina_Nikolayevna_MOM_BDAY == 1071978 or Maly_Nikita_Mikhailovich_BDAY < 16052005:
#     print(True)
# else:
#     print(False)

# birthday = ('15.05.2005')
# print('243 group,', 'Малый Никита Михайлович!', birthday)
# maly_nikita_mikhailovich_BDAY = int(input('Enter my BDAY'))
# malaya_yanina_nikolayevna_MOM_BDAY = int(input('Enter mom BDAY'))
# if maly_nikita_mikhailovich_BDAY > malaya_yanina_nikolayevna_MOM_BDAY:
#     print(True,': 1 more then 2')
# else:
#     print(False,': 1 loss then 2')

# birthday = '15.05.2005'
# full_name = 'Малый Никита Михайлович'
# print(f'243 group, {full_name}!  {birthday}')
# check = input('Enter your date: ')
# try:
#     val = int(check)
#     print(f'Date of birth check: {check} of {full_name}')
# except ValueError:
#     print("Это не число")



# day_of_birthday = int(input('Enter your day of BD: '))
# if day_of_birthday >= 1 and day_of_birthday <= 10:
#     print('1')
# elif day_of_birthday >= 10 and day_of_birthday < 21:
#     print('2')
# elif day_of_birthday >= 21 and day_of_birthday < 31:
#     print('3')
# elif day_of_birthday == 31:
#     print('4')
# elif day_of_birthday <= 0:
#     print('You are stupid! ')

# individyal tasks №2 on C

try:
    birthday = '15.05.2005'
    full_name = 'Малый Никита Михайлович'
    canthet_a = float(input('Enter cathet A: '))
    canthet_b = float(input('Enter cathet B: '))

    square = 1/2*(canthet_a * canthet_b)
    print(f'Your square: {square}')

    diamond_side = float(input('Enter side of diamond: '))
    perimeter = 4 * diamond_side
    print(f'Your diamond perimeter: {perimeter}')

    amount = square + perimeter
    print(f'Answer for task: {square} + {perimeter} = {amount}')
except ValueError:
    print('You REAL stupid!!! ')
except TypeError:
    print('Please enter right data')