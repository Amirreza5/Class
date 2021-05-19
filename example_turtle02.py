from turtle import Turtle, done

name = input('Please enter the shape: ')

T = Turtle()  #Staart of the turtle code

if name == 'circle':
    T.color('Blue')
    T.circle(150)

elif name == 'square' :
    T.forward(100)
    T.left(90)
    T.forward(100)
    T.left(90)
    T.forward(100)
    T.left(90)
    T.forward(100)
    T.left(90)

done()    #end of the turtle code