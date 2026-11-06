import time
import turtle as tur

brez_Lab4 = tur.Pen()

# in_p = int(input('Координата по х: ')), int(input('Координата по y: '))
# brez_Lab4.penup()
# brez_Lab4.goto(in_p)
# brez_Lab4.pendown()
#
# radius = int(input('circle radius (px): '))
# brez_Lab4.circle(radius)
# time.sleep(2)

#333

# in_point_Ox = int(input('Координата по х: '))
# in_point_Oy = int(input('Координата по y: '))
#
# average_Ox = int(in_point_Ox/2)
# average_Oy = int(in_point_Oy/2)
#
# print(f'Я начинаю с точки х: {average_Ox}')
# print(f'Я начинаю с точки у: {average_Oy}')
#
# brez_Lab4.penup()
# brez_Lab4.goto(average_Ox, average_Oy)
# brez_Lab4.pendown()
#
# radius = int(input('circle radius (px): '))
# brez_Lab4.begin_fill()
# brez_Lab4.color('red') # color
# brez_Lab4.circle(radius)
# brez_Lab4.end_fill()
# time.sleep(2)

# 333

# brez_Lab4.speed(2 )
# brez_Lab4.penup()
# brez_Lab4.goto(95, 210)
# brez_Lab4.pendown()
# brez_Lab4.goto(-64, 50)
#
# brez_Lab4.penup()
# brez_Lab4.goto(180, -10)
# brez_Lab4.pendown()
# brez_Lab4.pensize(4)
#
# brez_Lab4.begin_fill()
# brez_Lab4.color('blue', 'red')
# brez_Lab4.forward(87)
# brez_Lab4.left(115)
# brez_Lab4.forward(111)
# brez_Lab4.left(131)
# brez_Lab4.forward(111)
# brez_Lab4.end_fill()
#
# brez_Lab4.penup()
# brez_Lab4.goto(-270, 140)
# brez_Lab4.pendown()
# brez_Lab4.pensize(2)
#
# brez_Lab4.begin_fill()
# brez_Lab4.color('yellow', 'grey')
# brez_Lab4.circle(76.5)
# brez_Lab4.end_fill()
#
# brez_Lab4.penup()
# brez_Lab4.goto(-254, -195)
# brez_Lab4.pendown()
# brez_Lab4.pensize(5)
#
# brez_Lab4.forward(123)
# brez_Lab4.right(90)
# brez_Lab4.forward(66)
# brez_Lab4.right(90)
# brez_Lab4.forward(123)
# brez_Lab4.right(90)
# brez_Lab4.forward(66)
# brez_Lab4.right(90)
#
# brez_Lab4.penup()
# brez_Lab4.goto(190, -100)
# brez_Lab4.pendown()
# brez_Lab4.pensize(1)
#
# brez_Lab4.begin_fill()
# brez_Lab4.color('blue', 'pink')
# brez_Lab4.forward(200)
# brez_Lab4.right(70)
# brez_Lab4.forward(80)
# brez_Lab4.right(81)
# brez_Lab4.forward(90)
# brez_Lab4.pensize(2)
# brez_Lab4.left(10)
# brez_Lab4.forward(75)
# brez_Lab4.right(70)
# brez_Lab4.forward(80)
# brez_Lab4.right(45)
# brez_Lab4.forward(120)
# brez_Lab4.right(22)
# brez_Lab4.forward(22)
# brez_Lab4.end_fill()
# brez_Lab4.begin_fill()
# brez_Lab4.color('pink', 'blue')
# brez_Lab4.goto(180,210)
# i = 0
# while i <= 15:
#     brez_Lab4.forward(15)
#     brez_Lab4.left(18)
#     i += 1
# brez_Lab4.forward(90)
# v = 0
# while v <= 15:
#     brez_Lab4.forward(6)
#     brez_Lab4.left(25)
#     v += 1
# brez_Lab4.end_fill()


#-----------------------------------------------------------------------------------------------------------------
# import turtle
#
# # Основные цвета для персонажа
# BODY_COLOR = 'red'
# GLASS_COLOR = 'skyblue'
#
# # Главный объект
# t = turtle.Turtle()
#
#
# # Метод для рисования тела
# def body():
# 	t.pensize(30) # Размер кисти
#
# 	t.fillcolor(BODY_COLOR) # Цвет заполнения
# 	t.begin_fill()
#
# 	# Сторона справа
# 	t.right(90)
# 	t.forward(50)
# 	t.right(180)
# 	t.circle(40, -180)
# 	t.right(180)
# 	t.forward(200)
#
# 	# Голова
# 	t.right(180)
# 	t.circle(100, -180)
#
# 	# Сторона слева
# 	t.backward(20)
# 	t.left(15)
# 	t.circle(500, -20)
# 	t.backward(20)
#
# 	t.circle(40, -180)
# 	t.left(7)
# 	t.backward(50)
#
# 	t.up()
# 	t.left(90)
# 	t.forward(10)
# 	t.right(90)
# 	t.down()
#
# 	t.right(240)
# 	t.circle(50, -70)
#
# 	t.end_fill()
#
#
# # Рисуем очки
# def glass():
# 	# Передвигаем черепашку
# 	t.up()
# 	t.right(230)
# 	t.forward(100)
# 	t.left(90)
# 	t.forward(20)
# 	t.right(90)
# 	t.down()
#
# 	# Устанавливаем цвет
# 	t.fillcolor(GLASS_COLOR)
# 	t.begin_fill()
#
# 	t.right(150)
# 	t.circle(90, -55)
#
# 	t.right(180)
# 	t.forward(1)
# 	t.right(180)
# 	t.circle(10, -65)
# 	t.right(180)
# 	t.forward(110)
# 	t.right(180)
#
# 	t.circle(50, -190)
# 	t.right(170)
# 	t.forward(80)
#
# 	t.right(180)
# 	t.circle(45, -30)
#
# 	t.end_fill()
#
#
# # Рисуем рюкзак
# def backpack():
# 	t.up()
# 	t.right(60)
# 	t.forward(100)
# 	t.right(90)
# 	t.forward(75)
#
# 	t.fillcolor(GLASS_COLOR)
# 	t.begin_fill()
#
# 	t.down()
# 	t.forward(30)
# 	t.right(255)
#
# 	t.circle(300, -30)
# 	t.right(260)
# 	t.forward(30)
# 	t.end_fill()


# # Вызываем все необходимые методы
# body()
# glass()
# backpack()
#
# turtle.done()
# #--------------------------------------------------------------------------------------------------------------------------

# import turtle
# brez_Lab4 =turtle.Pen()
# turtle.bgcolor("black")
# colors=["red","yellow","blue","orange","purple","gray"]
# name=turtle.textinput("Введите своё имя","Ввод имени")#просим ввести имя в окне
# for x in range(50):
#     brez_Lab4.pencolor(colors[x%6])
#     brez_Lab4.penup()
#     brez_Lab4.forward(x*6)
#     brez_Lab4.pendown()
#     brez_Lab4.write(name,font=("Arial",10,"bold"))
#     brez_Lab4.left(360/6+3)

# from random import *
# from tkinter import *
#
# size = 600
# root = Tk()
# canvas = Canvas(root, width=size, height=size)
# canvas.pack()
# diapason = 0
# while diapason < 700:
#     colors = choice(['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange',
#                   'pink', 'purple', 'red','yellow', 'violet', 'indigo', 'chartreuse', 'lime', '#f55c4b'])
#     x0 = randint(0, size)
#     y0 = randint(0, size)
#     d = randint(0, size / 5)
#     canvas.create_oval(x0, y0, x0+d, y0+d, fill=colors)
#     root.update()
#     diapason += 1

import turtle

turtlePen = turtle.Turtle()
window = turtle.Screen()

window.bgcolor("black")


def polygon(n, size=100):
    if n > 2:
        angle = 360 / n

        for n in range(0, n):
            turtlePen.left(angle)
            turtlePen.forward(size)


turtlePen.speed(100)

colors = ['yellow', 'blue']
col = ['black', 'red']

size = 10

turtlePen.pensize(3)
for i in range(0, 50):
    turtlePen.speed(400)
    turtlePen.color(colors[i % 2])
    polygon(20, size)
    turtlePen.right(10)
    size = size + 5
time.sleep(3)
window.bgcolor("white")
for s in range(0, 50):
    turtlePen.color(col[s % 2])
    polygon(20, size)
    turtlePen.left(10)
    size = size - 5



window.mainloop()

time.sleep(5)

