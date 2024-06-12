#Podpis DSA
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
    
def dsa_sig(g,p,q,A,a,b,x):
    B = pow(g,b,p)%q
    C = ((x+a*B)%q*odwrot(b,q))%q
    return B,C

def dsa_ver(A,B,C,g,x,p,q):
    e = (x*odwrot(C,q))%q
    f = (B*odwrot(C,q))%q
    
    if ((pow(g,e,p) * pow(A,f,p))%p)%q == B:
        print("ver(%d,(%d,%d)) = tak" %(x,B,C))
    else:
        print("ver(%d,(%d,%d)) = nie" %(x,B,C))
        
print("*Generowanie klucza*")
p=int(input("Podaj p: "))
q=int(input("Podaj q: "))

if(p-1)%q!=0:
    print("Wybierz inne q")
else:
    print("q|(p-1)")
    
alfa=int(input("Podaj alfa: "))
a=int(input("Podaj a: "))

wykl=int((p-1)/q)
g=pow(alfa,wykl,p)
A=pow(g,a,p)

print("Klucz publiczny: (g,A) = (%d,%d)" %(g,A))
print("Klucz prywatny: a = ",a)

print("*Podpis*")
x=int(input("Podaj x: "))
b=int(input("Podaj b: "))

B,C = dsa_sig(g,p,q,A,a,b,x)
print("sig(%d) = (%d, %d)" %(x,B,C))

print("*Weryfikacja*")
dsa_ver(A,B,C,g,x,p,q)