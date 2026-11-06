"""w = int(input("Введите ширину: "))
h = int(input("Введите высоту: "))

for i in range(h):
    if i == 0 or i == h - 1:
        for j in range(w):
            print('XXX', end='')
    else:
        print('XXX', end='')
        for j in range(1, w - 1):
            print('XXX', end='')
        print('XXX', end='')
    print()"""

"""
def get_list(n):
    return list(range(1, n+1)) + list(range(n-1,0,-1)) # Рисует строку так, как нам нужно

print('Пишите не > 9 ) (Потом не красиво)')
inp = int(input('Сколько цифр в ромбе?  '))

height = get_list(inp) # Центральный вертикальный столбец
width = inp*2-1 # Ширина центральной строки. Она берётся как максимальная ширина всего ромба


for step in height: # Идём сверху вниз по вертикальному столбцу
    strs = (str(x) for x in get_list(step)) # И генерируем горизонтальные
    level = ''.join(strs)
    print(level.center(width))
    """

size = int(input('Введите ширину: '))
if size == 12:
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
    print('Операцию ввыполнить невозможно!')
else:
    print("Что вы ввели???")