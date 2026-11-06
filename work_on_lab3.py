import math

while True:
    birthday = ('15.05.2005')
    print('243 group,', 'Малый Никита Михайлович!', birthday)
    print('1-прямоугольник\n 2-треугольник\n 3-круг')
    choize = int(input('Enter your number: '))
    if choize == 1:
        a = int(input('Enter size a: '))
        b = int(input('Enter size b: '))
        square_p = a * b
        print(f'Your square for rectangle: {square_p}')
        break
    if choize == 2:
        a = int(input('Enter size a: '))
        b = int(input('Enter size b: '))
        c = int(input('Enter size c: '))
        summa = a + b + c
        poly_perimetr = 0.5 * summa
        square_tri = math.sqrt(poly_perimetr * (poly_perimetr - a) * (poly_perimetr - b) * (poly_perimetr - c))
        print(f'Your square for triangle: {round(square_tri, 3)} m^2')
        break
    if choize == 3:
        a = int(input('Enter radius a: '))
        square_s = math.pi * (math.pow(a, 2))
        print(f'Your square for circule: {square_s}')
        break
    if choize != 4:
        print('You write any NOT corect!')
        break

# a = int(input('Enter number a: '))
# b = int(input('Enter number b: '))
# c = int(input('Enter number c: '))
#
# per_a = math.pow(a, 3)
#
# numerator = per_a * (c - b)
# denominator = 7
# fraction = numerator / denominator
# formatted_number = format(fraction, '>15')
# print(formatted_number)


# a = int(input('Enter number a: '))
# b = int(input('Enter number b: '))
# c = int(input('Enter number c: '))
#
# per_a = math.pow(a, 3)
#
# numerator = per_a * (c - b)
# denominator = 7
# fraction = str(numerator / denominator)
# left_aligned_number = fraction.ljust(15)  # Выравнивание строки по левому краю
# print(f"'{left_aligned_number}'")