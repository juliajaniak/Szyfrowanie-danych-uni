#szyfr blokowy afiniczny
from macierz_odwrotna_modulo import macierz_odwrotna
from iloczyn_macierzy_modulo import iloczyn_macierzy
import random
import numpy

def wektor(n):
    lista=[]
    for i in range(n):
        liczba = random.randint(0,25) #wybieramy losowo liczbe
        lista.append(liczba)
    return lista

def macierz(n):
    return numpy.random.randint(0,25,size=(n,n)) #macierz nxn ktora ma w sobie same randomowe liczby

#NWD(det(L),26)==1
def NWD(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def dobra(L,n): #macierz jest dobra do odwracania jezeli wyznacznik !=0 oraz NWD(wyznacznik,mod)==1 
    wyznacznik = numpy.linalg.det(L)
    if NWD(wyznacznik,26)==1:
        return "NWD(det(M),26)==1"
    else:
        return "zła"
    
def kod(tekst):
    T=[]
    for i in tekst:
        T.append(ord(i)-97)
    return T

def dekod(szyfr):
    L=[]
    for i in szyfr:
        L.append(chr(i+97))
    return L

def wypisz(L,n):
    for i in range(n):
        print("%s"%L[i],end='')

def blokowy_szyfr_afiniczny(T,M,v): #musimy pomnożyc Macierz losowa*Tekst jawny + wektor losowy
    szyfr = (numpy.dot(M,T) + v)%26
    return szyfr


tekst=input("Podaj tekst: ")
T=kod(tekst)
print("Wektor tekstu: ",T)

n = len(tekst)
M=macierz(n)

while dobra(M,n)=="zła":
    M=macierz(n)
print("Macierz klucza: ","\n",M)

print(dobra(M,n))
v=wektor(n)
print("Wektor losowy: ",v)

C=blokowy_szyfr_afiniczny(T,M,v)

S=dekod(C)
print("Szyfrogram: ")
wypisz(S,n)

def blokowy_deszyfr_afiniczny(C,M1,v):
    odejmowanie=numpy.array(C)-numpy.array(v) #tak trzeba bo to sa dwie listy a nie macierze
    deszyfr = iloczyn_macierzy(M1,odejmowanie,26)
    return deszyfr

szyfrogram=input("\nPodaj szyfrogram: ")
C=kod(szyfrogram)
n=len(szyfrogram)

M1=macierz_odwrotna(M,26) #M^-1mod26
print("Macierz odwrotna do M:\n",M1)
print("M*M^(-1) mod 26:\n",iloczyn_macierzy(M1,M,26))

D=blokowy_deszyfr_afiniczny(C,M1,v)
D=[int(x) for x in D] #bo mi zwraca kropki a ja chce int
W=dekod(D)
print("Tekst odszyfrowany: ")
wypisz(W,n)
#działa do 12 znaków