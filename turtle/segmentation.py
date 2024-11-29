# import turtle

# w=turtle.Screen();
# w.screensize(300,200);

# tut=turtle.Turtle();
# tut.setpos(300,0);

# x=tut.xcor();
# y=tut.ycor();
# print(x,y);
# tut.forward(300);
# w.exitonclick();

import turtle as t
window = t.Screen()
t.screensize(300,200)
t.setworldcoordinates(0, 0, 300, 200)
t = t.Turtle()
t.penup()
t.setpos(100, 0)
t.pendown()
t.setpos(100, 200)
t.penup()
t.setpos(200, 0)
t.pendown()
t.setpos(200, 200)
window.exitonclick()