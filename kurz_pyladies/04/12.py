r = int ( input ('zadej počet řádků čtverce: '))

for t in range(r):
    if t==0 or t==r-1:
        for j in range(r+1):
            print ("X", end='')
    else:
        for k in range(r+1):
            if k==0 or k==r:
                 print("X", end='')
            else:
                 print (" ", end='')
