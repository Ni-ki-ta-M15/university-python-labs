
import random as ran
print("Игра \"Угадай число\"")
x = 0

while x == 0:
    try:
        print("Введите С какого числа будете угадывать )")
        a = int(input("С числа: "))
        print("Введите ПО какое число будете угадывать )")
        b = int(input("По число: "))

        Random_num = ran.randint(a, b)
        User_num = input("Угадайте число: ")
        while x == 0:
            if int(User_num) == Random_num:
                print("Вы угадали")
                print(f"Я загадала {Random_num}", end="\n\n")
                print("Хотите сыграть еще раз?")
                Again = input("")
                if Again == "да":
                    print("Введите с какого по какое число будете угадывать )")
                    a = int(input("С числа: "))
                    b = int(input("По число: "))
                    Random_num = ran.randint(a, b)
                    User_num = input("Угадайте число: ")
                    if int(User_num) == Random_num:
                        print("Вы угадали")
                        print(f"Я загадала {Random_num}", end="\n\n")
                        print("Хотите сыграть еще раз?")
                        Again = input("")
                        if Again == "да":
                            print("Введите с какого по какое число будете угадывать )")
                            a = int(input("С числа: "))
                            b = int(input("По число: "))
                            Random_num = ran.randint(a, b)
                            User_num = input("Угадай число: ")
                            if int(User_num) == Random_num:
                                print("Вы угадали")
                                print(f"Я загадала {Random_num}")
                            else:
                                print("Вы НЕ угадали :-)")
                                print(f"Было загадано число:{Random_num}")
                        elif Again == "нет":
                            print("Спасибо что сыграли в мою игру №№№ )")
                            break

                    else:
                        print("Вы НЕ угадали :-)", end="\n")
                        print(f"Было загадано число:{Random_num}", end="\n\n")
                elif Again == "нет":
                    print("Спасибо что сыграли в мою игру )")
                    break
            else:
                print("Вы НЕ угадали :-)", end="\n\n")
                print(f"Было загадано число:{Random_num}", end="\n\n")
    except ValueError:
        print("Ошибка,\n перезапустите програму ")
