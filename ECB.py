#ECB szyfr - binarny

def podziel(tekst,n):
    wynik = [tekst[i:i+n] for i in range(0,len(tekst),n)]
    #czyli dzielimy sobie co np. 4 i dajemy ten wycinek

    #gdyby było nieparzyście:
    for i in range(n-len(wynik[-1])):
        wynik[-1] = wynik[-1] + '1'
    return wynik

def blok(X,Pi):
    Z=''
    for i in range(len(X)): #czyli 4
        Z += X[Pi[i]] #odwołujemy się do elementu w permutacji żeby odczytało najpierw ktory element zamienia się na który
    return Z #do pojedynczego wywołania czyli X

def szyfr_ECB(P):
    C=''
    for X in P: #czyli te elementy pokolei np. ['1001','1010'] to bierze pierwszy itd
        c = blok(X,Pi) #na nim robimy tą permutacje
        C += c #dodajemy do całości
    return C

tekst=input("Podaj tekst: ")
n=int(input("Podaj rozmiar bloku: "))
P=podziel(tekst,n)
Pi=eval(input("Podaj permutacje: ")) #wczytuje nam liste
Sz=szyfr_ECB(P)
print("Szyfrogram: ",Sz)
