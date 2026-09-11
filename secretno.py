import turtle
t = turtle.Turtle()
t.pensize(5)
t.speed(3)
size = 100
for i in range(4):
    t.setheading(90 * i)
    t.forward(size)
    t.right(90)
    t.forward(size)
    t.penup()
    t.home()
    t.pendown()
t.hideturtle()
turtle.done()