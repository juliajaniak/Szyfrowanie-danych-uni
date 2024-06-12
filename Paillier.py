#Paillier

#import math --> math.gcd(a,b) = (nwd), math.lcm(a,b) = (nww)

import math

p=int(input('Podaj p: '))
q=int(input('Podaj q: '))
n=p*q
lmbda=math.lcm(p-1,q-1)
g=n+1

def L(x):
    y=(x-1)/n
    return int(y)

mi=pow(L(pow(g,lmbda,n*n)),-1,n)

def szyfrowanie(x,r):
    c=((pow(g,x,n*n))*(pow(r,n,n*n)))%(n*n)
    return c

def deszyfrowanie(y):
    m=((L(pow(y,lmbda,n*n)))*mi)%n
    return m

x1=int(input('Podaj x1: '))
r1=int(input('Podaj r1: '))

x2=int(input('Podaj x2: '))
r2=int(input('Podaj r2: '))

y1=szyfrowanie(x1,r1)
y2=szyfrowanie(x2,r2)
Y=(y1*y2)%(n*n)

X=deszyfrowanie(Y)
print('Suma głosów wyborców: ',X)
