import turtle

a = 0.05
t1 = turtle.Turtle()
t1.shape('turtle')
for i in range(1000):
    t1.forward(a)
    t1.right(2)
    a += 0.01
