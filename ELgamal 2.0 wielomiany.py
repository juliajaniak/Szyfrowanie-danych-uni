#pip install sympy
from sympy.polys.domains import ZZ
from sympy.polys.galoistools import *
from numpy import poly1d

K = ZZ
p = 2

def zamien(B):
    D=[]
    n = len(B)
    for i in range(n):
        D.append(B[n-i-1])
    return D

def poly_to_list(f):
    f = f.split('+')
    d = {}
    L = []
    for k in f:
        L.append(int(k[2:]))
    for i in range(0,L[0]+1):
        if i in L:
            d[i] = 1
        else:
            d[i] = 0
    K = list(d.values())
    return zamien(K)
  
def klucz(g,a,f,p,K):
    A = gf_pow_mod(g,a,f,p,K)
    return A

def szyfrowanie(g,b,f,A,m,p,K):
    B=gf_pow_mod(g,b,f,p,K)
    X=gf_pow_mod(A,b,f,p,K)
    Y=gf_mul(X,m,p,K)
    C=gf_rem(Y,f,p,K)
    
    return B,C

def deszyfrowanie(B,C,a,f,p,K):
    Z=gf_pow_mod(B,a,f,p,K)
    D,Q,R=gf_gcdex(Z,f,p,K)
    L=gf_mul(D,C,p,K)
    M=gf_rem(L,f,p,K)
    return M

f=input("Podaj f: ")
g=input("Podaj g: ")
a=int(input("Podaj wykl a: "))

g=poly_to_list(g)
f=poly_to_list(f)

A = klucz(g,a,f,p,K)
print("Klucz publiczny: ",end='\n')
print(poly1d(g),end= '\n')
print(poly1d(A),end='\n')
print("Klucz prywatny: ",a)

m=input("Podaj m: ")
m=poly_to_list(m)

b=int(input("Podaj wykl b: "))
B,C=szyfrowanie(g,b,f,A,m,p,K)

print("Szyfrogram: ",end= '\n')
print(poly1d(B),end='\n')
print(poly1d(C),end='\n')
M=deszyfrowanie(B,C,a,f,p,K)
print("Wiadomość: ",end='\n')
print(poly1d(M))