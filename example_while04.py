from turtle import Turtle, circle, done
from random import randint

t = Turtle()

while True:
    t.penup()
    t.goto(randint(-250, 250), randint(-250, 250))
    t.pendown()

    t.circle(50)

done()