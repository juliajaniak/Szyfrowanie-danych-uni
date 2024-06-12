#Podpis ElGamal

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
    
def klucz(p,g,a):
    return pow(g,a,p)

def elgamal_sig(g,p,A,a,b,x):
    B = pow(g,b,p)
    # C=((x-a*B)*pow(b,-1,p-1))%(p-1)
    C = ((x-a*B)*odwrot(b,p-1))%(p-1)
    return B,C

def elgamal_ver(A,B,C,g,x,p):
    if (pow(A,B,p)*pow(B,C,p))%p == pow(g,x,p):
        print("ver(%d,(%d,%d)) = tak" %(x,B,C))
    else:
        print("ver(%d,(%d,%d)) = nie" %(x,B,C))
        
p=int(input("Podaj p: "))
g=int(input("Podaj g: "))
a=int(input("Podaj a: "))

A=klucz(p,g,a)

print("*Generowanie klucza*")
print("Klucz publiczny: (g,A) = (%d,%d)" %(g,A))
print("Klucz prywatny: a = ",a)

print("*Podpis*")
x=int(input("Podaj x: "))
b=int(input("Podaj b: "))

B,C = elgamal_sig(g,p,A,a,b,x)
print("sig(%d) = (%d, %d)" %(x,B,C))

print("*Weryfikacja*")
elgamal_ver(A,B,C,g,x,p)