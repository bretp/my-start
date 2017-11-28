import tkinter
from random import *
canvas= tkinter.Canvas(width=400,height=400)
canvas.pack()

def kresli():
    x = randrange(400)
    y = randrange(400)
    canvas.create_rectangle(x-10,y-10,x+10,y+10)
    canvas.create_text(x,y,text=int(vstup1.get())*10)

button1 = tkinter.Button(text='kresli', command=kresli)

button1.place(x=100,y=100) #umístí tlačítko kdekoli, můžu s tím umístit i popisek Label
button1.pack() #tohle teprve vykreslí ono tlačítko
popisek = tkinter.Label(text='napis cislo')
popisek.pack()
vstup1 = tkinter.Entry()
vstup1.pack()







canvas.mainloop()
