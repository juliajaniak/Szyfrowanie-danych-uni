#Szyfr RSA - szyfruje i deszyfruje tekst w postaci liczby naturalnej

from egcd_2 import egcd 
from egcd_2 import odwrot 
from szybkie_potegowanie import szybkie_pot 

def nwd(a,b):
    if b>0:
        return nwd(b,a%b)
    return a
    
def pub_wykl(p,q):
    b = 3
    while ((nwd(b,(p-1)*(q-1))!=1) or (b>=p*q)):
        b += 2
    return b
    #q(n)=q(p*q)=q(p)*q(q)=(p-1)(q-1)

p = int(input("Podaj liczbę pierwszą p: "))
q = int(input("Podaj liczbę pierwszą q: "))
n=p*q
print("Moduł klucza: n=",n)
b=pub_wykl(p,q)
print("Wykładnik klucza publicznego: b =",b)
print("Klucz publiczny: (%d,%d)"%(b,n))
x=int(input("Podaj tekst (0<x<%d): "%(n+1)))
#ta liczba musi się mieścić w Zn

y=pow(x,b,n) #x^b modn
print("Szyfrogram: ",y)

#klucz prywatny!
def pryw_wykl(b,p,q):
    return odwrot(b,(p-1)*(q-1))
#pow(b,-1,(p-1)*(q-1))

a=pryw_wykl(b,p,q)
print("Wykładnik klucza prywatnego: a =",a)
print("Klucz prywatny: (%d,%d)"%(a,n))

x1=pow(y,a,n) #y^a modn
print("Tekst odszyfrowany: ",x1)
