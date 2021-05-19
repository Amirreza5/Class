from turtle import Turtle, done, forward, left

t = Turtle()
#dayere asli
t.color('black')
t.begin_fill()
t.circle(200)
t.end_fill()

#dayere koochak sefid payin safhe
t.penup()
t.goto(0, 50)
t.pendown()
t.color('white')
t.begin_fill()
t.circle(25)
t.end_fill()
#dayere bozork sefid balaye safhe
t.penup()
t.goto(0, 200)
t.pendown()
t.color('white')
t.begin_fill()
t.circle(90)
t.end_fill()
#dayere koochak siah balaye safhe
t.penup()
t.goto(0,265)
t.pendown()
t.color('black')
t.begin_fill()
t.circle(25)
t.end_fill()

t.penup()
t.goto(0,200)
t.pendown()
t.color('blue')
for x in range(50):
    forward(3)
    left(5)

done()