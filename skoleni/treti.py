import tkinter
from random import *
canvas = tkinter.Canvas(width=400,height=400)
canvas.pack()

x=200
y=200
for i in range(6):
    canvas.create_text(x,y,text=' '*15+'love', angle=i*60, font='Arial 30')


canvas.mainloop()
