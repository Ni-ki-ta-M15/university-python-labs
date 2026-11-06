# # import math
# #
# # while True:
# #     try:
# #         birthday = ('15.05.2005')
# #         print('243 group,', 'Малый Никита Михайлович!', birthday)
# #         print('1-прямоугольник\n 2-треугольник\n 3-круг')
# #         choize = int(input('Enter your number: '))
# #         if choize == 1:
# #             a = int(input('Enter size a: '))
# #             b = int(input('Enter size b: '))
# #             square_p = a * b
# #             print(f'Your square for rectangle: {square_p}')
# #             break
# #         elif choize == 2:
# #             a = int(input('Enter size a: '))
# #             b = int(input('Enter size b: '))
# #             c = int(input('Enter size c: '))
# #             summa = a + b + c
# #             poly_perimetr = 0.5 * summa
# #             square_tri = math.sqrt(poly_perimetr * (poly_perimetr - a) * (poly_perimetr - b) * (poly_perimetr - c))
# #             print(f'Your square for triangle: {round(square_tri, 3)} m^2')
# #             break
# #         elif choize == 3:
# #             a = int(input('Enter radius a: '))
# #             square_s = math.pi * (math.pow(a, 2))
# #             print(f'Your square for circule: {square_s}')
# #             break
# #         else:
# #             print('You write any NOT corect!')
# #             break
# #     except ValueError:
# #         print('You write any not correct!')
#
#
# # Example 1
# birthday = ('15.05.2005')
# print('243 group,', 'Малый Никита Михайлович!', birthday)
# letter = input('Enter big first letter of language what you know: ')
# if letter == 'J':
#     print('You know best language Java!')
# elif letter == 'P':
#     print('You know best language Python!')
# elif letter == 'C':
#     print('You know best language C!')
# elif letter == '#':
#     print('You know best language C# or C++!')
# elif letter == 'S':
#     print('You know best language SQL!, Ohhh, nooo')
# else:
#     print('Learn while it’s not too late')

# from prettytable import PrettyTable
#
# x = PrettyTable()
#
# x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
#
# x.add_row([
#         ["Adelaide", 1295, 1158259, 600.5],
#         ["Brisbane", 5905, 1857594, 1146.4],
#         ["Darwin", 112, 120900, 1714.7],
#         ["Hobart", 1357, 205556, 619.5],
#         ["Sydney", 2058, 4336374, 1214.8],
#         ["Melbourne", 1566, 3806092, 646.9],
#         ["Perth", 5386, 1554769, 869.4]])
#
# print(x)


import math, time

cols = 3
line_symbol = "+"
column_width = 27

while True:
    try:
        print('Okay, we have right triangular pyramid with:')
        base_side_C = float(input('Your base side equal: '))
        side_angle_B = float(input('Your side angle equal: ')) # Ask the user to enter the data

        squaring_C = math.pow(base_side_C, 2) # Squaring the number c
        B_radian = math.radians(side_angle_B) #Convert to radians
        tg_B = round(math.tan(B_radian), 3) #Find the tangent

        first_part = 0.433012 * squaring_C
        second_part = ((3 * base_side_C) / 2) * (base_side_C / 2) #Insert the data into the formula and everything is counted
        total_surface_area = round(first_part + second_part * tg_B, 3)

        print('Please wait, I\'m thinking...')
        time.sleep(2)
        data_row = line_symbol + (str(base_side_C).center(column_width) + line_symbol) + (str(tg_B).center(column_width) + line_symbol) + (str(total_surface_area).center(column_width) + line_symbol)
        header_row = line_symbol + ("Base side (c)".center(column_width) + line_symbol) + (" Side angle (γ, degrees) ".center(column_width) + line_symbol) + ("Total surface area".center(column_width) + line_symbol)
        border = line_symbol * (len(data_row) - 0)
        print(border)
        print(header_row)
        print(border)
        print(data_row)
        print(border)

        break
    except ValueError: #Check if the user has entered any letters
        print('You writen not number', '\n')