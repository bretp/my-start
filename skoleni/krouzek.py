import tkinter
from random import *
canvas= tkinter.Canvas(width=400,height=400)
canvas.pack()

def kruh():
    x = randrange(400)
    y = randrange(400)
    if 50<x<100 or 100<y<150:
        canvas.create_oval(x-5,y-5,x+5,y+5,fill='green')
    else:
        canvas.create_oval(x-5,y-5,x+5,y+5,fill='yellow')
    canvas.after(100,kruh) # zapne časovač, každou 100 milisekundu vytvoř kruh

kruh()



canvas.mainloop()
