# import pyautogui as py
# name = 'Nikita '
# def hello():
#     print("Hello ", name)
#
# def proverka (a, b, c ):
#     if a != 2 and b != 2 or c != 2:
#      return a * b * c
#     else:
#         print("some not correct")
#         py.alert("Для вывода информации ", "title", button="Okay ")
#         year = py.prompt("Сколько вам лет?", "Ваш возраст")
#         print("Вам", year, "лет сейчас.")
#         py.confirm("What your sex?", "Yea?", ("Man", "Woman"))
#         py.password("Enter your password", "pasword title")
#
# # import random as ran
# #
# # import time
# #
# # print('        Game \n\'Guess the number\'')
# #
# #
# # try:
# #     while True:
# #         print("Введите С какого числа будете угадывать )")
# #         a = int(input("С числа: "))
# #         print("Введите ПО какое число будете угадывать )")
# #         b = int(input("По число: "))
# #
# #         Random_num = ran.randint(a, b)
# #         User_num = int(input('Put yoyr number: '))
# #         if Random_num == User_num:
# #             print('You have guessed')
# #             print(f'Я загадала {Random_num}')
# #             Play_again = input('Do you want play again?')
# #             if Play_again == 'yes' or Play_again == 'да' or Play_again == 'lf':
# #                 while True:
# #                     print("Введите С какого числа будете угадывать )")
# #                     a = int(input("С числа: "))
# #                     print("Введите ПО какое число будете угадывать )")
# #                     b = int(input("По число: "))
# #
# #                     Random_num = ran.randint(a, b)
# #                     User_num = int(input('Put yoyr number: '))
# #                     if Random_num == User_num:
# #                         print('You have guessed')
# #                         print(f'Я загадала {Random_num}')
# #                         Play_again = input('Do you want play again?')              #I don't think
# #                         if Play_again == 'yes' or Play_again == 'да' or Play_again == 'lf':
# #                             while True:
# #                                 print("Введите С какого числа будете угадывать )")
# #                                 a = int(input("С числа: "))
# #                                 print("Введите ПО какое число будете угадывать )")
# #                                 b = int(input("По число: "))
# #
# #                                 Random_num = ran.randint(a, b)
# #                                 User_num = int(input('Put yoyr number: '))
# #                                 if Random_num == User_num:
# #                                     print('You have guessed')
# #                                     print(f'Я загадала {Random_num}')
# #                                 elif Random_num != User_num:
# #                                     print('You haven`t guessed')
# #                                     print(f'I riddled {Random_num}')
# #                         elif Play_again == 'no' or Play_again == 'нет':
# #                             break                                                # it's needed, but I'll leave it at that.
# #                     elif Random_num != User_num:
# #                         print('You haven`t guessed')
# #                         print(f'I riddled {Random_num}')
# #             elif Play_again == 'no' or Play_again == 'нет':
# #                 break
# #         elif Random_num != User_num:
# #             print('You haven`t guessed')
# #             print(f'I riddled {Random_num}')
# #             Play_again = input('Do you want play again?')
# #             if Play_again == 'yes' or Play_again == 'да':
# #                 while True:
# #                     print("Введите С какого числа будете угадывать )")
# #                     a = int(input("С числа: "))
# #                     print("Введите ПО какое число будете угадывать )")
# #                     b = int(input("По число: "))
# #
# #                     Random_num = ran.randint(a, b)
# #                     User_num = int(input('Put yoyr number: '))
# #                     if Random_num == User_num:
# #                         print('You have guessed')
# #                         print(f'I riddled {Random_num}')
# #                     elif Random_num != User_num:
# #                         print('You haven`t guessed')
# #                         print(f'I riddled {Random_num}')
# #             elif Play_again == 'no' or Play_again == 'нет':
# #                 break
# # except ValueError:
# #     print('There is a mistake')
# #     time.sleep(0.5)
# #     print('Please reapite a program')
# # import pyautogui
# # print(pyautogui.position())


# import numpy as np
# import matplotlib.pyplot as plt
#
# # Задаємо початкові параметри
# n = 4096
# kzkk = 64
# kvzz = 32
# B = 9600 * 4
# D = 600 * 29103
# Vc = 2 * 10 ** 8
# Ppom = 343 * 10 ** -4
# tp = D / Vc
# delta_tp = 100 * 10 ** -3
# tq = 200 * 10 ** -3
# tac = 100 * 10 ** -3
# tk = n / B
# tochik = 2 * tp + delta_tp + tq + tac
#
#
# # Створюємо функції для Rk, Rochn, Rpp, Rapb
# def Rk(n, kzkk):
#     return (n - kzkk) / n
#
#
# def Rochn(lmbda):
#     return (n - kvzz) / n * (1 - tochik / (lmbda * tk + 2 * tochik))
#
#
# def Rpp(lmbda):
#     return (n - kvzz) / n * (1 - lmbda * tk / (lmbda * tk + tochik))
#
#
# def Rapb(lmbda):
#     return (n - kvzz) / n * (1 - lmbda * tk)
#
#
# # Створюємо діапазон значень для λ
# lmbda = np.linspace(0, 2.5, 500)
#
# # Обчислюємо значення функцій для кожного λ
# Rochn_vals = Rochn(lmbda)
# Rpp_vals = Rpp(lmbda)
# Rapb_vals = Rapb(lmbda)
#
# # Побудова графіку
# plt.figure(figsize=(10, 6))
# plt.plot(lmbda, Rochn_vals, label="Rochn(λ)", linestyle='--', color='green')
# plt.plot(lmbda, Rpp_vals, label="Rpp(λ)", linestyle='-.', color='blue')
# plt.plot(lmbda, Rapb_vals, label="Rapb(λ)", linestyle=':', color='magenta')
#
# # Додаємо позначки
# plt.axvline(x=1.209, color='red', linestyle='--', label="λ гпп")
# plt.axvline(x=2.34375, color='green', linestyle='--', label="λ АПБ")
# plt.axhline(y=0.9375, color='orange', linestyle='--', label="n-kzkk/n")
#
# # Налаштування графіку
# plt.xlabel('λ')
# plt.ylabel('R')
# plt.title('Залежність відносної швидкості СПД від інтенсивності завад')
# plt.legend()
# plt.grid(True)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
#
# # Параметри
# n = 234 / 4  # Довжина одного кадру (пакету)
# m = 37.5  # Довжина коригуючого коду
# tk = 37.5  # Час передачі
# lambda_values = np.linspace(0, 40, 100)  # Діапазон інтенсивності завад
#
# # Вірність для систем з ВЗЗ
# Pzts = 1 - 2 ** (- (n - m))  # Ймовірність коректної передачі для ВЗЗ
#
# # Вірність для систем з коригуючим кодом
# Pzsk = (1 - 2 ** (- (n - m))) * (1 + lambda_values * tk) * np.exp(-lambda_values * tk)
#
# # Побудова графіка
# plt.figure(figsize=(16, 10))  # Збільшення розміру графіка
#
# # Графік для системи з ВЗЗ
# plt.plot(lambda_values, np.full_like(lambda_values, Pzts), label='Рзц (ВЗЗ)', color='blue', linestyle='-', linewidth=4)
#
# # Графік для системи з коригуючим кодом
# plt.plot(lambda_values, Pzsk, label='Рзцк (Коригуючий код)', color='green', linestyle='-', linewidth=2)
#
# # Додавання міток та заголовку
# plt.title('Залежності вірності передачі даних від інтенсивності завад', fontsize=18)
# plt.xlabel('Інтенсивність завад λ', fontsize=16)
# plt.ylabel('Вірність передачі Pзц та Pзцк', fontsize=16)
# plt.axhline(y=0.9999999997671694, color='red', linestyle='--', label='Pзц = 0.9999999997671694', linewidth=2)
# plt.axhline(y=2.014e-20, color='orange', linestyle='--', label='Pзцк = 2.014e-20', linewidth=2)
#
# plt.grid(True)
# plt.legend(fontsize=14)
# plt.xlim(0, 40)
# plt.ylim(-0.1, 1.1)  # Зміна межі Y для кращої видимості
# plt.xticks(np.arange(0, 41, 5), fontsize=14)
# plt.yticks(np.arange(0, 1.1, 0.1), fontsize=14)
#
# plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Параметри
n = 16384  # Довжина кадру (пакету)
k_vzz = 32  # Кількість коригуючих біт (для ВЗЗ)
k_zkk = 64  # Кількість коригуючих біт (для ЗКК)
tk = 6.8267  # Час передачі пакету (с)
tochik = 0.4  # Час очікування (с)
B = 2400  # Технічна швидкість передачі (bps)
Ppom = 0.0343  # Ймовірність помилки
lambda_values = np.linspace(0, 10, 100)  # Інтенсивність завад (λ)

# Збільшуємо всі значення відносних швидкостей у 5 разів для кращої візуалізації
scale_factor = 5

# Відносна швидкість передачі для СПД з ЗКК
Rk = ((n - k_zkk) / n) * scale_factor

# Відносна швидкість передачі з очікуванням
Roch = (((n - k_vzz) / n) * (1 - (tochik + 2 * tk) / (tk + tochik))) * scale_factor

# Інтенсивність помилок
L = B * Ppom

# Відносна швидкість з безперервною передачею
Rpp = ((L / n) * (1 - L / (tk + tochik))) * scale_factor

# Граничне значення інтенсивності завад для безперервної передачі
Lgr = (L + tk + tochik) * scale_factor

# Відносна швидкість з адресним перезапитом
Rapb = ((L / n) * (1 - L / tk)) * scale_factor

# Граничне значення інтенсивності завад для адресного перезапиту
Lapb = (L / tk) * scale_factor

# Побудова графіка
plt.figure(figsize=(12, 8))

# Відносна швидкість передачі для СПД з ЗКК
plt.plot(lambda_values, np.full_like(lambda_values, Rk), label='$R_k$', color='blue', linestyle='-', linewidth=2)

# Відносна швидкість передачі з очікуванням
plt.plot(lambda_values, np.full_like(lambda_values, Roch), label='$R_{och}$', color='green', linestyle='-', linewidth=2)

# Відносна швидкість з безперервною передачею
plt.plot(lambda_values, np.full_like(lambda_values, Rpp), label='$R_{pp}$', color='red', linestyle='-', linewidth=2)

# Відносна швидкість з адресним перезапитом
plt.plot(lambda_values, np.full_like(lambda_values, Rapb), label='$R_{apb}$', color='purple', linestyle='-',
         linewidth=2)

# Граничне значення інтенсивності завад для безперервної передачі
plt.axhline(y=Lgr, color='orange', linestyle='--', label='$L_{gr}$', linewidth=2)

# Граничне значення інтенсивності завад для адресного перезапиту
plt.axhline(y=Lapb, color='brown', linestyle='--', label='$L_{apb}$', linewidth=2)

# Налаштування графіку
plt.title('Залежність відносної швидкості передачі від інтенсивності завад (λ)', fontsize=16)
plt.xlabel('Інтенсивність завад λ', fontsize=14)
plt.ylabel('Відносна швидкість передачі (масштабована)', fontsize=14)
plt.grid(True)
plt.legend(fontsize=12)
plt.xlim(0, 10)
plt.ylim(0, max([Rk, Roch, Rpp, Rapb, Lgr, Lapb]) * 1.1)
plt.show()
