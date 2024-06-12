#p, q należy do P, n = p*q, fi(n)=(p-1)(q-1)
#b=nwd(b,fi(n))=1
#gcd -> wartość liczby b 0<b<fi(n)
#y=x^b mod n
#a: b^-1 mod fi(n)
#x=y^a mod n

#szyfr homomorficzny RSA do znajdowania średniej geometrycznej

from gcd import *

p=int(input('Podaj p: '))
q=int(input('Podaj q: '))
n=p*q
b=pub_wykl(p,q)
a=pow(b,-1,(p-1)*(q-1))

k=int(input('Ile danych: '))
Y=1

for i in range(k):
    x=int(input('Podaj x%d (0<x%d<%d): ' %(i+1,i+1,n)))
    y=pow(x,b,n)
    Y*=y%n
X=pow(Y,a,n)
print('Śr. geom. zaszyfr. danych: %f'  %(X**(1/k)))

