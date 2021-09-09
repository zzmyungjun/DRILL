import turtle as t

t.penup()
t.goto(-250,-250)
t.pendown()
count=6
a=-150
while(count>0):
    t.forward(500)
    t.penup()
    t.goto(-250,a)
    a=a+100
    t.pendown()
    count=count-1
    
t.penup()
t.right(90)
t.goto(250,250)
count=6
b=150
t.pendown()

while(count>0):
    t.forward(500)
    t.penup()
    t.goto(b,250)
    b=b-100
    t.pendown()
    count=count-1
