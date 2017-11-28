for i in range (4):
    if i==0:
        print ("první řádek")
    else:
        print ("není první")

r = int ( input ('zadej počet řádků čtverce: '))

for t in range(r):
    if t==0 or t==r-1:
        for j in range(r+1):
            print ("X", end='')
    else:
        for k in range(r+1):
            if k==0 or k==r:
                 print("X")
            else:
                 print (" ")

# faktorial
n = int (input('zadej n: '))
for i in range (n+1):
	fak = i * (i+1)

# posloupnost a delitelnost
for i in range (101):
    if i%3 + i%5  == 0:
        print ('Bum bác', end=" ")
        i+=1
    elif i%3 == 0:
        print ('bum', end=" ")
        i+=1
    elif i%5 == 0:
        print ('bác', end=" ")
        i+=1
    else:
        print (i, end=" ")
        i+=1

# prvocislo
n = int( input ('zadej číslo: ')

if (n%=2 or n%=3 or n%=5 or n%=7)     == 0
			or n != 7 or n!=5 or n!=3 or n!=2 or n!=1:
				print ('není prvočíslo')
else:
	print ('je to prvočíslo')

# fibonachi
for g in range (n+1):
	fib = g + g + 1
	print (g + fib)
