import math

try:
    m = int(input('Enter \'M\' number: '))
    n = int(input('Enter \'N\' number: '))
    k = int(input('Enter \'K\' number: '))
    result = (m - math.sqrt(n))/k
    round_result = round(result, 2)
    print(f'Your result: {round_result}')
except ZeroDivisionError:
    print()
    print('Number \'K\' enter 0; It\'s not correct!!!')
except ValueError:
    print()
    print('Last introduction enter not correct, you entered letter!')


