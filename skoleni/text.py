from random import *

def kecej():
    kdom = choice(('Kamarád','Spolužák','Roman','Pavel'))
    kdoz = choice(('Kamarádka','Spolužačka','Romana','Pavla'))
    delal = choice(('viděl','napsal','zazpíval','prozradil'))
    if choice(('z','m'))=="z":
        kdo = kdoz
        delal = delal+'a'
    else:
        kdo = kdom
    jake = choice(('velke','malé','křivé','směšné'))
    co = choice(('tajemství','překvapení'))
    veta = kdo + ' ' + delal + ' ' + jake + ' ' + co + '.'
    print(veta)

for i in range(10):
    kecej()
