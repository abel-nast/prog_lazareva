import turtle

t1 = turtle.Turtle()
t1.shape('turtle')
a = 10
for i in range(15):
    t1.forward(a)
    t1.left(90)
    t1.forward(a)
    t1.left(90)
    a += 10
