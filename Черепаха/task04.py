import turtle

n = 60
t1 = turtle.Turtle()
t1.shape('turtle')

for i in range(n):
    t1.forward(10)
    t1.left(360/n)
