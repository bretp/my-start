import tkinter
from random import *
canvas= tkinter.Canvas(width=400,height=400)
canvas.pack()

def animace():
    global ly, lx, body
    ly += 5
    canvas.delete('lopta')
    canvas.create_oval(lx-5,ly-5,lx+5,ly+5,fill='red',tags='lopta')
    if kx < lx < kx+50 and 360 <= ly <= 370: #jsem  to chytil, musím jen vyřešit body
        ly = 0
        lx = randrange(400)
        body +=1
        canvas.delete('oznam')
        canvas.create_text(200,20,text=body,tags='oznam')

    if ly>380: #jsem nechytil, musím jen vyřešit body
        ly = 0
        lx = randrange(400)
        body -=1
        canvas.delete('oznam')
        canvas.create_text(200,20,text=body,tags='oznam')
    if body>-2:
        canvas.after(100,animace)
    else:
        canvas.create_text(200,200,text='konec',font='Arial 30')

def posunkurzor(souradnice):
    global kx
    kx = souradnice.x
    canvas.delete('kurzor')
    canvas.create_line(kx,370,kx+50,370,width=5,fill='blue',tags='kurzor')




lx = randrange(400)
ly = 0
kx = 200
body = 0
canvas.create_line(kx,370,kx+50,370,width=5,fill='blue',tags='kurzor')
canvas.create_text(100,20,text='počet bodů:')
canvas.create_text(200,20,text=body,tags='oznam')

animace()
canvas.bind('<Motion>',posunkurzor)


canvas.mainloop()
