from colours import color_list
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed(0)
tim.penup()
tim.hideturtle()

tim.setx(-350)
tim.sety(-350)

columns = 10
rows = 10
step = 50
dotsize = 20

for i in range(rows):
    tim.setx(-350)
    tim.sety(step * i - 350)
    for n in range(columns):
        tim.dot(dotsize, random.choice(color_list))
        tim.forward(step)


screen = t.Screen()
screen.exitonclick()