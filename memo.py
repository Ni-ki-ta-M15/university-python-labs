#def hello(name):
    #str(print("Hello ", name))
#try:
    #name = str(input("enter your name: "))
    #print("Hello ", name)

#except : TypeError
#print("Please  enter your NAME")

#def proverka (a, b, c ):
   # if a != 2 and b != 2 or c == 10:
     #return a * b * c
   # else:
        #return "Some not correct"


#import random as ran
#x = 0
#try:
#        print("Введите С какого числа будете угадывать )")
#        a = int(input("С числа: "))
#        print("Введите ПО какое число будете угадывать )")
#        b = int(input("По число: "))
#        while x == 0:
#            Random_num = ran.randint(a, b)
#            User_num = input("Угадайте число: ")
#            while x == 0:
#                if int(User_num) == Random_num:
#                    print("Вы угадали")
#                   print(f"Я загадала {Random_num}", end="\n\n")
 #                   print("Хотите сыграть еще раз?")
#                    Again = input("")
#                    if Again == "да":
#                        print("Введите с какого по какое число будете угадывать )")
#                        a = int(input("С числа: "))
#                        b = int(input("По число: "))
#                        Random_num = ran.randint(a, b)
#                        User_num = input("Угадайте число: ")
#                        if int(User_num) == Random_num:
#                            print("Вы угадали")
#                            print(f"Я загадала {Random_num}", end="\n\n")
#                            print("Хотите сыграть еще раз?")
#                            Again = input("")
#                            if Again == "да":
#                                print("Введите с какого по какое число будете угадывать )")
#                                a = int(input("С числа: "))
 #                               b = int(input("По число: "))
#                                Random_num = ran.randint(a, b)
#                                User_num = input("Угадай число: ")
#                                if int(User_num) == Random_num:
#                                    print("Вы угадали")
#                                    print(f"Я загадала {Random_num}")
#                                else:
#                                    print("Вы НЕ угадали :-)")
#                                    print(f"Было загадано число:{Random_num}")
#                            elif Again == "нет":
#                                print("Спасибо что сыграли в мою игру №№№ )")
#                                break
#
#                        else:
#                            print("Вы НЕ угадали :-)", end="\n")
#                            print(f"Было загадано число:{Random_num}", end="\n\n")
#                    elif Again == "нет":
#                        print("Спасибо что сыграли в мою игру )")
 #                       break
#                else:
#                    print("Вы НЕ угадали :-)", end="\n\n")
#                    print(f"Было загадано число:{Random_num}", end="\n\n")
#except ValueError:
#    print("Ошибка,\n перезапустите програму ")

import time
import webbrowser

print('Что тебе нужно ?')
print('Youtube - 1 , Radio - 2 , Film - 3', end="\n\n")
N = int(input('Your number: '))
Youtube = 1
Radio = 2
Film = 3
if N == 1:
    print('Тебе веселый контент нужен? - 1')
    print('Или познавательный - 2')
    x = 0
    while x == 0:
        try:
            content = int(input('Твой выбор: '))
            if content == 1:
                print('Открываю ютуб, развлекательное ...')
                time.sleep(2)
                webbrowser.open('https://www.youtube.com/watch?v=w9WjR2phxBo')
                break
            elif content == 2:
                print('Открываю ютуб, познавательное...')
                time.sleep(2)
                webbrowser.open('https://www.youtube.com/watch?v=P0czP5MEbYQ')
                break
            else:
                print('Введи цифру 1 или 2)')

        except ValueError:
            print('Ты ошибся... Попробуй еще раз )')
elif N == 2:
    print('Ты слушаешь радио США - 1, Украины - 2 или Польши - 3 ?')
    x = 0
    while x == 0:
        try:
            coutry_radio = int(input('Твой выбор: '))
            if coutry_radio == 1:
                print('Открываю радио США: ')
                time.sleep(1)
                webbrowser.open('https://www.fmradiofree.com/americas-country')
                break
            elif coutry_radio == 2:
                print('Открываю радио Украины: ')
                time.sleep(1)
                webbrowser.open('http://www.radio-online.com.ua/?listen=lux_fm_ua')
                break
            elif coutry_radio == 3:
                print('Открываю радио Польши: ')
                time.sleep(1)
                webbrowser.open('https://player.polskieradio.pl/anteny/polsza')
                break
        except ValueError:
            print('Возможно ты ошибся, попробуй еще раз... ')
elif N == 3:
    print('Ты хочешь чтобы я что-то посоветовал?')
    print('Да или Нет')
    x = 0
    while x == 0:
        try:
            vibor = int(input('Твой выбор: '))
            if vibor == 1:
                print('Я могу посоветовать фильм: ')
                time.sleep(0.5)
                webbrowser.open('https://www.netflix.com/watch/80192646?trackId=14183190&tctx=1%2C9%2C6ac7a7f0-7715-43bb-b672-9a7bfef1c999-46140348%2CNES_7389BEFA2E8F1BEFF6C244C33937C3-7DBCDC9D5CA1B3-9B2D67AE55_p_1674035741083%2CNES_7389BEFA2E8F1BEFF6C244C33937C3_p_1674035741083%2C%2C%2C%2C80192646%2CVideo%3A80192646')
                break
            elif vibor == 2:
                print('Открываю Netflix: ')
                webbrowser.open('https://www.netflix.com/')
                break
            else:
                print('Введите верное число: ')
                break
        except ValueError:
            print('Забыл сказать: Да - 1, Нет - 2 ')
elif N != 1 or N != 2 or N != 3:

    print('Возможно, вы ошиблись с цифрой ')