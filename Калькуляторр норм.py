import numexpr as num
from colorama import init
from colorama import Fore, Back

init()
x = 0
while x == 0:
    print(Fore.CYAN)
    exam = input("Enter: ")
    res = num.evaluate(exam)
    print(Back.BLACK, Fore.MAGENTA, res)
    if exam == 'No':
        break