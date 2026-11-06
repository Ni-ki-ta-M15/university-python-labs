import math

# def square_rectangle():
#     a = float(input('Enter size a: '))
#     b = float(input('Enter size b: '))
#     square_p = a * b
#     print(f'Your square for rectangle: {square_p}')
#
# def square_trygol():
#     a = int(input('Enter size a: '))
#     b = int(input('Enter size b: '))
#     c = int(input('Enter size c: '))
#     summa = a + b + c
#     poly_perimetr = 0.5 * summa
#     square_tri = math.sqrt(poly_perimetr * (poly_perimetr - a) * (poly_perimetr - b) * (poly_perimetr - c))
#     print(f'Your square for triangle: {round(square_tri, 3)} m^2')
#
# def circle():
#     a = int(input('Enter radius a: '))
#     square_s = math.pi * (math.pow(a, 2))
#     print(f'Your square for circule: {square_s}')
# while True:
#     try:
#         birthday = ('15.05.2005')
#         print('243 group,', 'Малый Никита Михайлович!', birthday)
#         print('1-прямоугольник\n 2-треугольник\n 3-круг')
#         choize = int(input('Enter your number: '))
#         if choize == 1:
#             square_rectangle()
#             break
#         elif choize == 2:
#             square_trygol()
#             break
#         elif choize == 3:
#             circle()
#             break
#         else:
#             print('You write any NOT corect!')
#             break
#     except ValueError:
#         print('You write any not correct!')



# import math
#
# def rectangle_area():
#     a = float(input('Enter side a: '))
#     b = float(input('Enter side b: '))
#     return a * b
#
# def triangle_area():
#     a = float(input('Enter base a: '))
#     h = float(input('Enter height h: '))
#     return 0.5 * a * h
#
# def circle_area():
#     r = float(input('Enter radius r: '))
#     return math.pi * (r ** 2)
#
# while True:
#     try:
#         birthday = ('15.05.2005')
#         print('243 group,', 'Малый Никита Михайлович!', birthday)
#         print('1-прямоугольник\n 2-треугольник\n 3-круг')
#         choize = int(input('Enter your number: '))
#         if choize == 1:
#             print(f'Your square for rectangle:{rectangle_area()}')
#             break
#         elif choize == 2:
#             print(f'Your square for triangle:{triangle_area()}')
#             break
#         elif choize == 3:
#             print(f'Your square for circule: {circle_area()}')
#             break
#         else:
#             print('You write any NOT corect!')
#
#     except ValueError:
#         print('You write any not correct!')


def calculate_square(cathet_a, cathet_b):
    return 0.5 * cathet_a * cathet_b

def calculate_perimeter(diamond_side):
    return 4 * diamond_side

def calculate_amount(square, perimeter):
    return square + perimeter

try:
    birthday = '15.05.2005'
    full_name = 'Малый Никита Михайлович'
    cathet_a = float(input('Enter cathet A: '))
    cathet_b = float(input('Enter cathet B: '))
    square = calculate_square(cathet_a, cathet_b) # Вызов фунцыи
    print(f'Your square: {square}')

    diamond_side = float(input('Enter side of diamond: '))
    perimeter = calculate_perimeter(diamond_side)
    print(f'Your diamond perimeter: {perimeter}')

    amount = calculate_amount(square, perimeter)
    print(f'Answer for task: {square} + {perimeter} = {amount}')
except ValueError:
    print('You REAL stupid!!! ')
except TypeError:
    print('Please enter right data')