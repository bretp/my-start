import tkinter
from random import *
canvas= tkinter.Canvas(width=400,height=400)
canvas.pack()

#každý vykreslený objekt má ID jako pořadové číslo canvas.move(ID, dx, dy)

obdelnik = canvas.create_rectangle(10,10,20,20)
canvas.move(obdelnik,10,20) #ID objektu si automaticky pamatuje u názvu proměnné

canvas.create_rectangle(50,100,100,130,fill='blue',tags='auto')
canvas.create_oval(55,125,65,135,fill='yellow',tags='auto')
canvas.create_oval(85,125,95,135,fill='yellow',tags='auto')

autox = 50

def animace():
    global autox
    canvas.move('auto',10,0)
    autox += 10
    if autox>400:
        canvas.move('auto',-400,0)
        autox -=400
    canvas.after(100,animace)

animace()


canvas.mainloop()
