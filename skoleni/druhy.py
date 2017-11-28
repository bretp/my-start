import tkinter
from random import *
canvas = tkinter.Canvas(width=400,height=400)
canvas.pack()

canvas.create_line(50,50,300,randrange(400),fill=choice(('red','green','orange')))

canvas.create_rectangle(50,100,50+randrange(100),100+randrange(200))

#chci li stejnou šířku i délku 'čtverec' vylosovanou náhodně, potřebuji proměnnou do které to nalosuji
velikost = randrange(100)
canvas.create_rectangle(50,100,50+velikost,100+velikost)
canvas.create_text(50+velikost/2,100+velikost/2, text=velikost)

#dopravní značka na náhodném místě s náhodnou povolenou rychlostí
rychlost=str(randint(3,10))+'0'
#rychlost=randrange(10,100,10) #s krokem 10
#rychlost=choice((10,20,30)) #výběrem
x=randrange(100)
y=randrange(100)

canvas.create_oval(x,300,x+100,400,fill='',outline='red',width='20')
canvas.create_text(x+50,350,text=rychlost,font='Calibri 40 bold')

# více značek vedle sebe je důvodem k opakování, tedy cyklus for
#for i in (1,'ahoj',8,2,6):   #cyklus projde n-ticí hodnot (tuple)
y = 400
for i in range(1,6):
    x = randrange(400)

    canvas.create_text(x,y,text = i)
    canvas.create_rectangle(x-10,y-10,x+10,y+10)
    #canvas.create_rectangle(x-10,y-10,x+10,y+10) #už není v cyklu
    x=x+25


canvas.mainloop()
