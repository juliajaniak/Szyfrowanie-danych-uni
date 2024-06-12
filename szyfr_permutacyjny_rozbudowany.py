import numpy
from numpy import dot

#szyfr permutacyjny

def wypisz(L,n):
    for i in range(n):
        print("%s"%L[i],end='') #to nam scala dane literki ze zamiast a b c bedzie abc

def kod(tekst):
    T=[]
    for i in tekst:
        T.append(ord(i)-97)
    return T #tutaj zwracamy liste z tymi liczbami z zakresu 0,26


def dekod(szyfr):
    L=[]
    for i in szyfr:
        L.append(chr(i+97))
    return L #dekodujemy liczby z zakresu a,z

def szyfr_permutacyjny(T,M):
    A = numpy.array(M) #zeby wyszlo musza byc obie zrobione na numpy.array
    b = numpy.array(T)
    return A.dot(b) #mnożenie macierzy

tekst = input('Podaj tekst: ')
T = kod(tekst) ##lista liczb kodu tekstu
n = len(tekst)
init = [i for i in range(n)] #tutaj po prostu 1,2,3 itd. for range naszego len(tekst)
find = list(numpy.random.permutation(init)) #tu mamy randomowe permutacje/ustawienia tych naszych utworzonych liczb

M = numpy.zeros((n,n), dtype=int) #same zera na calej dlugosci
M[init,find]=1 #w miejscu jak mamy [wiersz,kolumna] to wstawiamy 1

C=szyfr_permutacyjny(T,M) #mnożymy dwie macierze
S=dekod(C) 
print("Szyfrogram: ")
wypisz(S,n)
print("\nM=\n",M)

##funkcja deszyfrująca
szyfrogram=input("\nPodaj szyfrogram: ")
S = kod(szyfrogram)
n = len(szyfrogram)

def zamien(d):
    nowy={}
    for klucze,wartosci in d.items():
        nowy[wartosci] = klucze
    return nowy

def sortuj(d):
    sortowane = {}
    sort_klucze=sorted(d.keys())
    for klucz in sort_klucze:
        sortowane[klucz] = d[klucz]
    return sortowane

d={}
for i in range(len(M)): #tu juz mamy podany dana macierz na ktorej to dziala
    for j in range(len(M[i])):
        if M[i][j] == 1:
            d[i] = j #jak znajdzie 1 to w slowniku zapisujemy miejsce wystapienia tej 1 na jakim wierszu i jakiej kolumnie


sortowanie = sortuj(d) #najpierw sortujemy nasze klucze po wartosci kluczy
zamiana = zamien(sortowanie) #no i teraz zamieniamy wartosci z kluczami
#w ten sposób mamy macierz odwróconą

M1=numpy.zeros((n,n), dtype=int)
for klucze, wartosci in zamiana.items():
    M1[klucze,wartosci] = 1 #teraz wiemy gdzie mają być 1

print("\nM1=\n",M1)
K=szyfr_permutacyjny(S,M1) #wystarczy raz jeszcze zrobic szyfr permutacyjny
O=dekod(K)
print("Tekst odszyfrowany: ")
wypisz(O,n)