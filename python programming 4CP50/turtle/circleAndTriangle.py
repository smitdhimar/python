import turtle

window=turtle.Screen()
turtle=turtle.Turtle()

turtle.color('purple')
turtle.begin_fill();
turtle.forward(60)
turtle.right(120);
turtle.forward(60)
turtle.right(120);
turtle.forward(60)
turtle.right(120);
turtle.end_fill();

turtle.color('red')
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

window.exitonclick();