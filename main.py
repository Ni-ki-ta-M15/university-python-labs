"""import numexpr as num
from colorama import init
from colorama import Fore, Back
from numpy import matrix as mat
mat.round()

init()
x = 0
while x == 0:
    print(Fore.YELLOW)
    exam = input("Введите ваш пример: ")
    res = num.evaluate(exam)
    print(Fore.LIGHTBLUE_EX)
    print(f"Результат: {res}")"""

x = 0
while x == 0:
    print('Введите размер до 13...')
    size = int(input('Введите ширину: '))
    if int(size == 12):
        print('      B B B B B B B B B B B B')
        print('     B                     B')
        print('    B                     B')
        print('   B                     B')
        print('  B                     B')
        print(' B                     B')
        print('B B B B B B B B B B B B ')
    elif size == 11:
        print('      B B B B B B B B B B B ')
        print('     B                   B')
        print('    B                   B')
        print('   B                   B')
        print('  B                   B')
        print(' B                   B')
        print('B B B B B B B B B B B')
    elif size == 10:
        print('      B B B B B B B B B B  ')
        print('     B                 B')
        print('    B                 B')
        print('   B                 B')
        print('  B                 B')
        print(' B                 B')
        print('B B B B B B B B B B ')
    elif size == 9:
        print('     B B B B B B B B B   ')
        print('    B               B')
        print('   B               B')
        print('  B               B')
        print(' B               B')
        print('B B B B B B B B B  ')
    elif size == 8:
        print('     B B B B B B B B')
        print('    B             B')
        print('   B             B')
        print('  B             B')
        print(' B             B')
        print('B B B B B B B B')
    elif size == 7:
        print('     B B B B B B B ')
        print('    B           B')
        print('   B           B')
        print('  B           B')
        print(' B B B B B B B ')
    elif size == 6:
        print('     B B B B B B')
        print('    B         B')
        print('   B         B')
        print('  B         B')
        print(' B B B B B B ')
    elif size == 5:
        print('    B B B B B')
        print('   B       B')
        print('  B       B')
        print(' B B B B B ')
    elif size == 4:
        print('    B B B B ')
        print('   B     B')
        print('  B     B')
        print(' B B B B')
    elif size == 3:
        print('   B B B')
        print('  B   B')
        print(' B B B')
    elif size == 2 or size == 1:
        print('Операцию ввыполнить невозможно!', end="\n\n")
    elif size == 13:
        print('Я сказал ДО 13)', end="\n\n")
    else:
        print("Понятно... Бай" , end='\n\n')