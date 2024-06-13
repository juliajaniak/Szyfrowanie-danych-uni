def nwd(a,b):
    if b>0:
        return nwd(b,a%b)
    return a
    
def pub_wykl(p,q):
    b = 3
    while ((nwd(b,(p-1)*(q-1))!=1) or (b>=p*q)):
        b += 2
    return b

p = int(input("Podaj liczbę p: "))
q = int(input("Podaj liczbę q: "))
n=p*q

b=pub_wykl(p,q)

x=input("Podaj tekst: ")


def pryw_wykl(b,p,q):
    return pow(b,-1,(p-1)*(q-1))

def str_to_nr(s):
    k = 0
    for i, j in enumerate(s):
        k += (ord(j) - 97) * (26 ** i)
    return k

x1=str_to_nr(x)
print("Liczba x: ",x1)
y=pow(x1,b,n)
print("Szyfrogram: ",y)

a=pryw_wykl(b,p,q)
y1=pow(y,a,n)
print("Tekst odszyfrowany: ",y1)
