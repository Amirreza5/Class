
from turtle import *

shape_ = input('Please enter the shape you want to be drawn: ')

if shape_ == 'square':
    forward(150)
    left(90)
    forward(150)
    left(90) 
    forward(150)
    left(90)
    forward(150)
    left(90)
elif shape_ == 'rectangle':
    forward(200)
    left(90)
    forward(100)
    left(90) 
    forward(200)
    left(90)
    forward(100)
    left(90)
elif shape_ == 'triangle':
    forward(150)
    left(120)
    forward(150)
    left(120)
    forward(150)
    left(120)
done()