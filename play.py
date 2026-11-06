import random
import time

start = input('Вы запустили игру "Камень, ножницы, бумага". Хотите поиграть? (Вводите + или -): ')

if start == '+':
    print('Загрузка...')
    time.sleep(1)
    print("Загрузка завершена! Начинаем!")
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...", end='\n\n')
    time.sleep(1)
    print('Если захотите закончить вводите "-".')
    print('Если захотите узнать счёт вводите "с".', end="\n\n")
    user_point = 0
    rand_point = 0
    x = 0
    while x == 0:
        user = input("Камень, ножницы или бумага? (Вводите к, н или б): ")
        list_play_bot = ['камень', 'ножницы', 'бумага']
        list_play = ['к', 'н', 'б']
        if user in list_play:
            rand = random.choice(list_play_bot)
            print("Я выбрал: ", rand, end="\n\n")
            if rand == 'камень' and user == 'н':
                rand_point += 1
                print('I won')
            if rand == 'камень' and user == 'б':
                user_point += 1
                print('You won')
            if rand == 'ножницы' and user == 'к':
                user_point += 1
                print('You won')
            if rand == 'ножницы' and user == 'б':
                rand_point += 1
                print('I won')
            if rand == 'бумага' and user == 'н':
                user_point += 1
                print('You won')
            if rand == 'бумага' and user == 'к':
                rand_point += 1
                print('I won')
            if rand == 'камень' and user == 'к':
                rand_point += 1
                user_point += 1
                print('Draw')
            if rand == 'ножницы' and user == 'н':
                rand_point += 1
                user_point += 1
                print('Draw')
            if rand == 'бумага' and user == 'б':
                rand_point += 1
                user_point += 1
                print('Draw')
        elif user == 'с':
            print('Ваши баллы - ', user_point, '. Баллы вашего соперника - ', rand_point, ".", end='\n\n')
            if user_point > rand_point:
                print('Вы лидируете! ')
            elif user_point < rand_point:
                print('Вы отстаете (')

        elif user == '-':
            if user_point > rand_point:
                print('Вы выиграли! ')
            elif user_point < rand_point:
                print('Вы проиграли( ')
            print('Ваши баллы - ', user_point, '. Баллы вашего соперника - ', rand_point, ".")
            print('Конец игры! Заходите ещё!')
            break
        else:
            print('Вводите к, н или б')


elif start == '-':
    print('Жаль... :-(')
else:
    print('Простите, я вас не понял, если хотите играть перезапустите программу и введите "+". Спасибо!')
