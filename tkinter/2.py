from tkinter import *
from random import random
root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
r = 50


def left_click(event):
    print("left click at", event.x, event.y)
    x = event.x
    y = event.y
    canv.create_oval(x-r/2, y-r/2, x + r/2, y + r/2,
                     fill='#%0x%0x%0x' % (int(random()*16), int(random()*16), int(random()*16)))


def right_click(event):
    print('right click at', event.x, event.y)
    canv.delete(ALL)


canv.bind('<Button-1>', left_click)
canv.bind('<Button-3>', right_click)

mainloop()
