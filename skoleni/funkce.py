import tkinter
from random import *
canvas= tkinter.Canvas(width=400,height=400)
canvas.pack()

def dom():
    x = randrange(400)
    y = randrange(400)
    canvas.create_rectangle(x,y,x+50,y+50)
    canvas.create_line(x,y,x+25,y-30,x+50,y)

dom() #jakmile se provede funkce, zapomenou se lokální proměnné, které jsou ve fci

def dom2(x,y,f):
    canvas.create_rectangle(x,y,x+50,y+50,fill=f)
    canvas.create_line(x,y,x+25,y-30,x+50,y)

dom2(100,100,'red')


def mocnina(a):
    return a*a #ukončí fci a vrátí hodnotu

b= mocnina(16) #výsledek fce načtu do proměnné
print(mocnina(10)) #výsledek funkce rovnou vytisknu

canvas.mainloop()
