import tkinter
# práce v grafickém prostředí tkinter, *rgb* soubor v nainstalovanem python adresáři obsahuje barvy pojmenované

canvas = tkinter.Canvas(width=600,height=500, bg='yellow') #otevře se okno - bez parametrů má 378x265
canvas.pack() #vykreslí plátno do okna

#trojúhelník
canvas.create_line(100,200,300,200,100,100,100,200,fill='blue',width=5)
canvas.create_line(0,0,300,200,) #ostatní parametry až za souřadnice

#obdélník (bez fill je průhledný, s nulovou šířkou souřadnice se vykreslí alespoň čára)
canvas.create_rectangle(100,100,250,200,fill='red',outline='',width='4')

#elipsa (vepsaná do obdelníka)
canvas.create_oval(300,300,500,400)

#vypsání textu (poze jednoslovné názvy fontů)
canvas.create_text(100,100,text='Ahoj',font='Calibri 30 bold')
canvas.create_text(200,100,text='Ahoj',font=('Times New Roman', 30, 'bold'), angle=90, anchor='nw')

#dopravní značka
canvas.create_oval(300,300,400,400,fill='',outline='red',width='20')
canvas.create_text(350,350,text='6 t',font='Calibri 40 bold')



canvas.mainloop() #mimo IDLE je potřeba, aby plátno nezmizelo, je tedy vždy na konci
