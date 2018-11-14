from tkinter import *
from random import *


def balls():
    x = randint(50, 750)
    y = randint(50, 550)
    r = randint(0, 100)
    root.after(1000, balls)
    canv.delete(ALL)
    canv.create_oval(x - r / 2, y - r / 2, x + r / 2, y + r / 2,
                     fill='#%0x%0x%0x' % (int(random() * 16), int(random() * 16), int(random() * 16)))


root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

root.after_idle(balls)
root.mainloop()
