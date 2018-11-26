import turtle

n = 12
t1 = turtle.Turtle()
t1.shape('turtle')
for i in range(n):
    t1.forward(150)
    t1.stamp()
    t1.left(180)
    t1.forward(150)
    t1.left(180+360/n)
