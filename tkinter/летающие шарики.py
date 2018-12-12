from tkinter import *

dt = 0.2
r = 30
sleep_time = 10


def time_handler():
    global x, y, Vx, Vy
    ax = 2
    ay = 1
    x = x + Vx*dt
    y = y + Vy*dt
    Vx = Vx + ax*dt
    Vy = Vy + ay*dt
    if y + r > 600:
        y = 600 - r
        Vy = - Vy
    if x + r > 800:
        x = 800 - r
        Vx = - Vx
    canvas.coords(oval1_id, x, y, x + r, y + r)
    root.after(sleep_time, time_handler)


def initialize():
    global root, canvas, oval1_id
    global x, y, Vx, Vy
    root = Tk()
    root.geometry('800x600')
    canvas = Canvas(root, bg='white')
    canvas.pack(fill=BOTH, expand=1)
    x = 350
    y = 250
    Vx = 10
    Vy = 2
    oval1_id = canvas.create_oval(x, y, x + r, y + r, fill="yellow")
    root.after(2000, time_handler)


initialize()
root.mainloop()
