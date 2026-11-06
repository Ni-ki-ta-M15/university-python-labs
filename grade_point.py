from colorama import init
from colorama import Fore, Style
init()
while True:
    quantity_Laborat = int(input('Будь ласка, напишіть кількість лабораторних: '))
    out_user = 0
    list_ball = []
    while out_user < quantity_Laborat :
        Lab = "Лабораторна робота №"+ str( out_user + 1 )+" : "
        list_ball.append(input(Lab))
        out_user += 1
        a = 0
    print(Fore.CYAN)
    while a < quantity_Laborat:
        print(list_ball[a])
        a += 1
        if a == quantity_Laborat:
            print('Перевірте)')
    print(Style.RESET_ALL)
    if quantity_Laborat == 5:
        print(Style.BRIGHT)
        a = int(list_ball[0])
        b = int(list_ball[1])
        c = int(list_ball[2])
        d = int(list_ball[3])
        e = int(list_ball[4])
        sr = (a + b + c + d + e) / quantity_Laborat
        print(f'Середній бал з 5 лабораторних: {sr}')
    if quantity_Laborat == 6:
        print(Style.BRIGHT)
        a = int(list_ball[0])
        b = int(list_ball[1])
        c = int(list_ball[2])
        d = int(list_ball[3])
        e = int(list_ball[4])
        f = int(list_ball[5])
        sr = (a + b + c + d + e + f) / quantity_Laborat
        print(f'Середній бал з 6 практичних: {sr}')
    print(Style.RESET_ALL)

