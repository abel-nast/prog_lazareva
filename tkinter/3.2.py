from tkinter import *
from random import *
s = 0


def balls():
    global x, y, r
    x = randint(50, 750)
    y = randint(50, 550)
    r = randint(0, 100)
    root.after(2000, balls)
    canv.delete(ALL)
    canv.create_oval(x - r / 2, y - r / 2, x + r / 2, y + r / 2,
                     fill='#%0x%0x%0x' % (int(random() * 16), int(random() * 16), int(random() * 16)))


def counter(event):
    global x, y, r, s
    a = event.x
    b = event.y
    while x-r/2 <= a <= x+r and y-r/2 <= b <= y+r and s < 10:
        s += 1
        canv.delete(ALL)
        canv.create_text(775, 575, text=s, font='Arial 25')
        break


root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

root.after_idle(balls)
canv.bind('<Button-1>', counter)
root.mainloop()
