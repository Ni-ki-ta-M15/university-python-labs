from colorama import init
from colorama import Fore, Style, Back

init()
file = open('../../txt/matrix.txt', 'w')
print(Fore.LIGHTYELLOW_EX)
masiv1 = [2, 5, -2]
masiv2 = [3, -7, 8]
masiv3 = [-1, 3, 10]
# print( *masiv, '\n' ,*masiv1,'\n',*masiv2)
file.write('First mutrix: \n ')
file.write(' [2, 5, -2] \n')
file.write('  [3, -7, 8] \n')
file.write('  [-1, 3, 10] \n\n\n')
print(masiv1)
print(masiv2)
print(masiv3)
print()
print()

##Поиск максимального значения в матрице.

maxim_1 = max(masiv1)
maxim_2 = max(masiv2)
maxim_3 = max(masiv3)

if maxim_1 > maxim_2:
    max_number = maxim_1
elif maxim_2 > maxim_3:
    max_number = maxim_2
elif maxim_3 > maxim_2:
    max_number = maxim_3
elif maxim_3 > maxim_1:
    max_number = maxim_3
print(Back.LIGHTYELLOW_EX, Fore.BLACK)
print('Максимальное число в матрице: ', max_number)
file.write('max_number: 10 \n\n')
print(Style.RESET_ALL)

minim_1 = min(masiv1)
minim_2 = min(masiv2)
minim_3 = min(masiv3)

if minim_1 < minim_2:
    min_number = minim_1
elif minim_2 < minim_3:
    min_number = minim_2
elif minim_3 < minim_2:
    min_number = minim_3
elif minim_3 < minim_1:
    min_number = minim_3
print(Back.LIGHTBLUE_EX, Fore.BLACK)
print('Минимальное число в матрице: ', min_number)

print(Style.RESET_ALL)
masiv2[1] = masiv3[2]
masiv3[2] = min_number
print(Fore.LIGHTCYAN_EX)
file.write('Second mutrix: \n ')
file.write('[2, 5, -2] \n')
file.write(' [3, 10, 8] \n')
file.write(' [-1, 3,-7] \n')
print(masiv1)
print(masiv2)
print(masiv3)

file.close()

Glav = masiv1[2] + masiv2[1] + masiv3[0]
print(Fore.LIGHTMAGENTA_EX, 'Сумма елементов главной диагонали = ', Glav)
Pob = masiv1[0] - masiv2[1] - masiv3[2]
print(Fore.MAGENTA, 'Разница елементов побочной  диагонали = ', Pob)
