#Podpis RSA

#Szyfr RSA - szyfruje i deszyfruje tekst w postaci liczby naturalnej

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
    #q(n)=q(p*q)=q(p)*q(q)=(p-1)(q-1)

#klucz prywatny!
def pryw_wykl(b,p,q):
    return odwrot(b,(p-1)*(q-1))

def rsa_sig(x,a,n):
    return pow(x,a,n)

def rsa_ver(x,y,b,n):
    if pow(y,b,n) == x:
        print("ver(%d,%d) = tak" %(x,y))
    else:
        print("ver(%d,%d) = nie" %(x,y))
    
print("*Generowanie klucza*")
p = int(input("Podaj liczbę pierwszą p: "))
q = int(input("Podaj liczbę pierwszą q: "))
#pow(b,-1,(p-1)*(q-1))

n=p*q
b=pub_wykl(p,q)
print("Klucz publiczny: (%d,%d)"%(n,b))

a=pryw_wykl(b,p,q)
print("Klucz prywatny: ",a)

print("*Podpis*")
x=int(input("Podaj x: "))
y=rsa_sig(x,a,n)
print("sig(%d) = %d" %(x,y))

print("*Weryfikacja*")
rsa_ver(x,y,b,n)