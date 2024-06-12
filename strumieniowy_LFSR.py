
def xor(a,b):
    X=''
    for i,j in zip(a,b):
        x = str(int(i)^int(j))
        X += x
    return X


def LFSR(tekst):
    seed='1000'
    b1=seed[0]
    b2=seed[1]
    b3=seed[2]
    b4=seed[3]
    
    c=seed
    n=len(tekst)
    for i in range(4,n):
        t = xor(b1,b2)
        c += t
        b1 = b2
        b2 = b3
        b3 = b4
        b4 = t
    return c

tekst=input("Podaj tekst: ")
wynik=LFSR(tekst)
print("Strumień klucza: ",wynik)
szyfrogram = xor(tekst,wynik) #szyfr strumieniowy to xorowanie kolejnych elementów tekstu jawnego i klucza
print("Szyfrogram: ",szyfrogram)
