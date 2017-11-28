import tkinter
from random import *
canvas= tkinter.Canvas(width=400,height=400)
canvas.pack()

def animace():
    global y
    y = y+5
    canvas.delete('all')
    canvas.create_oval(x-5,y-5,x+5,y+5)
    if y>350:
        y = 10
    if pokracovat ==1: #kdyby pokracovat bylo=True tak by zde bylo jen if pokracovat:
        canvas.after(100,animace)

def stop(info):
    global pokracovat
    if pokracovat==1:
        pokracovat=0
    else:
        pokracovat=1
        animace()

x = 200
y = 10
pokracovat = 1
animace()
canvas.bind_all('<space>',stop)


canvas.mainloop()
