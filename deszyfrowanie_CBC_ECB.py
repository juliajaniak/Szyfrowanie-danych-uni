#deszyfrujące

def podziel(tekst,n):
    wynik = [tekst[i:i+n] for i in range(0,len(tekst),n)]

    for i in range(n-len(wynik[-1])):
        wynik[-1] = wynik[-1] + '0'
    return wynik


def xor(a,b):
    X=''
    for i,j in zip(a,b):
        x = str(int(i)^int(j))
        X += x
    return X

def blok(X,Pi):
    Z=''
    for i in range(len(X)): 
        Z += X[Pi[i]]
    return Z 

def blok_odwr(Y,Pi):
    Z = ''
    for i in range(len(Y)):
        Z+=Y[Pi.index(i)]
    return Z

def szyfr_ECB(P):
    C=''
    for X in P: 
        c = blok(X,Pi) 
        C += c
    return C

def szyfr_CBC(P):
    C=''
    y=wektor
    for X in P:
        wynik = xor(X,y)
        c = blok(wynik,Pi)
        y = c 
        C += c 
    return C

def deszyfr_ECB(szyfr):
    P = podziel(szyfr,n)
    D=''

    for Y in P:
        d = blok_odwr(Y,Pi)
        D+=d

    return D

def deszyfr_CBC(szyfr):
    P = podziel(szyfr,n)
    D=''
    y=wektor

    for Y in P:
        d = blok_odwr(Y,Pi)
        wynik = xor(d,y)
        y = Y
        D+=wynik
    return D

wybor=input("Tryb ECB czy CBC? (E/C)")  
tekst=input("Podaj tekst: ")
n=int(input("Podaj rozmiar bloku: "))
P=podziel(tekst,n)
Pi=eval(input("Podaj permutacje: "))

if wybor == 'E':
    szyfr=szyfr_ECB(P)
    deszyfr=deszyfr_ECB(szyfr)
elif wybor == 'C':
    wektor=input("Podaj wektor IV: ")
    szyfr=szyfr_CBC(P)
    deszyfr=deszyfr_CBC(szyfr)
else:
    print("Podano zły format.")

print("Szyfrogram: ",szyfr)
print("Deszyfr: ",deszyfr)


