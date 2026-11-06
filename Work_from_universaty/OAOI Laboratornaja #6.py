# import turtle
# t = turtle.Turtle()
# t.shape('turtle')
# t.forward(150)
# t.left(90)
# t.circle(30)
# t.stamp()
# t.forward(150)
# t.left(90)
# t.circle(30)
# t.stamp()
# t.forward(150)

import time
import turtle as tur
b = tur.Pen()
b.penup()
b.goto(-340, -290)
b.pendown()
b.speed(2)
b.pensize(3)
b.begin_fill()
b.color('green', 'black')
b.forward(175)

times = 0
while times != 18:
    times += 1
    b.left(5)
    b.forward(1)
# b.left(5)
# b.forward(1)
# b.left(5)
# b.forward(1)
# b.left(5)
# b.forward(1)
# b.left(5)                 #That`s okay but that write stuped programize
# b.forward(1)
# b.left(5)
# b.forward(1)
# b.left(5)
# b.forward(1)
# b.left(5)
# b.forward(1)
# b.left(5)
# b.forward(1)
# b.left(5)
# b.forward(1)
# b.left(5)
# b.forward(1)
# b.left(5)
# b.forward(1)
# b.left(5)
# b.forward(1)
# b.left(5)
# b.forward(1)
# b.left(5)
# b.forward(1)
# b.left(5)
# b.forward(1)
# b.left(5)
# b.forward(1)
# b.left(5)
# b.forward(1)
# b.left(5)

b.forward(105)
b.left(90)
b.forward(175)

times = 0
while times != 18:
    times += 1
    b.left(5)
    b.forward(1)

b.forward(106)
b.end_fill()

b.penup()
b.goto(-120, -270)
b.pendown()
b.left(90)

b.forward(80)
b.left(135)
b.forward(55)
b.left(90)
b.forward(55)


b.penup()
b.goto(60, -220)
b.pendown()
b.right(45)
time.sleep(2)
b.begin_fill()
b.color('blue', 'yellow')

b.forward(80)
b.left(135)
b.forward(55)
b.left(90)

b.forward(55)

b.penup()
b.goto(90, -220)
b.pendown()
b.left(180)

timess = 0
while timess != 12:
    timess += 1
    b.forward(50)
    b.left(108)
b.end_fill()
time.sleep(2)

b.penup()
b.goto(90, 0)
b.pendown()
b.begin_fill()
b.color('red', 'pink')
b.left(10)
b.forward(90)
timess = 0
while timess != 18:
    timess += 1
    b.forward(12)
    b.left(10)
b.forward(100)
b.end_fill()

b.penup()
b.goto(-200, 175)
b.pendown()
b.begin_fill()
b.color('orange','blue')

b.left(80)

time_sqr = 0
while time_sqr != 4:
    time_sqr += 1
    b.forward(89)
    b.left(90)
b.end_fill()

import turtle
from math import tan, sqrt, pi

def prepare(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()

def draw_polygon(num_sides, side_length):
    angle = 360.0 / num_sides
    for i in range(num_sides):
        turtle.forward(side_length)
        turtle.right(angle)
    turtle.end_fill()

def calc_s(num_sides, side_length):
    return num_sides * side_length ** 2 / (4 * tan(pi/num_sides))

def calc_side(square):
    return sqrt(4 * square * tan(pi/num_sides) / num_sides)

turtle.hideturtle()
turtle.speed(1)

colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'black', 'yellow', 'pink', 'brown']
xcoords = [0, 150, -150, 150, -150, 270, -270, 270, -270]
ycoords = [0, 150, -150, -150, 150, 270, -270, -270, 270]

squares = []
numsides = []
for i in range(9):
    num_sides = i + 3
    square = round(calc_s(num_sides, 100), 2)
    side_length = round(calc_side(10000), 3)
    squares.append(square)
    numsides.append(num_sides)
    print("Углов:", num_sides, "была площадь:", square, "стала длина грани:", side_length,
          "изменение в", round(side_length/100, 2), "раз")
    prepare(xcoords[i], ycoords[i], colors[i])
    draw_polygon(num_sides, side_length)

turtle.exitonclick()
print("Список количество углов:", numsides, end="")
print("Список площади:", squares)

time.sleep(5)
