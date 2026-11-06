
quantity_sbj = int(input('Your quantity subject, please input: '))
out_user = 0
list_sbj = []
while quantity_sbj > out_user:
    sub = 'Laboratorna  #' + str(out_user + 1) + ':'
    list_sbj.append(input(sub))
    out_user += 1
quantity_sbj = quantity_sbj
out = 0
v = 0
list_ball = []
while quantity_sbj > out:
    print('<',list_sbj[v],'>')
    ball_sbj = input(f'Please input your ball for,{list_sbj[v]} ')
    list_ball.append(ball_sbj)
    v += 1
    out += 1

len_list = len(list_sbj)
i = 0
a = 0
while i <= len_list:
    i += 1
    if i <= len_list:
        print(list_ball[a])
        a += 1

    elif i > len_list:
        break

# if quantity_sbj == 2:
#     a = int(list_ball[0])
#     b = int(list_ball[1])
#     sr = (a + b)/quantity_sbj
#     print(f'Твой средний балл:{sr}')
# if quantity_sbj == 3:
#     a = int(list_ball[0])
#     b = int(list_ball[1])
#     c = int(list_ball[2])
#     sr = (a + b + c) / len_list
#     print(f'Твой средний балл:{sr}')
# if quantity_sbj == 5:
#     a = int(list_ball[0])
#     b = int(list_ball[1])
#     c = int(list_ball[2])
#     d = int(list_ball[3])
#     e = int(list_ball[4])
#     sr = (a + b + c + d + e)/quantity_sbj
#     print(f'Твой средний балл:{sr}')
#     if sr > 74.6:
#         print('Ты зачислен')
#     else:
#         print('Ти НЕ зарахований ')



# m = 0
# while quantity_sbj == len_list:#количество елементов в списке которшое мы узнаем через функцию :
#     sum = list_ball[0] + list_ball[m]
#     m += 1
#     print(sum)

sum = sum(list_ball)
a = sum / len_list
print(a)

