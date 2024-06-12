#szyfr CBC

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

def szyfr_CBC(P):
    C=''
    y=wektor
    for X in P:
        wynik = xor(X,y)
        c = blok(wynik,Pi)
        y = c 
        C += c 
    return C

tekst=input("Podaj tekst: ")
n=int(input("Podaj rozmiar bloku: "))
P=podziel(tekst,n)
Pi=eval(input("Podaj permutacje: "))
wektor=input("Podaj wektor IV: ")
sz = szyfr_CBC(P)
print("Szyfrogram: ",sz)
