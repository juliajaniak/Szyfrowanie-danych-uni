#RSA 2.0

pierwsze = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
            41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
            89, 97, 101, 103, 107, 109, 113, 127, 131,
            137, 139, 149, 151, 157, 163, 167, 173, 179,
            181, 191, 193, 197, 199, 211, 223, 227, 229,
            233, 239, 241, 251, 257, 263, 269, 271, 277,
            281, 283, 293, 307, 311, 313, 317, 331, 337,
            347, 349, 353, 359, 367, 373, 379, 383, 389,
            397, 401, 409, 419, 421, 431, 433, 439, 443,
            449, 457, 461, 463, 467, 479, 487, 491, 499,
            503, 509, 521, 523, 541, 547, 557, 563, 569,
            571, 577, 587, 593, 599, 601, 607, 613, 617,
            619, 631, 641, 643, 647, 653, 659, 661, 673,
            677, 683, 691, 701, 709, 719, 727, 733, 739,
            743, 751, 757, 761, 769, 773, 787, 797, 809,
            811, 821, 823, 827, 829, 839, 853, 857, 859,
            863, 877, 881, 883, 887, 907, 911, 919, 929,
            937, 941, 947, 953, 967, 971, 977, 983, 991, 997]


import random
def egcd(a,b):
    if a==0:
        return(b,0,1)
    else:
        g,y,x=egcd(b%a,a)
        return (g,x-(b//a)*y,y)
    
def odwrot(a,m):
    g,x,y=egcd(a, m)
    if g!= 1:
        print("Błąd.")
    else: 
        return x%m
    
def NWD(a,b):
    if b>0:
        return NWD(b,a%b)
    return a
    
def pub_wykl(p,q):
    b = 3
    while ((NWD(b,(p-1)*(q-1))!=1) or (b>=p*q)):
        b += 2
    return b

def pryw_wykl(b,p,q):
    return odwrot(b,(p-1)*(q-1))

def Rabin_Miller(n):
    s=n-1 
    r=0
    while s%2==0: 
        s = s//2
        r += 1
    for j in range(proba):
        a = random.randint(2,n-1)
        v=pow(a,s,n)
        if v!=1:
            i=0
            while v!=n-1: 
                if i == r-1:
                    return False
                else: 
                   i += 1
                   v = (v**2)%n
    return True

def pierwsza(n):
    if n<2:
        return False
    if n in pierwsze:
        return True
    for p in pierwsze:
        if n%p==0:
            return False
    return Rabin_Miller(n)

def generuj_pierwsza(k):
    while True:
        n=random.randint(2**(k-1),2**k)
        if pierwsza(n):
            return n
    
proba=3
k=10

p=generuj_pierwsza(k)
q=generuj_pierwsza(k)

n=p*q
b=pub_wykl(p,q)

#print("Klucz publiczny: (%d,%d)"%(b,n))
x=int(input("Podaj tekst x (0<x<%d): "%(n+1)))

y=pow(x,b,n)
print("Szyfrogram: ",y)

a=pryw_wykl(b,p,q)
#print("Klucz prywatny: (%d,%d)"%(a,n))
x1=pow(y,a,n)
print("Tekst odszyfrowany: ",x1)
