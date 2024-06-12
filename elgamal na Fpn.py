#pip install sympy
from sympy.polys.domains import ZZ
from sympy.polys.galoistools import *

K = ZZ
p = 2

def bit_to_list(b):
    l=[]
    for i in b:
        l.append(int(i))
    return l

def list_to_bit(l):
    b=''
    for i in l:
        b+=str(i)
    return b
    
def klucz(g,a,f,p,K):
    A = gf_pow_mod(g,a,f,p,K)
    return A

def szyfrowanie(g,b,f,A,m,p,K):
    B=gf_pow_mod(g,b,f,p,K) #pow(g,b,p)
    X=gf_pow_mod(A,b,f,p,K) #pow(A,b,p)
    Y=gf_mul(X,m,p,K) #x*X
    C=gf_rem(Y,f,p,K) #Y%p
    
    return B,C

def deszyfrowanie(B,C,a,f,p,K):
    Z=gf_pow_mod(B,a,f,p,K)
    D,Q,R=gf_gcdex(Z,f,p,K)
    L=gf_mul(D,C,p,K)
    M=gf_rem(L,f,p,K)
    return M

f=input("Podaj bity f: ")
g=input("Podaj bity g: ")
a=int(input("Podaj wykl a: "))

g=bit_to_list(g)
f=bit_to_list(f)

A = klucz(g,a,f,p,K)
print("Klucz publiczny: (%s, %s)" %(list_to_bit(g),list_to_bit(A)))
print("Klucz prywatny: ",a)

m=input("Podaj bity m: ")
m=bit_to_list(m)
b=int(input("Podaj wykl b: "))
B,C=szyfrowanie(g,b,f,A,m,p,K)

print("Szyfrogram: (%s, %s)" %(list_to_bit(B),list_to_bit(C)))
M=deszyfrowanie(B,C,a,f,p,K)
print("Wiadomość: %s" %list_to_bit(M))