import turtle

t1 = turtle.Turtle()
t1.shape('turtle')
a = 30
for i in range(10):
    t1.penup()
    t1.goto(-a/2, -a/2)
    t1.pendown()
    for b in range(4):
        t1.forward(a)
        t1.left(90)
    a += 20
