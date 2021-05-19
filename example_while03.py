from turtle import Turtle, done,
from random import randint

t = Turtle()


while True:
    t.penup()
    t.goto(randint(-250, 250), randint(-250, 250))
    t.pendown()
    t.color('violet')
    t.begin_fill()
    a = 1
    while a <= 4:
        t.forward(100)
        t.left(90)
        a += 1
    t.end_fill()
done()