from turtle import *
w=Screen()
t=Turtle();
color('blue') 
x=4;
while(x!=0):
    t.forward(200)
    t.left(90)
    x-=1;
t.penup()
t.forward(100)
t.color('red')
t.pendown()
t.circle(100)
w.exitonclick();