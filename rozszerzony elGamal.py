from sympy.polys.domains import ZZ
from sympy.polys.galoistools import *

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

#generowanie klucza
def klucz(g,a,f,p,K):
    A = gf_pow_mod(g,a,f,p,K);
    return A

#szyfrowanie
def szyfrowanie(g,b,f,A,m,p,K):
    B = gf_pow_mod(g,b,f,p,K)
    X = gf_pow_mod(A,b,f,p,K)
    Y = gf_mul(X,m,p,K)
    C = gf_rem(Y,f,p,K)
    return B, C

#deszyfrowanie
def deszyfrowanie(B,C,a,f,p,K):
    Z = gf_pow_mod(B,a,f,p,K)
    D,Q,R = gf_gcdex(Z, f, p, K)
    L = gf_mul(D,C,p,K)
    M = gf_rem(L,f,p,K)
    return M

K = ZZ
p = 2

print("\n\t* ROZSZERZONY ELGAMAL *\n")

b1 = input('\tPodaj bity f:\t')
f = bit_to_list(b1)

b2 = input('\tPodaj bity g:\t')
g = bit_to_list(b2)

a = int(input('\tPodaj wykl a:\t'))

A = klucz(g,a,f,p,K)

print("\n\tKlucz publiczny: (%s, %s)" %(list_to_bit(g),list_to_bit(A)))
print("\n\tKlucz prywatny: %d" %a)

b3 = input('\n\tPodaj bity m:\t')
m = bit_to_list(b3)

b = int(input("\tPodaj wykl b:\t"))

B,C = szyfrowanie(g,b,f,A,m,p,K)
print("\n\tSzyfrogram: (%s, %s)" %(list_to_bit(B),list_to_bit(C)))

M = deszyfrowanie(B,C,a,f,p,K)

print("\n\tWiadomość: %s" %list_to_bit(M))
