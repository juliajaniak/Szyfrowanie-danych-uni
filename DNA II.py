#DNA II
from kod_1 import *
from podzial import *
import numpy as np

kod_6 ={
    'A':'0',
    'T':'1',
    'G':'2',
    'C':'3'}

def zamien(slownik):
    slownik_1={}
    for klucz, wartosc in slownik.items():
        slownik_1[wartosc]=klucz
    return slownik_1

kod_66 = zamien(kod_6)

def kod_I(x):
    N=''
    for i in x:
        j=kod_11[i]
        N+=j
    return N

def kod_Ia(x):
    N=''
    for i in x:
        j=kod_1[i]
        N+=j
    return N

def kod_VI(x):
    N = ''
    for i in x:
        j = kod_6[i]
        N +=j
    return N

def kod_VIa(x):
    N = ''
    for i in x:
        j = kod_66[i]
        N += j
    return N

def suma(lista):

    macierz = np.array([[int(znak) for znak in wiersz] for wiersz in lista])
    
    wiersz = np.sum(macierz, axis=1) % 4
    kolumna = np.sum(macierz, axis=0) % 4
    calosc = (wiersz.sum() + kolumna.sum()) % 4
    
    return wiersz, kolumna, calosc

def szyfrowanie(x):
    X = kod_I(x)
    N = kod_VI(X)

    D = podziel(N,6)

    wiersz, kolumna, calosc = suma(D)

    y = ''
    for i in range(len(D)):
        y += D[i] + str(wiersz[i])
    
    y += ''.join(str(numer) for numer in kolumna)
    y += ''.join(str(calosc))

    K = kod_VIa(y)
    return K

def deszyfrowanie(y):
    N = kod_VI(y)
    N = N[:-7]

    K = ''
    for i in range(len(N)):
        if (i+1)%7 != 0:
            K += N[i]
    
    X = podziel(K,1)
    D = kod_VIa(X)

    L = podziel(D,3)
    M = kod_Ia(L)
    return M

print("* SZYFR DNA II *")
x = input('Podaj tekst: ')
y = szyfrowanie(x)
print("Szyfrogram: %s" %y)
x1 = deszyfrowanie(y)
print("Deszyfrowanie: %s" %x1)