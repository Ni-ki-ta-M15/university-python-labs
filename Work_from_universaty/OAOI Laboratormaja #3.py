import time
import turtle as tur

brezenhem = tur.Pen()
"""
in_p = int(input('C координаты х: ')), int(input('С координаты у: '))
brezenhem.penup()
brezenhem.goto(in_p)
brezenhem.pendown()
brezenhem.pensize(4)
print('----------------')
to_p = (int(input('В координаты х: ')), int(input('В координаты у: ')))
brezenhem.goto(to_p)
time.sleep(5)


brezenhem.screen.setup(800, 800)
brezenhem.up()
brezenhem.goto(-450, 0)
brezenhem.pensize(3)
brezenhem.color('yellow', 'black')
brezenhem.down()
brezenhem.setheading(270)
for i in range(5):                             #ВОЛНЫ
    brezenhem.circle(50, 180)
    brezenhem.begin_fill()
    brezenhem.circle(-50, 180)
    brezenhem.end_fill()
brezenhem.screen.exitonclick()
brezenhem.screen.mainloop()
"""




import turtle

turtlePen = turtle.Turtle()
window = turtle.Screen()


def polygon(n, size=80):
    if n > 2:
        angle = 360 / n

        for n in range(0, n):
            turtlePen.left(angle)
            turtlePen.forward(size)


turtlePen.speed(10)

for i in range(0, 100, 5):
    polygon(3, 10 + i)
    turtlePen.left(20)

size = 40

for i in range(0, 80):
    polygon(4, size)
    turtlePen.left(5)
    size = size + 3
window.mainloop()






# import turtle
#
# turtlePen = turtle.Turtle()
# window = turtle.Screen()
#
# window.bgcolor("black")
#
#
# def polygon(n, size=80):
#     if n > 2:
#         angle = 360 / n
#
#         for n in range(0, n):
#             turtlePen.left(angle)
#             turtlePen.forward(size)
#
#
# turtlePen.speed(100)
#
# colors = ['orange', 'cyan', 'blue', 'green', 'red', 'pink']
#
# size = 40
#
# for i in range(0, 75):
#     turtlePen.color(colors[i % 5])
#     polygon(4, size)
#     turtlePen.left(4)
#     size = size + 3
#
#
#
# window.mainloop()