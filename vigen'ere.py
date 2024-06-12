import random

def Vigener(tekst,klucz):
    szyfr=''
    pary = zip(tekst,klucz)
    for i, j in pary:
        szyfr += chr((((ord(i)-97)+(ord(j)-97))%26)+97) #przechodzimy najpierw do -97 a pozniej na nowo do +97
    return szyfr
    
def deszyfr(szyfr1,klucz):
    tekst=''
    pary = zip(szyfr1,klucz)
    for i, j in pary:
        tekst += chr((((ord(i)-97)-(ord(j)-97))%26)+97) #-97 sie skroci mozna nie pisać
    return tekst

def generuj_klucz(n):
    klucz=''
    for i in range(n):
        klucz += chr(random.randint(0,25)+97)
    return klucz

tekst=input("Podaj tekst: ")
n=len(tekst)
#klucz=input("Podaj klucz: ")
klucz=generuj_klucz(n)
szyfr1=Vigener(tekst,klucz)
print("Szyfrogram: ",szyfr1)
print("Odszyfrowany: ",deszyfr(szyfr1,klucz))