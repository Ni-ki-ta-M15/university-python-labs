# import math, prettytable, time
#
# while True:
#     try:
#         print('Okay, we have right triangular pyramid with:')
#         base_side_C = float(input('Your base side equal: '))
#         side_angle_B = float(input('Your side angle equal: ')) # Ask the user to enter the data
#
#         squaring_C = math.pow(base_side_C, 2) # Squaring the number c
#         B_radian = math.radians(side_angle_B) #Convert to radians
#         tg_B = round(math.tan(B_radian), 3) #Find the tangent
#
#         first_part = 0.433012 * squaring_C
#         second_part = ((3 * base_side_C) / 2) * (base_side_C / 2) #Insert the data into the formula and everything is counted
#         total_surface_area = round(first_part + second_part * tg_B, 3)
#
#         print('Please wait, I\'m thinking...')
#         time.sleep(2)
#         table = prettytable.PrettyTable() #Create table with help method PrettyTable
#
#         table.field_names = ["Base side (c)", "Side angle (γ, degrees)", "Total surface area"] #Create columns with names
#         table.add_row([base_side_C, tg_B, total_surface_area]) #Create columns with data
#         print(table)
#
#         break
#     except ValueError: #Check if the user has entered any letters
#         print('You writen not number', '\n')
# name = 'Maliy Nikita'
# print(f'#56, group - 243, #14- for list, {name}')

import math, time


def MNM(cols, line_sum):
    print(cols * '+')
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
        MNM(85, '+')
        header_row = print(
            ("Base side (c)".center(column_width)) + (" Side angle (γ, degrees) ".center(column_width)) + ("Total surface area".center(column_width)))
        MNM(85, '+')
        data_row = print((str(base_side_C).center(column_width) + (str(tg_B).center(column_width)) + (str(total_surface_area).center(column_width))))
        MNM(85, '+')
        break
    except ValueError: #Check if the user has entered any letters
        print('You writen not number', '\n')