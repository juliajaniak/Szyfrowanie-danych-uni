import random
def Vernam(tekst, klucz):
    szyfr=''
    pary=zip(tekst,klucz) #pary się utworzą
    for i, j in pary: #i odpowiada za znak tekstu, a j za znak klucza
        szyfr += chr(ord(i)^ord(j)) #jak będą te same znaki to daje 0
    return szyfr 
    
def generuj_klucz(n):
    klucz=''
    for i in range(n):
        klucz += chr(random.randint(0,25)+97) #randomowy klucz losujemy liczbe z Z26 i dodajemy +97 do kodu ASCII na nasze a b c
    return klucz

tekst=input("Podaj tekst: ")
n=len(tekst)
#klucz=input("Podaj klucz: ")
klucz=generuj_klucz(n)
szyfr1=Vernam(tekst,klucz)
print("Szyfrogram: ",szyfr1.encode()) #wychodzi ciąg zapisany w ASCII 16-nastkowym
##deszyfrująca
print("Deszyfrująca: ",Vernam(szyfr1,klucz)) #bo jest to samo w deszyfrujacej ale na wyniku

