from kod_1 import *
from kod_2 import *
from kod_3 import *
from kod_3_1 import *
from kod_4 import *
from kod_5 import *
from podzial import *

#kodony
def kod_I(x):
    N=''
    for i in x:
        j=kod_22[i]
        N+=j
    return N

def kod_Ia(x):
    N=''
    for i in x:
        j=kod_2[i]
        N+=j
    return N

def tekst_do_bit(tekst):
    bit=''
    for i in tekst:
        j=kod_44[i]
        bit+=j
    return bit

def bit_do_tekst(bit):
    tekst=''
    for i in bit:
        j=kod_4[i]
        tekst+=j
    return tekst

def transkrypcja(c):
    N=''
    for i in c:
        j=kod_3_1[i]
        N+=j
    return N

#łańcuch znaków aminokwasów
def translacja(c):
    y=''
    for i in c:
        if len(i) == 3:
            y+=kod_5[i]
        else:
            y+=i
    return y

def szyfrowanie(x,K):
    B=tekst_do_bit(x)
    b=podziel(B,3)
    c=''
    Z=zip(b,K)
    for i,j in Z:
        k=i+j
        c+=k
    Y=podziel(c,2)
    y=kod_I(Y)
    return y

def deszyfrowanie(y,K):
    Y = podziel(y,1)
    Y = kod_Ia(Y)
    
    Y = podziel(Y,4)

    x = ''
    for i in Y:
        x += i[:3]
    
    x = podziel(x,8)
    
    x = bit_do_tekst(x)
    return x

print("* SZYFR DNA III *")
x=input('Podaj tekst: ')
K=input('Podaj klucz: ')
y1=szyfrowanie(x,K)
y=transkrypcja(y1)
y=podziel(y,3)
y=translacja(y)

t = ''
wynik = ''
for i in range(len(y)):
    t += y[i]
    if len(t) == 3:
        wynik += ('(%s)' %t)
        t = ''
wynik += t
print('Szyfrogram: %s' %wynik)

deszyfr = deszyfrowanie(y1,K)
print('Deszyfrowanie: %s' %deszyfr)

