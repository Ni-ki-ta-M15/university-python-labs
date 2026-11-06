# import math
# AB = int(input('Длина 1 катета:'))
# AC = float(input('Длина 2 катета:'))
# BC = math.sqrt(AB**2 + AC**2)
# triangle_area = (AB * AC) / 2
# perimeter_triangle = AB + AC + BC
# print(f'Площадь треугольника {triangle_area}')
# print(f'Периметр треугольника{perimeter_triangle}')


#3

# birthday = ('15.05.2005')
# print('243 group,', 'Малый Никита Михайлович!', birthday)
#
# name = input('What is your name: ')
# city = input('Where are you from: ')
# hobby = input('What is your hobby: ')
# print('')
#
# print(f'This is {name}')
# print(f'It is {city}')
# print(f'Her/his hobby is {hobby}')

#4


# import time
# birthday = ('15.05.2005')
# print('243 group,', 'Малый Никита Михайлович!', birthday)
#
# birth_day = int(input('Your birth DAY: '))
# birth_month = int(input('Your birth MONTH: '))
# birth_year = int(input('Your birth DAY: '))
#
# print(f'Реши пример: ({birth_day} + {birth_month}) * {birth_year}')
# time.sleep(5)
# print(f'{(birth_day + birth_month) * birth_year}')

# 5

# birthday = ('15.05.2005')
# print('243 group,', 'Малый Никита Михайлович!', birthday)
#
# my_day = input('Your birthDAY: ')
# my_year = input('Your birthYEAR: ')
#
# mother_day = int(input('Mother birthDAY: '))
# mother_year = int(input('Mother birthYEAR: '))
#
# addition_my = int(my_day) + int(my_year)
# print(f'Addition my number: {addition_my}')
# deduction_mother = mother_year - mother_day
# print(f'Deduction mother number: {deduction_mother}')
#
# division_our = addition_my / deduction_mother
# print(f'Division our number: {round(division_our, 3)}')

# individyal tasks

canthet_a = float(input('Enter cathet A: '))
canthet_b = float(input('Enter cathet B: '))

square = 1/2*(canthet_a * canthet_b)
print(f'Your square: {square}')

diamond_side = float(input('Enter side of diamond: '))
perimeter = 4 * diamond_side
print(f'Your diamond perimeter: {perimeter}')

amount = square + perimeter
print(f'Answer for task: {square} + {perimeter} = {amount}')
