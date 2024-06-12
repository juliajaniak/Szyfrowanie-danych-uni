from kod_1 import *
from kod_2 import *
from kod_3 import *
from podzial import *

#kodony
def kod_I(x):
    N=''
    for i in x:
        N += kod_11[i]
    return N

#alfabet
def kod_I2(x):
    N=''
    for i in x:
        N+=kod_1[i]
    return N

#znaki zasad
def kod_II(x):
    N=''
    for i in x:
        N+=kod_2[i]
    return N

#bity
def kod_II2(x):
    N=''
    for i in x:
        N+=kod_22[i]
    return N

#znaki zasad
def transkrypcja(x):
    N=''
    for i in x:
        N+=kod_3[i]
    return N

def xor(B,b):
    z=zip(B,b)
    X=''
    for i,j in z:
        k=int(i)^int(j)
        X+=str(k)
    return X

def szyfrowanie(x, K):
    d=kod_I(x)
    D=kod_I(K)
    b=kod_II(d)
    B=kod_II(D)
    Y=xor(B,b)
    Y=podziel(Y,2)
    y=kod_II2(Y)
    y=transkrypcja(y)
    return y

def deszyfrowanie(y, K):
    D=kod_I(K)
    B=kod_II(D)
    Y=transkrypcja(y)
    b=kod_II(Y)
    X=xor(B,b)
    X=podziel(X,2)
    X=kod_II2(X)
    X=podziel(X,3)
    x=kod_I2(X)
    return x
    
print("* SZYFR DNA I *")
x=input('Podaj tekst: ')
K=input('Podaj klucz: ')
sz = (szyfrowanie(x,K))
print('Szyfrogram: %s' %sz)
odsz = deszyfrowanie(sz,K)
print('Tekst odszyfr: %s' %odsz)
