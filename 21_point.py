import random
import time
from colorama import init
from colorama import Fore, Back, Style
init()

print('Game \'21 point\'')
print('All rools you know!')
yee = str(input('Right?'))



bank_player = 50

try:
    if yee == 'yes':
        attempts = 0
        while bank_player >= 2 or attempts <= 5:
            if attempts > 2:
                stop = input('Maybe, you need stop?')
                if stop == 'yes':
                    player_earned = int(bank_player - 50)
                    print(f'You have earnet: {player_earned}')
                    break
                if stop == 'no':
                    attempts -= 2
            print('Okay, Let`s go!')
            print(Fore.GREEN, f'You have, {bank_player} $')
            money_minus = int(input('Сколько поставите?: ')) # 60$
            print(Style.RESET_ALL)
            money_player = bank_player - money_minus # 50$ - 60$

            if money_player <= -1:
                print(Fore.BLACK, Back.RED, 'You are haker: return game!!!', Style.RESET_ALL)
                bank_player = 1
                print(f'Now,your bank: {bank_player},$')
                time.sleep(2)
                print('You lost!!!')
                break

            to_x2 = money_minus * 2
            to_x4 = money_minus * 4
            to_x6 = money_minus * 6
            list_21_point = [6, 7, 8, 9, 10, 2, 3, 4, 11]

            firs = random.choice(list_21_point)
            second = random.choice(list_21_point)

            player_list = [firs, second]
            list_21_point.remove(firs)
            list_21_point.remove(second)
            print(list_21_point)
            amount_point = (player_list[0] + player_list[1])
            abount_point = int(amount_point)

            print(f'2 your card: {player_list[0]}, and {player_list[1]}')
            time.sleep(2)
            print(f'Amount: {amount_point}')
            attempts += 1



            while True:
                if amount_point == 21:
                    print(Fore.LIGHTYELLOW_EX, 'You hit the Jackpot!!!', Style.RESET_ALL)
                    bank_player = money_player + to_x6
                    break
                if amount_point < 21:
                    more = input('More?')
                    if more == '+':
                        plus_point = random.choice(list_21_point)
                        player_list.append(plus_point)

                        list_21_point.remove(plus_point)
                        your_sum = sum(player_list)
                        print(f'You got: {plus_point}')
                        print(f'You have', your_sum, 'in your hands')

                        if your_sum > 21:
                            print(Fore.CYAN)
                            print('You loze!')
                            bank_player = money_player
                            print(Style.RESET_ALL)
                            break
                        if your_sum == 21:
                            print(Fore.MAGENTA,'You won!')
                            bank_player = money_player + to_x4
                            print(f'You have, {bank_player} $', Style.RESET_ALL )
                            break

                    plus_point = random.choice(list_21_point)
                    your_sum = sum(player_list)
                    if more == '-':
                        if  your_sum >= 18 and your_sum <= 20 :
                            print(Fore.MAGENTA,'You won')
                            bank_player = money_player + to_x2
                            print()
                            print(f'You have, {bank_player} $',Style.RESET_ALL)
                            break
                        if your_sum <= 17:
                            print('You loze!')
                            bank_player = money_player
                        break
                    if more == '--':
                        player_earned = int(bank_player - 50)
                        print(f'You have earnet: {player_earned}')
                        break


    if yee == 'no':
        print('Okay I will tell you all rools:')
        print('What You’ll Need?')
        print('Under the traditional 21 card game rules, all you need to play is a regular deck of playing cards.')
        time.sleep(2)
        attempts = 0
        while bank_player >= 2 and attempts <= 5:
            if attempts > 2:
                stop = input('Maybe, you need stop?')
                if stop == 'yes':
                    player_earned = int(bank_player - 50)
                    print(f'You have earnet: {player_earned}')
                    break
                if stop == 'no':
                    attempts -= 2

            print('Okay, Let`s go!')
            print(Fore.GREEN, f'You have, {bank_player} $')
            money_minus = int(input('Сколько поставите?: '))
            print(Style.RESET_ALL)
            money_player = bank_player - money_minus
            if money_player <= -1:
                print(Fore.BLACK, Back.RED, 'You are haker: return game!!!', Style.RESET_ALL)
                bank_player = 1
                print(f'Now,your bank = {bank_player}$')
                time.sleep(2)
                print('You lost!!!')
                break
            to_x2 = money_minus * 2
            to_x4 = money_minus * 4
            to_x8 = money_minus * 8
            list_21_point = [6, 7, 8, 9, 10, 2, 3, 4, 11]

            firs = random.choice(list_21_point)
            second = random.choice(list_21_point)

            player_list = [firs, second]
            list_21_point.remove(firs)
            list_21_point.remove(second)
            print(list_21_point)
            amount_point = (player_list[0] + player_list[1])
            abount_point = int(amount_point)
            print(f'2 your card: {player_list[0]}, and {player_list[1]}')
            time.sleep(2)
            print(f'Amount: {amount_point}')

            while True:
                if amount_point == 21:
                    print(Fore.LIGHTYELLOW_EX, 'You hit the JACKPOT!!!', Style.RESET_ALL)
                    bank_player = money_minus + to_x8
                    print(Fore.LIGHTYELLOW_EX, f'You have, {bank_player} $', Style.RESET_ALL)
                    break
                if amount_point < 21:
                    more = input('More?')
                    if more == '+':
                        plus_point = random.choice(list_21_point)
                        player_list.append(plus_point)

                        list_21_point.remove(plus_point)
                        your_sum = sum(player_list)
                        print(f'You got: {plus_point}')
                        print(f'You have', your_sum, 'in your hands')

                        if your_sum > 21:
                            print(Fore.CYAN)
                            print('You loze!')
                            bank_player = money_player
                            print(Style.RESET_ALL)
                            break
                        if your_sum == 21:
                            print(Fore.MAGENTA,'You won!')
                            bank_player = money_minus + to_x4
                            print(f'You have, {bank_player} $', Style.RESET_ALL )
                            break

                    plus_point = random.choice(list_21_point)
                    your_sum = sum(player_list)
                    if more == '-':
                        if  your_sum >= 18 and your_sum <= 20 :
                            print(Fore.MAGENTA,'You won')
                            bank_player = money_player + to_x2
                            print()
                            print(f'You have, {bank_player} $',Style.RESET_ALL)
                            break
                        if your_sum <= 17:
                            print('You loze!')
                            bank_player = money_player
                        break
                    if more == '--':
                        player_earned = int(bank_player - 50)
                        print(Fore.BLUE, f'You have earnet: {player_earned}', Style.RESET_ALL)
                        break

except ValueError:
    print('Please return this program, We are working on improvements!')

