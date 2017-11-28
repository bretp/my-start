import tkinter
from random import *
canvas= tkinter.Canvas(width=400,height=400)
canvas.pack()
#canvas2= tkinter.Canvas(width=400,height=400,bg='yellow')
#canvas2.pack()
def klik(souradnice):
    print(type(souradnice)) #vyhodnotím co to je za typ
    x=souradnice.x #fce má zapuzdřenou speciální proměnnou a ta má parametr x
    y = souradnice.y
    canvas.create_oval(x-5,y-5,x+5,y+5)

def cara(souradnice):
    x=souradnice.x #atribut fce má parametr x
    y = souradnice.y
    canvas2.create_line(200,400,x,y,width=5,fill='green')

def pis(info):
    if info.char=='a':
        print('Ahoj')
    elif info.char=='c':
        print('čau')
    elif info.char=='d':
        print('Dobrý den')
    else:
        print('nemám pozdrav')

def pis2(info):
    if info.char=='a':
        print('Ahoj')
    if info.char=='c':
        print('čau')
    if info.char=='d':
        print('Dobrý den')
    else:
        print('nemám pozdrav')


#canvas.bind('<Button-1>',klik)
canvas.bind('<Button-1>',klik)
canvas.bind_all('<Button-3>',cara) #reaguje na obou plátnech

#canvas.bind_all('<a>',pis)
canvas.bind_all('<Key>',pis2)  #když potřebuji ukázat jak vnořit if

#'<Button-1>' levé '<Button-1>' pravé '<Button-1>' třetí '<Motion>' pohyb myši '<B1Motion>' pohyb se zmáčknutým tlačítkem '<ButtonRelease-1>'

canvas.mainloop()
