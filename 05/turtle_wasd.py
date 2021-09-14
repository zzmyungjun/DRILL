import turtle

def turtle_upmove():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def turtle_downmove():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def turtle_leftmove():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def turtle_rightmove():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

turtle.shape('turtle')
turtle.onkey(turtle_upmove,'Up')
turtle.onkey(turtle_downmove,'Down')
turtle.onkey(turtle_leftmove,'Left')
turtle.onkey(turtle_rightmove,'Right')
turtle.onkey(restart,'Escape')
turtle.listen()
