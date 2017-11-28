import tkinter
from random import *
canvas= tkinter.Canvas(width=400,height=400)
canvas.pack()

def kruh(x,y):
    canvas.create_oval(x-5,y-5,x+5,y+5)

def cara(souradnice):
    x=souradnice.x #atribut fce má parametr x
    y = souradnice.y
    barva='black'
    if x<=200 and y<=200:
        barva='green'
    if x<=200 and y>=200:
        barva="yellow"
    if 0<y<200 and 200<x<400:
        barva='red'
    if 200<y<400 and 200<x<400:
        barva="blue"
        kruh(x,y)
    canvas.create_line(200,200,x,y,width=5,fill=barva)

canvas.bind('<Button-1>',cara)


canvas.mainloop()
