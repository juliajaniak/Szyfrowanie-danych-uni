#szyfr Rabina

from egcd import *

def szyfrowanie(x,n):
    y = pow(x,2,n)
    return y

def deszyfrowanie(p,q,y):
    d,yp,yq=egcd(p,q)
    a = pow(y,(p+1)//4,p)
    b = pow(y,(q+1)//4,q)
    r=(yp*p*b+yq*q*a)%n
    s=(yp*p*b-yq*q*a)%n
    R= -r%n
    S= -s%n
    return r,s,R,S
print('* SZYFR RABINA *')
p=int(input('Podaj p: '))
q=int(input('Podaj q: '))
x=int(input('Podaj x: '))
n=p*q

y=szyfrowanie(x,n)
print('Szyfrogram: ',y)
print('Wiadomości: ')
X=deszyfrowanie(p,q,y)
print(X)
